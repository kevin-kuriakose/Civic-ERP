import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Fund"), "fieldname": "fund_name", "fieldtype": "Data", "width": 200},
        {"label": _("Type"), "fieldname": "fund_type", "fieldtype": "Data", "width": 120},
        {"label": _("Source"), "fieldname": "source", "fieldtype": "Data", "width": 120},
        {"label": _("Opening Balance"), "fieldname": "opening_balance",
         "fieldtype": "Currency", "width": 150},
        {"label": _("Current Balance"), "fieldname": "balance",
         "fieldtype": "Currency", "width": 150},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]


def get_data(filters):
    cond = ""
    if filters.get("fund_type"):
        cond += f" AND fund_type = '{filters['fund_type']}'"
    if filters.get("status"):
        cond += f" AND status = '{filters['status']}'"

    rows = frappe.db.sql(f"""
        SELECT fund_name, fund_type, source,
               opening_balance, balance, status
        FROM `tabFund`
        WHERE 1=1 {cond}
        ORDER BY fund_type, fund_name
    """, as_dict=True)

    result = []
    restricted_total = 0
    unrestricted_total = 0

    for r in rows:
        result.append({
            "fund_name": r.fund_name,
            "fund_type": r.fund_type,
            "source": r.source,
            "opening_balance": flt(r.opening_balance),
            "balance": flt(r.balance),
            "status": r.status,
        })
        if r.fund_type == "Restricted":
            restricted_total += flt(r.balance)
        else:
            unrestricted_total += flt(r.balance)

    if result:
        result.append({
            "fund_name": "RESTRICTED TOTAL",
            "fund_type": "", "source": "", "opening_balance": 0,
            "balance": restricted_total, "status": "",
        })
        result.append({
            "fund_name": "UNRESTRICTED TOTAL",
            "fund_type": "", "source": "", "opening_balance": 0,
            "balance": unrestricted_total, "status": "",
        })
    return result
