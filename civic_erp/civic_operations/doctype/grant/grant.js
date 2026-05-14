frappe.ui.form.on("Grant", {
    refresh(frm) {
        if (!frm.is_new()) {
            const days_left = frm.doc.end_date ?
                Math.ceil((new Date(frm.doc.end_date) - new Date()) / 86400000) : null;
            if (days_left !== null) {
                const color = days_left < 30 ? "red" : days_left < 90 ? "orange" : "green";
                frm.dashboard.add_indicator(
                    __("{0} days remaining", [days_left]), color);
            }
        }
    }
});
