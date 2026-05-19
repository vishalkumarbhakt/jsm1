# JSM LMS (Full Stack)

This repository now contains a full-stack school/learning management scaffold with:

- **Frontend:** React + React Router + Redux Toolkit + Axios + Tailwind CSS + Framer Motion + React Hook Form + Chart.js
- **Backend:** Django + Django REST Framework
- **Auth:** JWT access/refresh tokens (SimpleJWT)
- **Roles:** `admin`, `teacher`, `student`

## Repository structure

- `/backend` Django API project
  - apps: `accounts`, `students`, `teachers`, `courses`, `attendance`, `assignments`, `quizzes`, `payments`, `notifications`
- `/frontend` React application
  - folders: `src/pages`, `src/components`, `src/layouts`, `src/services`, `src/redux`, `src/routes`
- `/jsm` preserved legacy static assets/site

## Backend setup

```bash
cd backend
python -m pip install -r requirements.txt
cp .env.example .env  # optional
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at: `http://127.0.0.1:8000`

### Backend env vars

- `DEBUG` (default: `True`)
- `SECRET_KEY`
- `ALLOWED_HOSTS` (comma-separated)
- `CORS_ALLOWED_ORIGINS` (comma-separated)
- `STRIPE_SECRET_KEY`
- `STRIPE_PUBLISHABLE_KEY`

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://127.0.0.1:5173`

Set API URL if needed:

```bash
# frontend/.env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

## Implemented API scaffolding

- Auth:
  - `POST /api/auth/register/`
  - `POST /api/auth/login/`
  - `POST /api/auth/logout/`
  - `POST /api/auth/token/refresh/`
  - `GET /api/auth/me/`
- Student:
  - notes/videos/quizzes listing
  - assignment submit
  - attendance/progress/notifications/payments listing
- Teacher:
  - upload note
  - create/manage assignments
  - mark attendance
  - create/manage quizzes
  - evaluate submissions
- Admin:
  - manage students/teachers/courses
  - analytics summary endpoint
- Payments:
  - Stripe payment intent preparation endpoint (`/api/payments/create-intent/`)

## Validation

- Backend: `python manage.py test accounts students`
- Frontend: `npm run build`

UI screenshot generated at: `/home/runner/work/jsm1/jsm1/frontend-home.png`
