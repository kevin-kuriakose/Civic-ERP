frappe.ui.form.on("Fund Transfer", {
    refresh(frm) {
        if (frm.doc.docstatus === 0 && !frm.is_new() &&
            frm.doc.approval_status === "Pending") {
            frm.add_custom_button(__("Approve"), () => {
                frm.set_value("approval_status", "Approved");
                frm.save();
            }).addClass("btn-success");
            frm.add_custom_button(__("Reject"), () => {
                frm.set_value("approval_status", "Rejected");
                frm.save();
            }).addClass("btn-danger");
        }
    }
});
