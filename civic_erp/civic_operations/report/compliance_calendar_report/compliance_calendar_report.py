import frappe
from frappe import _
from frappe.utils import getdate, today, date_diff


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Obligation"), "fieldname": "obligation_type",
         "fieldtype": "Data", "width": 200},
        {"label": _("Due Date"), "fieldname": "due_date",
         "fieldtype": "Date", "width": 120},
        {"label": _("Days Remaining"), "fieldname": "days_remaining",
         "fieldtype": "Int", "width": 130},
        {"label": _("Filed Date"), "fieldname": "filed_date",
         "fieldtype": "Date", "width": 120},
        {"label": _("Status"), "fieldname": "status",
         "fieldtype": "Data", "width": 100},
        {"label": _("Penalty"), "fieldname": "penalty_amount",
         "fieldtype": "Currency", "width": 120},
    ]


def get_data(filters):
    rows = frappe.db.sql("""
        SELECT obligation_type, due_date, filed_date,
               status, penalty_amount
        FROM `tabCompliance Tracker`
        ORDER BY due_date ASC
    """, as_dict=True)

    result = []
    for r in rows:
        days = date_diff(r.due_date, today()) if r.due_date else 0
        result.append({
            "obligation_type": r.obligation_type,
            "due_date": r.due_date,
            "days_remaining": days,
            "filed_date": r.filed_date,
            "status": r.status,
            "penalty_amount": r.penalty_amount or 0,
        })
    return sorted(result, key=lambda x: x["due_date"] or "9999-12-31")
