document.addEventListener("DOMContentLoaded", function () {
    const statusFilter = document.getElementById("status-filter");
    const assignedFilter = document.getElementById("assigned-filter");
    const tableRows = document.querySelectorAll("tbody tr");
    const sortButton = document.getElementById("sort-req-number");

    let sortAscending = true;

    // Sort Table Rows by Request #
    function sortTable() {
        const rowsArray = Array.from(tableRows);
        rowsArray.sort((a, b) => {
            const reqA = parseInt(a.cells[0].textContent.trim(), 10);
            const reqB = parseInt(b.cells[0].textContent.trim(), 10);
            return sortAscending ? reqA - reqB : reqB - reqA;  // Compare as numbers
        });

        const tbody = document.querySelector("tbody");
        tbody.innerHTML = ""; // Clear current rows
        rowsArray.forEach(row => tbody.appendChild(row)); // Append sorted rows

        sortAscending = !sortAscending; // Toggle sorting direction
    }

    // Filter Table Rows by Status and Assigned
    function filterTable() {
        // console.log("Filtering table...");
        const statusValue = statusFilter.value;
        const assignedValue = assignedFilter.value.toLowerCase();

        tableRows.forEach(row => {

              // Get selected values from dropdowns inside the row
            const statusDropdown = row.querySelector('select[name="status"]');
            const assignedDropdown = row.querySelector('select[name="engineer_id"]');


            const statusText = statusDropdown ? statusDropdown.value : "";
            const assignedText = assignedDropdown
                ? assignedDropdown.options[assignedDropdown.selectedIndex].text.toLowerCase()
                : "";

            const matchesStatus = !statusValue || statusText === statusValue;
            const matchesAssigned = !assignedValue || assignedText.includes(assignedValue);

            row.style.display = matchesStatus && matchesAssigned ? "" : "none";
        });
    }

    // Event Listeners
    sortButton.addEventListener("click", sortTable);
    statusFilter.addEventListener("change", filterTable);
    assignedFilter.addEventListener("input", filterTable);
});
