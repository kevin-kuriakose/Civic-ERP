import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class Donation(Document):

    def on_submit(self):
        if not frappe.db.get_value("Donor", self.donor, "first_donation_date"):
            frappe.db.set_value("Donor", self.donor, "first_donation_date",
                self.donation_date)
        self._update_fund_balance()

    def _update_fund_balance(self):
        if self.fund:
            fund_bal = flt(frappe.db.get_value("Fund", self.fund, "balance"))
            frappe.db.set_value("Fund", self.fund, "balance",
                fund_bal + flt(self.amount))
            frappe.db.commit()

    def on_cancel(self):
        if self.fund:
            fund_bal = flt(frappe.db.get_value("Fund", self.fund, "balance"))
            frappe.db.set_value("Fund", self.fund, "balance",
                fund_bal - flt(self.amount))
            frappe.db.commit()

