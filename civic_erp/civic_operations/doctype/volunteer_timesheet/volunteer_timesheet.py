import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class VolunteerTimesheet(Document):

    def validate(self):
        from frappe.utils import flt
        # Parse hours from activities text as fallback
        pass

    def on_submit(self):
        from frappe.utils import flt
        vol = frappe.get_doc("Volunteer", self.volunteer)
        new_total = flt(vol.total_hours_contributed) + flt(self.total_hours)
        frappe.db.set_value("Volunteer", self.volunteer,
            "total_hours_contributed", new_total)
        frappe.db.commit()

