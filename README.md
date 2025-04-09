# SalonAI

**AI-Based Scheduling & Recommending App for Hair Salons**  
A project by Team 12 (Lassonde School of Engineering, York University)  
Last updated: February 7, 2025  

▶️ **[Watch the Demo](https://youtu.be/n8-DVjK4JD0)**  

---

## Table of Contents
- [SalonAI](#salonai)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [System Architecture](#system-architecture)
  - [Technology Stack](#technology-stack)
  - [Installation \& Setup](#installation--setup)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Project Structure](#project-structure)
  - [Team Organization](#team-organization)
  - [Appendix \& References](#appendix--references)

---

## Introduction
SalonAI is an AI-powered scheduling and recommendation platform designed to streamline hair salon operations. It automates booking, scheduling, and quoting processes, and it provides personalized hairstyle and color recommendations for clients. By integrating **Next.js 13** (using the new “App Router”) on the front end, the system supports better SEO and flexible rendering strategies (SSR or SSG) where needed.

---

## Features
1. **AI-Based Recommendations**  
   - Suggests personalized hairstyles and color options using an LLaMA model fine-tuned on client history.  
   - Logs recommendations for stylist review and future reference.

2. **Automated Scheduling & Booking**  
   - Allows clients to view availability, book appointments, and receive instant confirmations.  
   - Minimizes double bookings or scheduling conflicts.

3. **Salon Management Tools**  
   - Provides salon staff with a unified dashboard for appointments, staff schedules, and real-time updates.  
   - Handles quoting and pricing logic, role-based access, and analytics (optional).

4. **Multi-Platform Access**  
   - **Next.js (Web)**: Enables server-side rendering (SSR) or static site generation (SSG) for SEO-friendly, fast-loading pages.  
   - **React Native (Mobile)** (optional): iOS and Android apps for booking, notifications, and on-the-go operations.

---

## System Architecture
The application is designed in layered components for scalability and maintainability:

1. **Presentation Layer (Front-End)**
   - **Next.js (Web)**: Uses Next.js 13’s App Router, located in `next-app/app/`.
   - **React Native (Mobile)**: (Optional) for native mobile applications.

2. **Application Layer (Backend)**
   - **Flask** (with optional Flask-RESTX or Flask-Restful).  
   - Exposes REST endpoints for booking, user management, and style recommendation requests.

3. **AI Module**
   - **LLaMA model (7B or 13B)**, typically hosted on a local GPU server (e.g., 2×NVIDIA V100).  
   - Provides recommendation logic via internal REST or gRPC calls.  
   - Uses techniques like LoRA or QLoRA for efficient fine-tuning.

4. **Data Layer (Database)**
   - **PostgreSQL** (recommended) or MySQL for persistent data (appointments, user profiles, stylists, etc.).  
   - Optional **Redis cache** for quick data retrieval or repeated AI queries.

---

## Technology Stack
- **Backend**: Python 3, Flask (with optional Flask-RESTX, Flask-Restful, or SQLAlchemy)  
- **Front-End**: Next.js 13 (Node.js, TypeScript/JavaScript)  
- **Mobile (Optional)**: React Native (JavaScript/TypeScript)  
- **Database**: PostgreSQL (preferred) or MySQL  
- **AI**: LLaMA 7B or 13B model with GPU support  
- **Containerization/Orchestration**: Docker, docker-compose, optionally Kubernetes  
- **Version Control**: Git + GitHub / GitLab for branching and pull requests  
- **CI/CD**: GitHub Actions or similar for automated testing and builds  

---

## Installation & Setup

go to each respective folder for this. 



## Usage
1. **Client Workflow**  
   - Sign up or log in via the Next.js website (or optional mobile app).  
   - Browse available staff times and book an appointment.  
   - View AI-generated hairstyle or color recommendations, along with price quotes.

2. **Salon Staff / Admin Workflow**  
   - Access a centralized scheduling dashboard showing all appointments.  
   - Confirm or override AI suggestions for styles or color plans.  
   - Update service pricing, manage staff schedules, and run performance analytics.

3. **Notifications & Updates**  
   - Clients receive email or push notifications (if on mobile) when appointments are confirmed or changed.  
   - Staff can see real-time updates and new booking requests on their Next.js admin console or mobile app.

---

## Testing
1. **Unit Tests**  
   - Write Python tests for your Flask endpoints (you can use [`pytest`](https://docs.pytest.org/) or [`unittest`](https://docs.python.org/3/library/unittest.html)).  
   - For Next.js, use [Jest](https://jestjs.io/) or [Testing Library](https://testing-library.com/docs/react-testing-library/intro/) to test pages and components.
2. **Integration Tests**  
   - Evaluate end-to-end flows (booking, quoting, AI recommendations) across Flask and Next.js.
3. **Performance Tests**  
   - Check AI response times and concurrency for recommendations.  
   - Use [Locust](https://locust.io/) or JMeter if needed.
4. **User Acceptance Tests (UAT)**  
   - Simulate real-user scenarios with staging/demo data to validate the overall experience.

---

## Project Structure
A possible directory layout:

```
EECS-2311-FINAL-PROJECT-SALON-AI/
├─ Backend/
│  ├─ app.py           # Flask source code
│  ├─ requirements.txt
│  └─ venv/            # Virtual environment
├─ newAI/
│  ├─ modelCompoarison.ipynb     # AI microservice
│  ├─ weights/                   # Model weights (LLaMA)
│  └─ ...
├─ Frontend/           # Next.js 13 project
│  ├─ app/             # App Router files (page.tsx, layout.tsx, etc.)
│  ├─ public/
│  ├─ node_modules/
│  ├─ package.json
│  └─ ...
└─ README.md             
```

*(If using React Native, you might have a `mobile/` folder parallel to `next-app/`.)*

---

## Team Organization
look at corresponding ITR folders


## Appendix & References
- Refer to the [Group 8 Detailed Design & Implementation Plan]citeturn0file0 for full system architecture diagrams, data flow charts, and in-depth rationale behind each design choice.
- **Flask Documentation**:  
  [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **Next.js Documentation**:  
  [https://nextjs.org/docs](https://nextjs.org/docs)
- **React Native Documentation** (if using mobile):  
  [https://reactnative.dev/](https://reactnative.dev/)
- **LLaMA Model & LoRA Methods**:  
  Refer to open-source docs and huggingface.co guides.

For any questions, issues, or contributions, please open a GitHub issue or contact the team via our shared channels.

---

**End of README**
