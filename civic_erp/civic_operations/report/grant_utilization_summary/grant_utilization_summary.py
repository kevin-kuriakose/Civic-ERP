import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Grant"), "fieldname": "grant_title", "fieldtype": "Data", "width": 200},
        {"label": _("Agency"), "fieldname": "granting_agency", "fieldtype": "Data", "width": 150},
        {"label": _("Budget Category"), "fieldname": "budget_category",
         "fieldtype": "Data", "width": 150},
        {"label": _("Allocated"), "fieldname": "allocated_amount",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Spent"), "fieldname": "spent_amount",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Variance"), "fieldname": "variance",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Utilization %"), "fieldname": "utilization_pct",
         "fieldtype": "Float", "width": 120},
    ]


def get_data(filters):
    rows = frappe.db.sql("""
        SELECT g.grant_title, g.granting_agency,
               gb.budget_category, gb.allocated_amount,
               gb.spent_amount, gb.variance
        FROM `tabGrant` g
        LEFT JOIN `tabGrant Budget Line` gb ON gb.parent = g.name
        WHERE g.status IN ('Active','Closed')
        ORDER BY g.grant_title, gb.budget_category
    """, as_dict=True)

    result = []
    for r in rows:
        alloc = flt(r.allocated_amount)
        spent = flt(r.spent_amount)
        pct = round((spent / alloc * 100), 1) if alloc else 0
        result.append({
            "grant_title": r.grant_title or "",
            "granting_agency": r.granting_agency or "",
            "budget_category": r.budget_category or "(No budget lines)",
            "allocated_amount": alloc,
            "spent_amount": spent,
            "variance": flt(r.variance),
            "utilization_pct": pct,
        })
    return result
