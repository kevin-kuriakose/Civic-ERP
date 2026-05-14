"""
Install CivicEdge notifications.
Run: bench --site mysite.local execute civic_erp.civic_operations.notification.install_notifications.run
"""
import frappe
import json
import os


def run():
    notif_dir = os.path.join(
        os.path.dirname(__file__)
    )
    count = 0
    for fname in os.listdir(notif_dir):
        if not fname.endswith(".json") or fname == "__init__.py":
            continue
        fpath = os.path.join(notif_dir, fname)
        try:
            with open(fpath) as f:
                data = json.load(f)
        except Exception as e:
            print(f"  Error reading {fname}: {e}")
            continue

        name = data.get("name")
        if not name:
            continue

        if frappe.db.exists("Notification", name):
            doc = frappe.get_doc("Notification", name)
            for k, v in data.items():
                if k not in ("creation", "modified", "modified_by", "owner"):
                    doc.set(k, v)
            doc.save(ignore_permissions=True)
            print(f"  Updated: {name}")
        else:
            for field in ("creation", "modified", "modified_by", "owner"):
                data.pop(field, None)
            try:
                frappe.get_doc(data).insert(ignore_permissions=True)
                print(f"  Inserted: {name}")
                count += 1
            except Exception as e:
                print(f"  Error inserting {name}: {e}")

    frappe.db.commit()
    print(f"\n✅ {count} notifications installed")
