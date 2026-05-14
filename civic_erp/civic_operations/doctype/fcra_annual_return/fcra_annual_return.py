import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FCRAAnnualReturn(Document):

    def validate(self):
        total = flt(self.total_foreign_received)
        utilized = flt(self.total_utilized)
        if total > 0:
            # Calculate admin vs program split from FCRA Utilization Entries
            admin = flt(frappe.db.sql("""
                SELECT SUM(amount) FROM `tabFCRA Utilization Entry`
                WHERE is_admin_expense=1 AND docstatus=1
            """)[0][0])
            program = utilized - admin
            self.admin_expense_percent = round((admin / total) * 100, 2) if total else 0
            self.program_expense_percent = round((program / total) * 100, 2) if total else 0
            if self.admin_expense_percent > 20:
                frappe.msgprint(
                    "⚠️ Admin expense ratio {:.1f}% exceeds FCRA 20% limit".format(
                        self.admin_expense_percent),
                    alert=True, indicator="red")
            elif self.admin_expense_percent > 18:
                frappe.msgprint(
                    "⚠️ Admin expense ratio {:.1f}% approaching FCRA 20% limit".format(
                        self.admin_expense_percent),
                    alert=True, indicator="orange")

