import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class BudgetHead(Document):

    def validate(self):
        self.variance = flt(self.budget_allocation) - flt(self.spent_amount)
        if flt(self.budget_allocation) <= 0:
            frappe.throw(_("Budget Allocation must be greater than zero"))
        if self.variance < 0:
            self.status = "Exhausted"
