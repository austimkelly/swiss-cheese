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

def vulnerable_query(username):
    # Vulnerable code with improperly escaped user input
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    # Connecting to the database
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # Executing the vulnerable query
    cursor.execute(query)

    # Fetching the results
    results = cursor.fetchall()

    # Closing the database connection
    connection.close()

    return results

# Create and populate the database
create_and_populate_database()

# Test the vulnerable query
user_input = input("Enter username: ") # Enter:  ' OR '1'='1' -- 
result = vulnerable_query(user_input)

# Display the results
print(result)
