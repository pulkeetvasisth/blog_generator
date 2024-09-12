// index.js
document.querySelector("form").addEventListener("submit", function(event) {
    var prompt = document.getElementById("prompt").value;
    if (prompt.length < 5) {
        alert("Blog topic must be at least 5 characters long.");
        event.preventDefault();
    }
});

