** User Access Control (Python Example with Flask)

from flask import Flask, request

app = Flask(__name__)

# User roles and permissions dictionary
user_roles = {
    "admin": ["all"],
    "user": ["read_only"]
}

def has_permission(user, permission):
    return user_roles.get(user, []) in ["all", permission]

@app.route("/protected_resource")
def protected_resource():
    if has_permission(current_user, "access_resource"):
        return "Access granted!"
    else:
        return "Access denied!", 403

if __name__ == "__main__":
    app.run(debug=True)

** 2. User Access Control (Flask Example):
This code defines functions and routes for a Flask application.
The /protected_resource route checks if the current_user has the required permission (access_resource) using the has_permission function.
If the user has the permission:
The route returns "Access granted!"
If the user lacks the permission:
The route returns "Access denied!" with a status code of 403 (Forbidden).
