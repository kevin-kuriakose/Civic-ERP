import frappe
from frappe import _


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Meeting Date"), "fieldname": "meeting_date",
         "fieldtype": "Date", "width": 120},
        {"label": _("Meeting"), "fieldname": "meeting_name",
         "fieldtype": "Data", "width": 160},
        {"label": _("Attendance List"), "fieldname": "attendance_list",
         "fieldtype": "Data", "width": 300},
        {"label": _("Total Board Members"), "fieldname": "total_members",
         "fieldtype": "Int", "width": 150},
        {"label": _("Quorum Met"), "fieldname": "quorum_met",
         "fieldtype": "Data", "width": 110},
    ]


def get_data(filters):
    meetings = frappe.db.sql("""
        SELECT name, date, attendance_list
        FROM `tabBoard Meeting`
        WHERE docstatus = 1
        ORDER BY date DESC
    """, as_dict=True)

    total_members = frappe.db.count("Board Member", {"status": "Active"})
    quorum_required = max(3, (total_members // 3))

    result = []
    for m in meetings:
        attendees = len([x for x in (m.attendance_list or "").split(",") if x.strip()])
        quorum = "✅ Yes" if attendees >= quorum_required else "❌ No"
        result.append({
            "meeting_date": m.date,
            "meeting_name": m.name,
            "attendance_list": m.attendance_list or "",
            "total_members": attendees,
            "quorum_met": quorum,
        })
    return result
