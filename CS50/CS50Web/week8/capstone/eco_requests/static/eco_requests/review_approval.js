document.addEventListener("DOMContentLoaded", function () {
    const reqNumberFilter = document.getElementById("request-number-filter");
    const drawingFilter = document.getElementById("drawing-filter");
    const drawingStatusFilter = document.getElementById("drawing-status-filter");
    const reviewerFilter = document.getElementById("reviewer-filter");
    const approvalStatusFilter = document.getElementById("approval-status-filter");
    const tableRows = document.querySelectorAll("tbody tr");

    // Filter Table Rows by multiple fields
    function filterTable() {
        const reqNumberValue = reqNumberFilter.value.toLowerCase();
        const drawingValue = drawingFilter.value.toLowerCase();
        const drawingStatusValue = drawingStatusFilter.value;
        const reviewerValue = reviewerFilter.value;
        const approvalStatusValue = approvalStatusFilter.value;

        tableRows.forEach(row => {
            // Get cell values for each row (text content for Req. # and Drawing, select value for status, reviewer, and approval)
            const reqNumberCell = row.cells[0].textContent.toLowerCase();
            const drawingCell = row.cells[1].textContent.toLowerCase();

            // Get the selected value from the dropdowns in the table row
            const drawingStatusCell = row.querySelector('select[name="drawing_status"]').value;
            const reviewerCell = row.querySelector('select[name="reviewer_id"]').options[row.querySelector('select[name="reviewer_id"]').selectedIndex].text;
            const approvalStatusCell = row.querySelector('select[name="approval_status"]').value;

            // Match filter criteria
            const matchesReqNumber = reqNumberCell.includes(reqNumberValue);
            const matchesDrawing = drawingCell.includes(drawingValue);
            const matchesDrawingStatus = drawingStatusCell.includes(drawingStatusValue);
            const matchesReviewer = reviewerCell.includes(reviewerValue);
            const matchesApprovalStatus = approvalStatusCell.includes(approvalStatusValue);

            // Show or hide the row based on matches
            row.style.display = (matchesReqNumber && matchesDrawing && matchesDrawingStatus && matchesReviewer && matchesApprovalStatus) ? "" : "none";
        });
    }

    // Event Listeners for filters
    reqNumberFilter.addEventListener("input", filterTable);
    drawingFilter.addEventListener("input", filterTable);
    drawingStatusFilter.addEventListener("change", filterTable);
    reviewerFilter.addEventListener("change", filterTable);
    approvalStatusFilter.addEventListener("change", filterTable);
});
