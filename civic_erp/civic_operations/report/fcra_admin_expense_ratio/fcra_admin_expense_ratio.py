import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Financial Year"), "fieldname": "financial_year",
         "fieldtype": "Data", "width": 120},
        {"label": _("Total Foreign Received"), "fieldname": "total_foreign_received",
         "fieldtype": "Currency", "width": 170},
        {"label": _("Total Utilized"), "fieldname": "total_utilized",
         "fieldtype": "Currency", "width": 150},
        {"label": _("Admin Expense %"), "fieldname": "admin_pct",
         "fieldtype": "Float", "width": 130},
        {"label": _("Program Expense %"), "fieldname": "program_pct",
         "fieldtype": "Float", "width": 140},
        {"label": _("Status"), "fieldname": "compliance_status",
         "fieldtype": "Data", "width": 120},
    ]


def get_data(filters):
    rows = frappe.db.sql("""
        SELECT financial_year, total_foreign_received,
               total_utilized, admin_expense_percent, program_expense_percent
        FROM `tabFCRA Annual Return`
        ORDER BY financial_year DESC
    """, as_dict=True)

    result = []
    for r in rows:
        admin = flt(r.admin_expense_percent)
        status = "✅ Compliant"
        if admin > 20:
            status = "❌ BREACH (>20%)"
        elif admin > 18:
            status = "⚠️ Warning (>18%)"

        result.append({
            "financial_year": r.financial_year,
            "total_foreign_received": flt(r.total_foreign_received),
            "total_utilized": flt(r.total_utilized),
            "admin_pct": admin,
            "program_pct": flt(r.program_expense_percent),
            "compliance_status": status,
        })
    return result
