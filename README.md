# CollegeSaathi 🎓

**AI-powered college admission tracker for first-generation students in India.**

Track admissions, compare 500+ colleges, never miss a deadline. Built with ❤️ for students who don't have anyone to guide them.

## Features

- **🔍 Browse Colleges** — Filter by state, stream, course level, college type, fees, and entrance exams
- **🎯 Smart Recommendations** — Monzy-style questionnaire that recommends 50-100 best colleges based on your preferences
- **⚡ Deadline Tracking** — See which applications are open, closing soon, or upcoming
- **❤️ Wishlist** — Save colleges (requires free account)
- **📱 Responsive** — Works on mobile, tablet, and desktop
- **🔐 Auth** — Google OAuth, Email, or Phone login
- **📄 Official Notifications** — Download links for admission notifications

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, React, Tailwind CSS, Zustand, Framer Motion |
| Backend | FastAPI (Python), SQLAlchemy, Pydantic |
| Database | PostgreSQL |
| Auth | JWT + Google OAuth |
| Deployment | Vercel (frontend) + Railway (backend) |

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.10+
- PostgreSQL 14+

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Setup database
# Create a PostgreSQL database called 'faraway'
# Copy .env.example to .env and update DATABASE_URL

# Run migrations & seed data
python -m app.seed_data

# Start server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Visit `http://localhost:3000`

### Environment Variables

Backend (`.env`):
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/faraway
SECRET_KEY=your-random-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
FRONTEND_URL=http://localhost:3000
```

## Deployment

Per the hosting plan: **Vercel** (frontend + admin UI), **Render or Railway** (backend), **Neon or Supabase** (PostgreSQL).

> **Note:** Local dev defaults to SQLite. Production must use PostgreSQL — set `DATABASE_URL` to your Neon/Supabase connection string.

### 1. Database → Neon or Supabase (PostgreSQL)

1. Create a free PostgreSQL project on [neon.tech](https://neon.tech) or [supabase.com](https://supabase.com)
2. Copy the connection string (use the **pooled** URL on serverless if offered)
3. Set `DATABASE_URL` in your backend env vars

Seed the database once (from Render/Railway shell or locally pointing at prod DB):

```bash
cd backend
python -m app.seed_data
```

### 2. Backend → Render or Railway

**Render** (uses `render.yaml` in repo root):

1. Connect GitHub repo at [render.com](https://render.com)
2. Create a **Web Service** with root directory `backend`
3. Set environment variables from `backend/.env.example`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Set `FRONTEND_URL` to your Vercel URL (e.g. `https://collegesathi.vercel.app`)

**Railway** alternative: deploy `backend` folder, same env vars and start command.

### 3. Frontend + Admin → Vercel

The admin panel is a Next.js route at `/admin` — it deploys **with the frontend**, not separately.

1. Import repo at [vercel.com](https://vercel.com)
2. Set **Root Directory** to `frontend`
3. Add environment variable:
   - `BACKEND_URL` = your Render/Railway API URL (e.g. `https://collegesathi-api.onrender.com`)
4. Deploy

Visit `https://your-app.vercel.app/admin` for the admin dashboard (email + password + OTP).

### Environment checklist

| Variable | Where | Purpose |
|----------|-------|---------|
| `DATABASE_URL` | Backend | PostgreSQL (Neon/Supabase) |
| `SECRET_KEY` | Backend | JWT signing |
| `FRONTEND_URL` | Backend | CORS (your Vercel URL) |
| `BACKEND_URL` | Vercel | API proxy target |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Backend | Admin login |
| `SMTP_PASSWORD` | Backend | Admin OTP emails |

## Data

The seed script populates the database with:
- **500+** real and realistic Indian colleges (IITs, NITs, IIMs, AIIMS, DU colleges, state universities, private universities)
- **60+** courses across UG, PG, PhD
- **32** entrance exams (JEE, NEET, CUET, CAT, CLAT, etc.)
- Cutoff data, admission rounds, fees, and deadlines

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/colleges` | GET | List colleges with filters & pagination |
| `/api/colleges/{id}` | GET | College details |
| `/api/colleges/filters/options` | GET | Available filter values |
| `/api/recommend` | POST | Get recommendations based on questionnaire |
| `/api/auth/register` | POST | Create account |
| `/api/auth/login` | POST | Login |
| `/api/auth/google` | POST | Google OAuth |
| `/api/wishlist` | GET | Get wishlisted colleges |
| `/api/wishlist/toggle` | POST | Add/remove from wishlist |
| `/api/wishlist/ids` | GET | Get wishlist college IDs |

## Future Scope

- [ ] Real-time deadline scraper (DU, Mumbai Univ, JOSAA, NSP)
- [ ] Push notifications for deadline reminders
- [ ] AI-powered SOP writer
- [ ] Multilingual support (Hindi, Tamil, Bengali, Marathi)
- [ ] Voice notes for guidance
- [ ] College comparison tool
- [ ] Scholarship database
- [ ] Aadhaar-based form pre-fill
- [ ] WhatsApp bot integration

## License

MIT
