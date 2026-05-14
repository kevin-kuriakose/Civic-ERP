import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Month/Year"), "fieldname": "month_year",
         "fieldtype": "Data", "width": 130},
        {"label": _("Foreign (FCRA) Receipts"), "fieldname": "fcra_amount",
         "fieldtype": "Currency", "width": 180},
        {"label": _("Domestic Receipts"), "fieldname": "domestic_amount",
         "fieldtype": "Currency", "width": 160},
        {"label": _("Total"), "fieldname": "total",
         "fieldtype": "Currency", "width": 130},
        {"label": _("FCRA %"), "fieldname": "fcra_pct",
         "fieldtype": "Float", "width": 100},
    ]


def get_data(filters):
    # Foreign contributions
    fcra_rows = frappe.db.sql("""
        SELECT DATE_FORMAT(receipt_date, '%Y-%m') as month_year,
               SUM(inr_equivalent) as amount
        FROM `tabForeign Contribution`
        WHERE docstatus = 1
        GROUP BY month_year
        ORDER BY month_year DESC
    """, as_dict=True)
    fcra_map = {r.month_year: flt(r.amount) for r in fcra_rows}

    # Domestic donations
    dom_rows = frappe.db.sql("""
        SELECT DATE_FORMAT(donation_date, '%Y-%m') as month_year,
               SUM(amount) as amount
        FROM `tabDonation`
        WHERE docstatus = 1
        GROUP BY month_year
        ORDER BY month_year DESC
    """, as_dict=True)
    dom_map = {r.month_year: flt(r.amount) for r in dom_rows}

    all_months = sorted(set(list(fcra_map.keys()) + list(dom_map.keys())),
                        reverse=True)
    result = []
    for m in all_months:
        fcra = flt(fcra_map.get(m, 0))
        domestic = flt(dom_map.get(m, 0))
        total = fcra + domestic
        pct = round(fcra / total * 100, 1) if total else 0
        result.append({
            "month_year": m,
            "fcra_amount": fcra,
            "domestic_amount": domestic,
            "total": total,
            "fcra_pct": pct,
        })
    return result
