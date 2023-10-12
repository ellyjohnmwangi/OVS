import http.cookies
import random
import os

# Initialize a dictionary to store session data
sessions = {}


# Function to generate a random session ID
def generate_session_id():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(32))


# Function to create a new session
def create_session():
    session_id = generate_session_id()
    sessions[session_id] = {}
    return session_id


# Function to retrieve session data
def get_session(session_id):
    return sessions.get(session_id, {})


# Function to set session data
def set_session(session_id, data):
    sessions[session_id] = data


# Example usage:

# Create a new session
session_id = create_session()

# Set session data
session_data = {'user_id': 123, 'username': 'john_doe'}
set_session(session_id, session_data)

# Retrieve session data
retrieved_data = get_session(session_id)
print(retrieved_data)
