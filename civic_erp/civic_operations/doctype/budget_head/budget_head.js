frappe.ui.form.on("Budget Head", {
    budget_allocation(frm) {
        frm.set_value("variance",
            flt(frm.doc.budget_allocation) - flt(frm.doc.spent_amount));
    },
    spent_amount(frm) {
        frm.set_value("variance",
            flt(frm.doc.budget_allocation) - flt(frm.doc.spent_amount));
    }
});
