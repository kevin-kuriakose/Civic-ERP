import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class SalaryCostAllocation(Document):

    def validate(self):
        from frappe.utils import flt
        total = flt(self.fund_percent) + flt(self.grant_percent) + flt(self.program_percent)
        if abs(total - 100) > 0.01:
            import frappe
            frappe.throw(f"Fund + Grant + Program allocations must total 100%. Currently: {total:.1f}%")

