frappe.ui.form.on("Fund", {
    refresh(frm) {
        if (!frm.is_new()) {
            const color = flt(frm.doc.balance) > 0 ? "green" : "red";
            frm.dashboard.add_indicator(
                __("Balance: Rs {0}", [format_currency(frm.doc.balance, "INR")]),
                color
            );
        }
    },
    opening_balance(frm) {
        if (frm.is_new()) {
            frm.set_value("balance", flt(frm.doc.opening_balance));
        }
    }
});
