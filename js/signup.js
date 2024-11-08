// Basic form validation for signup
document.querySelector("form").addEventListener("submit", function(event) {
    var form = event.target;
    var password = form.querySelector("input[name='password']").value;
    var confirmPassword = form.querySelector("input[name='confirmPassword']").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        event.preventDefault();  // Prevent submission if passwords don't match
    }
});
