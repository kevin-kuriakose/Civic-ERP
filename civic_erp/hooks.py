from . import __version__ as app_version

app_name = "civic_erp"
app_title = "CivicEdge ERP"
app_publisher = "bizaxl"
app_description = "ERP for Government Bodies and Non-Profit Organizations"
app_email = "admin@bizaxl.com"
app_license = "MIT"
app_version = "0.0.1"

required_apps = ["frappe", "erpnext"]

app_include_css = "/assets/civic_erp/css/civic_erp.css"
app_include_js = "/assets/civic_erp/js/civic_erp.js"

doc_events = {}

scheduler_events = {
    "daily": [],
    "weekly": [],
}

after_install = "civic_erp.install.after_install"

override_doctype_class = {
    "Fund": "civic_erp.civic_operations.doctype.fund.fund.Fund",
    "Fund Transaction": "civic_erp.civic_operations.doctype.fund_transaction.fund_transaction.FundTransaction",
    "Budget Head": "civic_erp.civic_operations.doctype.budget_head.budget_head.BudgetHead",
    "Fund Transfer": "civic_erp.civic_operations.doctype.fund_transfer.fund_transfer.FundTransfer",
    "Grant": "civic_erp.civic_operations.doctype.grant.grant.Grant",
    "Grant Application": "civic_erp.civic_operations.doctype.grant_application.grant_application.GrantApplication",
    "Grant Disbursement": "civic_erp.civic_operations.doctype.grant_disbursement.grant_disbursement.GrantDisbursement",
    "Grant Utilization Report": "civic_erp.civic_operations.doctype.grant_utilization_report.grant_utilization_report.GrantUtilizationReport",
    "Grant Budget Line": "civic_erp.civic_operations.doctype.grant_budget_line.grant_budget_line.GrantBudgetLine",
    "Donor": "civic_erp.civic_operations.doctype.donor.donor.Donor",
    "Donation": "civic_erp.civic_operations.doctype.donation.donation.Donation",
    "Donation Receipt": "civic_erp.civic_operations.doctype.donation_receipt.donation_receipt.DonationReceipt",
    "Fundraising Campaign": "civic_erp.civic_operations.doctype.fundraising_campaign.fundraising_campaign.FundraisingCampaign",
    "Pledge": "civic_erp.civic_operations.doctype.pledge.pledge.Pledge",
    "FCRA Registration": "civic_erp.civic_operations.doctype.fcra_registration.fcra_registration.FCRARegistration",
    "Foreign Contribution": "civic_erp.civic_operations.doctype.foreign_contribution.foreign_contribution.ForeignContribution",
    "FCRA Utilization Entry": "civic_erp.civic_operations.doctype.fcra_utilization_entry.fcra_utilization_entry.FCRAUtilizationEntry",
    "FCRA Annual Return": "civic_erp.civic_operations.doctype.fcra_annual_return.fcra_annual_return.FCRAAnnualReturn",
    "FCRA Compliance Calendar": "civic_erp.civic_operations.doctype.fcra_compliance_calendar.fcra_compliance_calendar.FCRAComplianceCalendar",
    "CSR Project": "civic_erp.civic_operations.doctype.csr_project.csr_project.CSRProject",
    "CSR Utilization Report": "civic_erp.civic_operations.doctype.csr_utilization_report.csr_utilization_report.CSRUtilizationReport",
    "Program": "civic_erp.civic_operations.doctype.program.program.Program",
    "Beneficiary": "civic_erp.civic_operations.doctype.beneficiary.beneficiary.Beneficiary",
    "Beneficiary Enrollment": "civic_erp.civic_operations.doctype.beneficiary_enrollment.beneficiary_enrollment.BeneficiaryEnrollment",
    "Program Activity": "civic_erp.civic_operations.doctype.program_activity.program_activity.ProgramActivity",
    "Impact Report": "civic_erp.civic_operations.doctype.impact_report.impact_report.ImpactReport",
    "Volunteer": "civic_erp.civic_operations.doctype.volunteer.volunteer.Volunteer",
    "Volunteer Assignment": "civic_erp.civic_operations.doctype.volunteer_assignment.volunteer_assignment.VolunteerAssignment",
    "Volunteer Timesheet": "civic_erp.civic_operations.doctype.volunteer_timesheet.volunteer_timesheet.VolunteerTimesheet",
    "Tender": "civic_erp.civic_operations.doctype.tender.tender.Tender",
    "Vendor Empanelment": "civic_erp.civic_operations.doctype.vendor_empanelment.vendor_empanelment.VendorEmpanelment",
    "Procurement Request": "civic_erp.civic_operations.doctype.procurement_request.procurement_request.ProcurementRequest",
    "Utilization Certificate": "civic_erp.civic_operations.doctype.utilization_certificate.utilization_certificate.UtilizationCertificate",
    "Staff": "civic_erp.civic_operations.doctype.staff.staff.Staff",
    "Salary Cost Allocation": "civic_erp.civic_operations.doctype.salary_cost_allocation.salary_cost_allocation.SalaryCostAllocation",
    "Volunteer vs Staff Log": "civic_erp.civic_operations.doctype.volunteer_vs_staff_log.volunteer_vs_staff_log.VolunteerVsStaffLog",
    "Board Member": "civic_erp.civic_operations.doctype.board_member.board_member.BoardMember",
    "Board Meeting": "civic_erp.civic_operations.doctype.board_meeting.board_meeting.BoardMeeting",
    "Compliance Tracker": "civic_erp.civic_operations.doctype.compliance_tracker.compliance_tracker.ComplianceTracker",
}
