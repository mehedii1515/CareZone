Car Zone - Used Car Selling Website 🚗
A real-world Django project built to simulate a used car dealership business. This project follows a client-oriented development workflow and includes full-stack implementation using Django, PostgreSQL, Bootstrap, OAuth, and Heroku Deployment.

🌐 Live Demo
🔗 Visit Live Site (https://carzone-00ph.onrender.com/)

📎 GitHub Repository
🔗 https://github.com/mehedii1515/CareZone

📌 Features
✅ Real-world client-based project structure

✅ HTML5 & Bootstrap-based responsive frontend

✅ PostgreSQL database integration

✅ Fully customized Django admin panel

✅ RichText editor and multi-select fields in backend

✅ Browse, search, and filter cars

✅ Pagination for car listings

✅ User authentication system

✅ Social login: Google and Facebook

✅ Email sending functionality

✅ Database dump and load for local/remote servers

✅ Production deployment using render


🛠️ Tech Stack
Backend: Python, Django

Frontend: HTML5, Bootstrap 4

Database: PostgreSQL

Authentication: Django Allauth (for Google & Facebook Login)

Editor: CKEditor


📂 Project Setup
1. Clone Repository
bash
Copy
Edit
git clone https://github.com/mehedii1515/CareZone.git
cd CareZone
2. Setup Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Configure PostgreSQL and .env
Create a .env file with your database and secret keys:

ini
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_postgres_db_url
5. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
7. Collect Static Files
bash
Copy
Edit
python manage.py collectstatic
8. Run Server
bash
Copy
Edit
python manage.py runserver
🚀 Deployment
On Heroku
Use Gunicorn as WSGI HTTP Server

Use Whitenoise for serving static files

Add Procfile and runtime.txt

Deploy via GitHub integration or Heroku CLI

📸 Screenshots
Include images of:

Homepage

Car Listings

Admin Panel

Login with Google/Facebook

(You can upload images to your GitHub repo and link them here)


👨‍💻 Author
Md. Mehedi Hasan
Web Developer
GitHub Profile

🏷️ Tags
django python web development real project bootstrap heroku postgresql admin customization social login car dealership website
