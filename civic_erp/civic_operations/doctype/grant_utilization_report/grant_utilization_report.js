frappe.ui.form.on("Grant Utilization Report", {
    budget_lines_on_form_rendered(frm) { frm.trigger("calculate_totals"); },
    calculate_totals(frm) {
        let total = 0;
        (frm.doc.budget_lines || []).forEach(row => {
            total += flt(row.spent_amount);
            frappe.model.set_value(row.doctype, row.name, "variance",
                flt(row.allocated_amount) - flt(row.spent_amount));
        });
        frm.set_value("total_expenditure", total);
    }
});
