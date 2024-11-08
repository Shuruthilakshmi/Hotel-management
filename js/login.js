// Basic form validation for login
document.querySelector("form").addEventListener("submit", function(event) {
    var form = event.target;
    var username = form.querySelector("input[name='username']").value;
    var password = form.querySelector("input[name='password']").value;

    if (!username || !password) {
        alert("Please fill in both username and password.");
        event.preventDefault();  // Prevent submission if empty
    }
});
