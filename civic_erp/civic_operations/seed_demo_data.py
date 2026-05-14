"""
CivicEdge ERP Demo Data
Run: bench --site mysite.local execute civic_erp.civic_operations.seed_demo_data.run
"""
import frappe
from frappe.utils import today, add_months, add_days


def run():
    print("=" * 60)
    print("  CivicEdge ERP — Demo Data")
    print("=" * 60)

    company = frappe.defaults.get_user_default("Company") or "bizaxl"

    # ── Funds ─────────────────────────────────────────────────
    funds = [
        ("Education Fund", "Restricted", "Donor", 500000),
        ("Health Program Fund", "Restricted", "Grant", 1000000),
        ("Admin Operations", "Unrestricted", "Donor", 200000),
        ("FCRA Operations", "Restricted", "Government", 750000),
        ("Emergency Relief", "Emergency Relief", "Donor", 100000),
    ]
    for name, ftype, source, balance in funds:
        if not frappe.db.exists("Fund", {"fund_name": name}):
            frappe.get_doc({
                "doctype": "Fund",
                "naming_series": "FUND-.YYYY.-.#####",
                "fund_name": name,
                "fund_type": ftype,
                "source": source,
                "status": "Active",
                "opening_balance": balance,
                "balance": balance,
            }).insert(ignore_permissions=True)
            print(f"  Fund: {name}")
    frappe.db.commit()
    print("✅ Funds created")

    # ── Fiscal Year check ─────────────────────────────────────
    fy = frappe.db.get_value("Fiscal Year", {}, "name")
    print(f"  Fiscal Year: {fy}")

    # ── Donors ────────────────────────────────────────────────
    donors = [
        ("Tata Trusts", "Corporate", "Major Donor"),
        ("Infosys Foundation", "CSR", "Major Donor"),
        ("Rahul Mehta", "Individual", "Regular Donor"),
        ("Priya Sharma", "Individual", "Small Donor"),
        ("USAID", "Foreign", "Major Donor"),
    ]
    for dname, dtype, tier in donors:
        if not frappe.db.exists("Donor", {"donor_name": dname}):
            frappe.get_doc({
                "doctype": "Donor",
                "naming_series": "DONOR-.YYYY.-.#####",
                "donor_name": dname,
                "donor_type": dtype,
                "donor_tier": tier,
                "is_80g_eligible": 1,
                "is_fcra_donor": 1 if dtype == "Foreign" else 0,
                "status": "Active",
            }).insert(ignore_permissions=True)
            print(f"  Donor: {dname}")
    frappe.db.commit()
    print("✅ Donors created")

    # ── Grant ─────────────────────────────────────────────────
    if not frappe.db.exists("Grant", {"grant_title": "USAID Health Initiative 2026"}):
        frappe.get_doc({
            "doctype": "Grant",
            "naming_series": "GRNT-.YYYY.-.#####",
            "grant_title": "USAID Health Initiative 2026",
            "granting_agency": "USAID",
            "grant_type": "International",
            "total_amount": 5000000,
            "start_date": today(),
            "end_date": add_months(today(), 24),
            "reporting_frequency": "Quarterly",
            "status": "Active",
            "budget_lines": [
                {"budget_category": "Medical Supplies",
                 "allocated_amount": 2000000, "spent_amount": 0},
                {"budget_category": "Staff Salaries",
                 "allocated_amount": 1500000, "spent_amount": 0},
                {"budget_category": "Training",
                 "allocated_amount": 1000000, "spent_amount": 0},
                {"budget_category": "Admin",
                 "allocated_amount": 500000, "spent_amount": 0},
            ],
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        print("✅ Grant created")

    # ── Programs ──────────────────────────────────────────────
    programs = [
        ("Digital Literacy for Rural Youth", "Digital Literacy"),
        ("Mother and Child Health", "Health"),
        ("Women Livelihood Training", "Livelihood"),
    ]
    for pname, ptype in programs:
        if not frappe.db.exists("Program", {"program_name": pname}):
            frappe.get_doc({
                "doctype": "Program",
                "naming_series": "PRG-.YYYY.-.#####",
                "program_name": pname,
                "program_type": ptype,
                "target_beneficiary_count": 500,
                "start_date": today(),
                "end_date": add_months(today(), 12),
                "budget": 500000,
                "status": "Active",
            }).insert(ignore_permissions=True)
            print(f"  Program: {pname}")
    frappe.db.commit()
    print("✅ Programs created")

    # ── Board Members ─────────────────────────────────────────
    members = [
        ("Dr. Anita Sharma", "Chairperson"),
        ("Mr. Rajesh Kumar", "Secretary"),
        ("Ms. Priya Patel", "Treasurer"),
        ("Prof. S. Krishnan", "Board Member"),
        ("Mr. Arun Singh", "Board Member"),
    ]
    for mname, designation in members:
        if not frappe.db.exists("Board Member", {"member_name": mname}):
            frappe.get_doc({
                "doctype": "Board Member",
                "naming_series": "BM-.YYYY.-.#####",
                "member_name": mname,
                "designation": designation,
                "term_start": add_months(today(), -12),
                "term_end": add_months(today(), 24),
                "background_declaration_signed": 1,
                "status": "Active",
            }).insert(ignore_permissions=True)
            print(f"  Board Member: {mname}")
    frappe.db.commit()
    print("✅ Board Members created")

    # ── Compliance Tracker entries ────────────────────────────
    obligations = [
        ("FCRA Annual Return", add_months(today(), 3)),
        ("Income Tax Return", add_months(today(), 4)),
        ("80G Renewal", add_months(today(), 2)),
        ("ROC Filing", add_months(today(), 1)),
        ("Audit Completion", add_months(today(), 5)),
    ]
    for obl, due in obligations:
        if not frappe.db.exists("Compliance Tracker",
                                {"obligation_type": obl, "status": "Pending"}):
            frappe.get_doc({
                "doctype": "Compliance Tracker",
                "naming_series": "CT-.YYYY.-.#####",
                "obligation_type": obl,
                "due_date": due,
                "status": "Pending",
            }).insert(ignore_permissions=True)
            print(f"  Compliance: {obl}")
    frappe.db.commit()

    print("")
    print("=" * 60)
    print("  Demo data complete!")
    print("  Visit /app/civicedge to explore the workspace")
    print("=" * 60)
