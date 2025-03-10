# SalonAI Backend Setup Guide

This guide will walk you through setting up the backend portion of the SalonAI project using Git Bash on Windows.

## Prerequisites

- [Git Bash](https://gitforwindows.org/) installed  
- [Python 3.x](https://www.python.org/downloads/) installed and added to your PATH  
- A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account (free tier works)

## Getting Started

### 1. Clone the Repository

Open Git Bash and run:

```bash
git clone https://github.com/victobui/EECS-2311-Final-Project-Salon-AI.git
cd EECS-2311-Final-Project-Salon-AI
```

### 2. Navigate to the Backend Directory

```bash
cd Backend
```

### 3. Set Up MongoDb

Before running the backend, you need to configure your MongoDB Atlas cluster:

1. **Get the Connection String:**  
   - Your connection string should resemble:  
     ```
     mongodb+srv://VictoBuicaYorku:adrian@tempcluster.60vcy.mongodb.net/
     ```


### 4. Create and Activate the Virtual Environment

Create a virtual environment using Python:

```bash
python -m venv venv
```

Activate the virtual environment in Git Bash:

```bash
source venv/Scripts/activate
```

You should now see `(venv)` in your prompt, indicating the environment is active.

### 5. Install Dependencies

Upgrade pip and install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:**  
If you encounter an installation error for `dotenv`, run:  
```bash
pip install python-dotenv
```

### 6. Run the Flask Application

With the virtual environment activated, start the Flask server:

```bash
python run.py
```

The backend should now be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```
Backend/
├── api/
|   |──services
│       ├── __init__.py           # Flask app initialization
│       ├── models/               # Database models
│       ├── routes/               # API endpoints
│       └── services/             # Business logic
├── venv/                     # Virtual environment (created during setup)
├── .env                      # Environment variables
├── makefile                  # Build automation (Linux style)
├── requirements.txt          # Python dependencies
└── run.py                    # Application entry point
```

## Troubleshooting

- **Module Not Found Error:**  
  Ensure you have a `backend` directory with an `__init__.py` file and that you're running the script from the correct directory.

- **MongoDB Connection Issues:**  
  - Verify your credentials in the `.env` file.  
  - Make sure your IP address is whitelisted in MongoDB Atlas.  
  - Confirm that your MongoDB cluster is running and accessible.

- **Virtual Environment Activation Issues:**  
  If `source venv/Scripts/activate` doesn't work, try:
  ```bash
  . venv/Scripts/activate
  ```
  
- **Package Installation Errors:**  
  Install packages individually if needed:
  ```bash
  pip install flask flask-pymongo flask-bcrypt flask-jwt-extended python-dotenv certifi pymongo
  ```

## Next Steps

- Explore the API endpoints defined in the `backend/routes` folder.  
- Connect your frontend application to this backend.  
- Test the complete application workflow by navigating to your endpoints.

For any questions or issues during setup, please open a GitHub issue or contact the team.