# **<span style="color:red">_!! IMPORTANT NOTE !!_</span>**

**This API application is meant to be hosted in a DigitalOcean Droplet. Any and all the code run on a local machine will <span style="color:red">NOT</span> work. Please contact our developers at quickease.team@gmail.com for inquiries.**

**You are free to try and install the application but all unoperable features are beyond our scope of support.**

# QuickEase Backend - Installation Guide

Welcome to the **QuickEase Backend**! This guide will walk you through setting up the backend locally on your machine.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.11+**
- **pip** (comes with Python)
- **git** (to clone the repository)

---

## Step 1: Clone the Repository

Clone the QuickEase backend repository to your machine:

```bash
git clone <repository-url>
cd <backend-folder>
```

---

## Step 2: Install Python and pip (if not already installed)

### On Linux/Mac (recommended)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### On Windows (native installation)

- Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
- During installation, **check the box**: ✅ _Add Python to PATH_

Verify installation:

```bash
python --version
pip --version
```

---

## Step 3: Create and Activate a Virtual Environment

Create a virtual environment inside your project folder:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```bash
  .\venv\Scripts\Activate
  ```

---

## Step 4: Install Dependencies

With the virtual environment active, install all required packages:

```bash
pip install -r requirements/base.txt
```

---

## Step 5: Set Up the `.env` File

Create a file called `.env` in the same directory as `manage.py`, and add the required environment variables. Example:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/quickease_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

Modify the variables to match your local setup.

---

## Step 6: Apply Migrations

Run the following to apply database migrations:

```bash
python manage.py migrate
```

---

## Step 7: Run the Development Server

Start the backend server:

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to check if everything is working.

---

## Optional: Check Django Installation

To double-check everything installed correctly:

```bash
python -m django --version
```

---

## Need Help?

Email us at quickease.team@gmail.com
