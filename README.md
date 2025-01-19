# Overview

This is a Task Manager, a Django project designed to manage tasks on our daily routine. This project is a part of Django Tutorial Class.

## Installation

0. Create a project directory and open it in your fav code editor and run the following commands in the terminal:

1. Clone the repository:

   ```bash
   git clone https://github.com/prakashtaz0091/Task-Manager---Django

   ```

2. Create and activate a virtual environment:

   - On Linux/macOS:

     ```bash
     pip install virtualenv
     virtualenv venv
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Technologies Used

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: Django Templates with Bootstrap CSS
