Before running the Flask application, create a file named .env in the backend directory with the following content:

# Credentials for Flask Application

# JWT Secret Key (used to sign and verify JSON Web Tokens)
JWT_SECRET_KEY=example_secret

# MongoDB Credentials
# Replace these placeholders with your actual MongoDB credentials
MONGO_USERNAME=your_example_username
MONGO_PASSWORD=your_example_password
MONGO_CLUSTER=your_cluster_url