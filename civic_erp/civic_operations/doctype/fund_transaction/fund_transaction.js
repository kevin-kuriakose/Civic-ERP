frappe.ui.form.on("Fund Transaction", {
    refresh(frm) {
        if (!frm.is_new()) {
            const color = frm.doc.direction === "In" ? "green" : "orange";
            frm.dashboard.add_indicator(
                __(frm.doc.direction === "In" ? "Inflow" : "Outflow"), color);
        }
    }
});
