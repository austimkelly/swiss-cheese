import sqlite3

def create_and_populate_database():
    # Connect to the database (this will create it if it doesn't exist)
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # Create a users table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")

    # Insert some dummy data
    dummy_data = [("JohnDoe",), ("AliceSmith",), ("BobJohnson",)]
    cursor.executemany("INSERT INTO users (username) VALUES (?)", dummy_data)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

def safe_query(username):
    # Use a parameterized query to avoid SQL injection
    query = "SELECT * FROM users WHERE username = ?"

    # Connecting to the database
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # Executing the safe query with the username as a parameter
    cursor.execute(query, (username,))

    # Fetching the results
    results = cursor.fetchall()

    # Closing the database connection
    connection.close()

    return results

# Create and populate the database
create_and_populate_database()

# Test the safe query
user_input = input("Enter username: ")
result = safe_query(user_input)

# Display the results
print(result)

