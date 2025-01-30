document.addEventListener("DOMContentLoaded", function() {
        // Select all expand links
        const expandLinks = document.querySelectorAll('[data-bs-toggle="collapse"]');

        expandLinks.forEach(function(link) {
            const targetId = link.getAttribute('data-bs-target');
            const targetElement = document.querySelector(targetId);

            // Detect when the collapse state changes
            targetElement.addEventListener('shown.bs.collapse', function () {
                // Change the link text to [Collapse] when expanded
                link.textContent = '[Collapse]';
            });

            targetElement.addEventListener('hidden.bs.collapse', function () {
                // Change the link text to [Expand] when collapsed
                link.textContent = '[Expand]';
            });
        });

        // ToolTips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

