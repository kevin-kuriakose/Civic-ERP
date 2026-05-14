import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Volunteer"), "fieldname": "volunteer_name",
         "fieldtype": "Data", "width": 180},
        {"label": _("Week Starting"), "fieldname": "week_start_date",
         "fieldtype": "Date", "width": 130},
        {"label": _("Hours"), "fieldname": "total_hours",
         "fieldtype": "Float", "width": 100},
        {"label": _("Cumulative Hours"), "fieldname": "cumulative_hours",
         "fieldtype": "Float", "width": 140},
        {"label": _("Verified By"), "fieldname": "verified_by",
         "fieldtype": "Data", "width": 140},
    ]


def get_data(filters):
    rows = frappe.db.sql("""
        SELECT vt.volunteer, v.volunteer_name,
               vt.week_start_date, vt.total_hours, vt.verified_by
        FROM `tabVolunteer Timesheet` vt
        JOIN `tabVolunteer` v ON v.name = vt.volunteer
        WHERE vt.docstatus = 1
        ORDER BY v.volunteer_name, vt.week_start_date
    """, as_dict=True)

    result = []
    cumulative = {}
    for r in rows:
        key = r.volunteer
        cumulative[key] = flt(cumulative.get(key, 0)) + flt(r.total_hours)
        result.append({
            "volunteer_name": r.volunteer_name,
            "week_start_date": r.week_start_date,
            "total_hours": flt(r.total_hours),
            "cumulative_hours": cumulative[key],
            "verified_by": r.verified_by,
        })
    return result
