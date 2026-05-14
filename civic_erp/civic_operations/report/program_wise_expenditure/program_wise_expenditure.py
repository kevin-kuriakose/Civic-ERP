import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    return get_columns(), get_data(filters or {})


def get_columns():
    return [
        {"label": _("Program"), "fieldname": "program_name",
         "fieldtype": "Data", "width": 200},
        {"label": _("Type"), "fieldname": "program_type",
         "fieldtype": "Data", "width": 130},
        {"label": _("Budget"), "fieldname": "budget",
         "fieldtype": "Currency", "width": 130},
        {"label": _("Beneficiaries"), "fieldname": "beneficiary_count",
         "fieldtype": "Int", "width": 120},
        {"label": _("Cost per Beneficiary"), "fieldname": "cost_per_beneficiary",
         "fieldtype": "Currency", "width": 160},
        {"label": _("Status"), "fieldname": "status",
         "fieldtype": "Data", "width": 100},
    ]


def get_data(filters):
    programs = frappe.db.sql("""
        SELECT name, program_name, program_type, budget, status
        FROM `tabProgram`
        ORDER BY program_type, program_name
    """, as_dict=True)

    result = []
    for p in programs:
        benf_count = frappe.db.count("Beneficiary Enrollment",
            {"program": p.name})
        budget = flt(p.budget)
        cpb = round(budget / benf_count, 2) if benf_count else 0
        result.append({
            "program_name": p.program_name,
            "program_type": p.program_type,
            "budget": budget,
            "beneficiary_count": benf_count,
            "cost_per_beneficiary": cpb,
            "status": p.status,
        })
    return result
