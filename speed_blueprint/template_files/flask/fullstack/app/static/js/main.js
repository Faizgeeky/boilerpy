// Main JavaScript file for {{project_name}}

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.transition = 'opacity 0.5s';
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Processing...';
            }
        });
    });

    // Add active class to current nav link
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav a');
    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentLocation) {
            link.style.fontWeight = 'bold';
            link.style.textDecoration = 'underline';
        }
    });

    // Password strength indicator
    const passwordInput = document.querySelector('input[name="password"]');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            let strength = 0;

            if (password.length >= 8) strength++;
            if (password.match(/[a-z]+/)) strength++;
            if (password.match(/[A-Z]+/)) strength++;
            if (password.match(/[0-9]+/)) strength++;
            if (password.match(/[^a-zA-Z0-9]+/)) strength++;

            let indicator = this.parentElement.querySelector('.password-strength');
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.className = 'password-strength';
                indicator.style.marginTop = '0.5rem';
                indicator.style.fontSize = '0.875rem';
                this.parentElement.appendChild(indicator);
            }

            if (password.length === 0) {
                indicator.textContent = '';
            } else if (strength <= 2) {
                indicator.textContent = 'Weak password';
                indicator.style.color = '#dc3545';
            } else if (strength <= 4) {
                indicator.textContent = 'Medium password';
                indicator.style.color = '#ffc107';
            } else {
                indicator.textContent = 'Strong password';
                indicator.style.color = '#28a745';
            }
        });
    }

    // Confirm password match indicator
    const confirmPasswordInput = document.querySelector('input[name="confirm_password"]');
    if (confirmPasswordInput && passwordInput) {
        confirmPasswordInput.addEventListener('input', function() {
            let indicator = this.parentElement.querySelector('.password-match');
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.className = 'password-match';
                indicator.style.marginTop = '0.5rem';
                indicator.style.fontSize = '0.875rem';
                this.parentElement.appendChild(indicator);
            }

            if (this.value.length === 0) {
                indicator.textContent = '';
            } else if (this.value === passwordInput.value) {
                indicator.textContent = 'Passwords match';
                indicator.style.color = '#28a745';
            } else {
                indicator.textContent = 'Passwords do not match';
                indicator.style.color = '#dc3545';
            }
        });
    }
});

// Utility function for making AJAX requests
function fetchJSON(url, options = {}) {
    return fetch(url, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    });
}

// Example: Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;

    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(notification, container.firstChild);

        setTimeout(() => {
            notification.style.transition = 'opacity 0.5s';
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 500);
        }, 5000);
    }
}
