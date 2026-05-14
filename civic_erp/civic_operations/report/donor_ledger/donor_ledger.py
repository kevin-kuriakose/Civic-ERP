import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Donor"), "fieldname": "donor_name", "fieldtype": "Data", "width": 180},
        {"label": _("Type"), "fieldname": "donor_type", "fieldtype": "Data", "width": 100},
        {"label": _("Date"), "fieldname": "donation_date", "fieldtype": "Date", "width": 100},
        {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Mode"), "fieldname": "mode_of_payment", "fieldtype": "Data", "width": 110},
        {"label": _("Purpose"), "fieldname": "purpose", "fieldtype": "Data", "width": 150},
        {"label": _("80G Issued"), "fieldname": "is_80g_receipt_issued",
         "fieldtype": "Check", "width": 100},
        {"label": _("Cumulative Total"), "fieldname": "cumulative_total",
         "fieldtype": "Currency", "width": 150},
    ]


def get_data(filters):
    cond = ""
    if filters.get("donor"):
        cond += f" AND d.name = '{filters['donor']}'"

    rows = frappe.db.sql(f"""
        SELECT dn.donor, dr.donor_name, dr.donor_type,
               dn.donation_date, dn.amount, dn.mode_of_payment,
               dn.purpose, dn.is_80g_receipt_issued
        FROM `tabDonation` dn
        JOIN `tabDonor` dr ON dr.name = dn.donor
        WHERE dn.docstatus = 1 {cond}
        ORDER BY dr.donor_name, dn.donation_date
    """, as_dict=True)

    result = []
    cumulative = {}
    for r in rows:
        key = r.donor
        cumulative[key] = flt(cumulative.get(key, 0)) + flt(r.amount)
        result.append({
            "donor_name": r.donor_name,
            "donor_type": r.donor_type,
            "donation_date": r.donation_date,
            "amount": flt(r.amount),
            "mode_of_payment": r.mode_of_payment,
            "purpose": r.purpose,
            "is_80g_receipt_issued": r.is_80g_receipt_issued,
            "cumulative_total": cumulative[key],
        })
    return result
