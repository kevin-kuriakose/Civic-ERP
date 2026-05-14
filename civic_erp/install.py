import frappe


def after_install():
    frappe.db.commit()
    print("✅ CivicEdge ERP installed successfully")
