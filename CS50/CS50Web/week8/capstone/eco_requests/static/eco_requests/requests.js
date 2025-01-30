document.addEventListener("DOMContentLoaded", function () {
    const statusFilter = document.getElementById("status-filter");
    const requestNumberFilter = document.getElementById("request-number-filter");
    const tableRows = document.querySelectorAll("tbody tr");

    function filterTable() {
        const statusValue = statusFilter.value.toLowerCase();
        const requestNumberValue = requestNumberFilter.value.toLowerCase();

        tableRows.forEach(row => {
            const statusText = row.cells[6].textContent.trim().toLowerCase(); // Status is the 7th column (0-indexed)
            const requestNumberText = row.cells[0].textContent.trim().toLowerCase(); // Req.# is the 1st column

            // Check if row matches both filters
            const matchesStatus = !statusValue || statusText === statusValue;
            const matchesRequestNumber = !requestNumberValue || requestNumberText.includes(requestNumberValue);

             // Show or hide rows based on matches
            if (matchesStatus && matchesRequestNumber) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    }

    statusFilter.addEventListener("change", filterTable);
    requestNumberFilter.addEventListener("input", filterTable);
});

