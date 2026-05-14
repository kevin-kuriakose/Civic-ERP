import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("CSR Project"), "fieldname": "project_name",
         "fieldtype": "Data", "width": 200},
        {"label": _("Corporate Donor"), "fieldname": "corporate_donor",
         "fieldtype": "Data", "width": 150},
        {"label": _("Theme"), "fieldname": "theme",
         "fieldtype": "Data", "width": 130},
        {"label": _("CSR Amount"), "fieldname": "csr_amount",
         "fieldtype": "Currency", "width": 140},
        {"label": _("Total Spent"), "fieldname": "total_spent",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Remaining"), "fieldname": "remaining",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Reports Filed"), "fieldname": "reports_filed",
         "fieldtype": "Int", "width": 110},
        {"label": _("Status"), "fieldname": "status",
         "fieldtype": "Data", "width": 100},
    ]


def get_data(filters):
    projects = frappe.db.sql("""
        SELECT name, project_name, corporate_donor, theme,
               csr_amount, status
        FROM `tabCSR Project`
        ORDER BY project_name
    """, as_dict=True)

    result = []
    for p in projects:
        spent_result = frappe.db.sql("""
            SELECT COALESCE(SUM(expenditure), 0) as total
            FROM `tabCSR Utilization Report`
            WHERE csr_project = %s AND docstatus = 1
        """, p.name, as_dict=True)
        spent = flt(spent_result[0].total if spent_result else 0)
        csr = flt(p.csr_amount)
        reports = frappe.db.count("CSR Utilization Report",
            {"csr_project": p.name, "docstatus": 1})
        result.append({
            "project_name": p.project_name,
            "corporate_donor": p.corporate_donor,
            "theme": p.theme,
            "csr_amount": csr,
            "total_spent": spent,
            "remaining": csr - spent,
            "reports_filed": reports,
            "status": p.status,
        })
    return result
