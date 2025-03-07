QuickEase Backend Installation Guide

1. Install Python and pip
   For Linux/Mac (recommended)
   Install Python (version 3.11+ recommended)
   bash
   Copy
   Edit
   sudo apt update # For Ubuntu/Debian
   sudo apt install python3 python3-pip python3-venv
   Check installation:
   bash
   Copy
   Edit
   python3 --version
   pip3 --version
   For Windows (native installation, not WSL)
   Download Python from: https://www.python.org/downloads/
   During installation, make sure to check the box: ✅ Add Python to PATH
   After installation, check:
   bash
   Copy
   Edit
   python --version
   pip --version
2. Clone the Backend Code
   If you haven't already cloned your QuickEase backend repository, clone it into your working directory:

bash
Copy
Edit
git clone <repository-url>
cd <backend-folder> 3. Create and Activate Virtual Environment
This ensures you don’t install packages globally.

Create virtual environment (inside your project folder):

bash
Copy
Edit
python3 -m venv venv
Activate virtual environment:

Linux/macOS:
bash
Copy
Edit
source venv/bin/activate
Windows (PowerShell):
bash
Copy
Edit
.\venv\Scripts\Activate 4. Install Requirements from requirements/base.txt
After activating your virtual environment, install dependencies:

bash
Copy
Edit
pip install -r requirements/base.txt 5. Set Up .env File
Inside the backend project folder (where your manage.py is), create a file named .env if it doesn’t already exist.

Example content (adjust based on your actual variables):

ini
Copy
Edit
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/quickease_db
ALLOWED_HOSTS=localhost,127.0.0.1
Make sure this .env file matches what your settings expect (like if you’re using django-environ).

6. Apply Migrations
   Once the .env is ready, apply migrations to set up your database schema:

bash
Copy
Edit
python manage.py migrate 7. Run the Development Server
Finally, run the server to confirm setup works:

bash
Copy
Edit
python manage.py runserver
Open your browser at http://localhost:8000 to confirm the backend is running.

Optional (Check Installation Worked)
You can also check:

bash
Copy
Edit:w
python -m django --version
This confirms Django installed correctly.
