document.addEventListener("DOMContentLoaded", function() {
    var btn = document.getElementById("dropdownButton");
    var menu = document.getElementById("categoryMenu");
    var label = document.getElementById("selectedCategoryText");
    var checkboxes = menu.getElementsByTagName("input");

    // Open or close the menu when button is clicked
    btn.onclick = function() {
        if (menu.style.display === "block") {
            menu.style.display = "none";
        } else {
            menu.style.display = "block";
        }
    };

    // Update the text showing how many boxes are checked
    function updateCount() {
        var count = 0;
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                count = count + 1;
            }
        }

        if (count === 0) {
            label.textContent = "Select healthcare categories";
        } else if (count === 1) {
            label.textContent = "1 category selected";
        } else {
            label.textContent = count + " categories selected";
        }
    }

    // Run updateCount whenever any checkbox changes
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].onchange = updateCount;
    }

    // Select All button
    var selectAll = document.getElementById("selectAllButton");
    if (selectAll) {
        selectAll.onclick = function() {
            for (var i = 0; i < checkboxes.length; i++) {
                checkboxes[i].checked = true;
            }
            updateCount();
        };
    }

    // Clear All button
    var clearAll = document.getElementById("clearAllButton");
    if (clearAll) {
        clearAll.onclick = function() {
            for (var i = 0; i < checkboxes.length; i++) {
                checkboxes[i].checked = false;
            }
            updateCount();
        };
    }

    // Close the menu if user clicks outside of it
    window.onclick = function(event) {
        if (!btn.contains(event.target) && !menu.contains(event.target)) {
            menu.style.display = "none";
        }
    };

    updateCount();
});
