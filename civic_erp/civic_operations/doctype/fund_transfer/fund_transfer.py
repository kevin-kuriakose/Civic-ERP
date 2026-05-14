import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FundTransfer(Document):

    def validate(self):
        if flt(self.amount) <= 0:
            frappe.throw(_("Amount must be greater than zero"))
        if self.source_fund == self.destination_fund:
            frappe.throw(_("Source and Destination funds cannot be the same"))

    def on_submit(self):
        if self.approval_status != "Approved":
            frappe.throw(_("Fund Transfer must be Approved before submit"))
        self._execute_transfer()

    def on_cancel(self):
        self._reverse_transfer()

    def _execute_transfer(self):
        src = frappe.get_doc("Fund", self.source_fund)
        if flt(src.balance) < flt(self.amount):
            frappe.throw(_(
                f"Insufficient balance in {self.source_fund}. "
                f"Available: Rs {src.balance:.2f}"))
        frappe.db.set_value("Fund", self.source_fund, "balance",
            flt(src.balance) - flt(self.amount))
        dst = frappe.get_doc("Fund", self.destination_fund)
        frappe.db.set_value("Fund", self.destination_fund, "balance",
            flt(dst.balance) + flt(self.amount))
        frappe.db.commit()

    def _reverse_transfer(self):
        src = frappe.get_doc("Fund", self.source_fund)
        frappe.db.set_value("Fund", self.source_fund, "balance",
            flt(src.balance) + flt(self.amount))
        dst = frappe.get_doc("Fund", self.destination_fund)
        frappe.db.set_value("Fund", self.destination_fund, "balance",
            flt(dst.balance) - flt(self.amount))
        frappe.db.commit()
