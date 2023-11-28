from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dummy data representing a list of users
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Route to get user details by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to update user details by ID (Vulnerable to IDOR)
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    # In a real application, proper authentication and authorization checks should be performed here

    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

# Route for the root URL ("/") to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
