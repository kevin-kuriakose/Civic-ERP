import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class Fund(Document):

    def validate(self):
        if flt(self.opening_balance) < 0:
            frappe.throw(_("Opening Balance cannot be negative"))
        if not self.balance:
            self.balance = flt(self.opening_balance)

    def after_insert(self):
        if flt(self.opening_balance) > 0:
            self.balance = flt(self.opening_balance)
            frappe.db.set_value("Fund", self.name, "balance",
                self.balance)
            frappe.db.commit()
