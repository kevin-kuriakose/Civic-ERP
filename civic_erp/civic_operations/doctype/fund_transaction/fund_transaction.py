import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FundTransaction(Document):

    def validate(self):
        if flt(self.amount) <= 0:
            frappe.throw(_("Amount must be greater than zero"))

    def on_submit(self):
        self._update_fund_balance()

    def on_cancel(self):
        self._reverse_fund_balance()

    def _update_fund_balance(self):
        fund = frappe.get_doc("Fund", self.fund)
        current = flt(fund.balance)
        if self.direction == "In":
            new_balance = current + flt(self.amount)
        else:
            new_balance = current - flt(self.amount)
            if new_balance < 0:
                frappe.throw(_(
                    f"Insufficient fund balance. Available: Rs {current:.2f}"))
        frappe.db.set_value("Fund", self.fund, "balance", new_balance)
        frappe.db.commit()

    def _reverse_fund_balance(self):
        fund = frappe.get_doc("Fund", self.fund)
        current = flt(fund.balance)
        if self.direction == "In":
            new_balance = current - flt(self.amount)
        else:
            new_balance = current + flt(self.amount)
        frappe.db.set_value("Fund", self.fund, "balance", new_balance)
        frappe.db.commit()
