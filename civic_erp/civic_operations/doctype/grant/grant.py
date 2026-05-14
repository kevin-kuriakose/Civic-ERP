import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class Grant(Document):

    def validate(self):
        if getdate(self.end_date) <= getdate(self.start_date):
            frappe.throw(_("End Date must be after Start Date"))
        for row in self.budget_lines or []:
            row.variance = flt(row.allocated_amount) - flt(row.spent_amount)
