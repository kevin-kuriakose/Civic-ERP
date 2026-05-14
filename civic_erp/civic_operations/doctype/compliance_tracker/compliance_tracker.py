import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class ComplianceTracker(Document):

    def validate(self):
        from frappe.utils import getdate, today
        import frappe
        if self.due_date and getdate(self.due_date) < getdate(today()) and self.status == "Pending":
            self.status = "Overdue"

