document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('register-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('register-username').value;
        const password = document.getElementById('register-password').value;
        registerUser(username, password);
    });

    document.getElementById('login-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('login-username').value;
        const password = document.getElementById('login-password').value;
        loginUser(username, password);
    });
});

function registerUser(username, password) {
    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username, password})
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('message').textContent = 'Registration successful';
        } else {
            throw new Error('Registration failed');
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = error.message;
    });
}

function loginUser(username, password) {
    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username, password})
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('message').textContent = 'Login successful';
        } else {
            throw new Error('Login failed');
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = error.message;
    });
}
