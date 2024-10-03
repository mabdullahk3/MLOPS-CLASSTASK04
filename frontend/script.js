document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    fetch('http://127.0.0.1:5000/api/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, age }),
    })
    .then(response => response.json())
    .then(data => {
        alert("User added: " + JSON.stringify(data));
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
