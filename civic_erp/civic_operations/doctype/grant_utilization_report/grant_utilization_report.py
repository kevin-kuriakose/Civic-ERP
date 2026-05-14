import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class GrantUtilizationReport(Document):

    def validate(self):
        total = sum(flt(row.spent_amount) for row in self.budget_lines or [])
        self.total_expenditure = total
        grant_total = flt(frappe.db.get_value(
            "Grant", self.grant, "total_amount"))
        self.balance = grant_total - total
