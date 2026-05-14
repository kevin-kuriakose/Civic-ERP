frappe.ui.form.on("Grant Disbursement", {
    refresh(frm) {
        const color = frm.doc.status === "Received" ? "green" :
                      frm.doc.status === "Delayed" ? "red" : "orange";
        frm.dashboard.add_indicator(__(frm.doc.status || "Pending"), color);
    }
});
