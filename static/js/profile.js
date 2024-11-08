// Basic form validation for profile update
document.querySelector("form").addEventListener("submit", function(event) {
    var form = event.target;
    var username = form.querySelector("input[name='username']").value;
    var email = form.querySelector("input[name='email']").value;

    if (!username || !email) {
        alert("Please fill in all required fields.");
        event.preventDefault();  // Prevent submission if fields are empty
    }
});
