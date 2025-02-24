# Salon AI Wiki

## Home
Welcome to the **Salon AI** GitHub Wiki! This documentation provides an overview of the project, including features, architecture, development process, and contributions.

## Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [System Architecture](#system-architecture)
- [Iteration Plan](#iteration-plan)
- [User Stories](#user-stories)
- [Development Guidelines](#development-guidelines)
- [Testing & Deployment](#testing--deployment)
- [Contributions](#contributions)
  
---

## Project Overview
**Salon AI** is a smart salon management system designed to streamline appointment scheduling, service management, and payments through AI-powered recommendations. Users can book appointments, receive notifications, and interact with a modernized digital experience.

### Key Features
- ✅ **User Registration & Authentication**  
- ✅ **Appointment Booking & Management**  
- ✅ **Service Listings & Customization**  
- ✅ **Payment Processing** (Credit Card, Debit Card, Cash, Online)  
- ✅ **Notifications & Reminders**  
- ✅ **Staff Management & Role-Based Access**  

---

## Repository Structure
/SalonAI │── src/ # Source code directory │ ├── models/ # Business logic & domain models │ ├── services/ # Business logic service layer │ ├── database/ # Stub database (temporary storage) │ ├── gui/ # Graphical User Interface (GUI) │── test/ # Unit tests (JUnit) │── lib/ # External dependencies │── docs/ # Documentation & architecture sketches │── logs/ # Development logs & meeting notes │── README.md # Project overview │── LICENSE.md # Licensing information │── .gitignore # Ignored files list


---

## System Architecture
The system is composed of the following core components:

### Class Diagram
![Class Diagram](https://github.com/victobui/EECS-2311-Final-Project-Salon-AI/blob/master/Documentation/ITR1/Salon%20AI%20-%20Class%20Diagram.png)

### Component Overview
- **User Management** → Handles user authentication, registration, and profile updates.
- **Appointment Management** → Enables customers to book, reschedule, and cancel salon appointments.
- **Service Management** → Allows staff to add, edit, or remove services.
- **Payment Processing** → Supports multiple payment methods.
- **Notification System** → Sends automated reminders and updates.
- **Stub Database** → Temporary storage for testing (ArrayList-based).
- **GUI Module** → Provides a user-friendly interface.

---

## Iteration Plan
### Iteration 0 (ITR0)
- Define project requirements and user stories.
- Create system architecture and database schema.
- Design UI wireframes.

### Iteration 1 (ITR1)
- Implement domain-specific classes (**User, Appointment, Payment, Service**).
- Develop a stub database.
- Write unit tests using **JUnit**.
- Develop GUI for at least one major user story.
- Set up the **GitHub repository** with version control.
- Maintain a **log file** for development tasks and meetings.

---

## User Stories
| ID  | User Type | Description | Priority | Status |
|-----|----------|------------|----------|--------|
| US1 | Customer | Register and log in | High | In Progress |
| US2 | Customer | Schedule an appointment | High | In Progress |
| US3 | Customer | View appointment history | Medium | To Do |
| US4 | Staff    | Manage salon services | High | In Progress |
| US5 | Staff    | View scheduled appointments | Medium | To Do |
| US6 | System   | Send appointment reminders | High | In Progress |

---

## Development Guidelines
- **Coding Standards**: Follow consistent naming conventions and clean code practices.
- **Git Best Practices**:  
  - Use **feature branches** for new features.  
  - Commit frequently with meaningful messages.  
  - Avoid **large commits** close to the deadline.  
- **Testing**: Write **unit tests** for every major functionality.
- **Documentation**:  
  - Maintain the **Wiki** for project documentation.  
  - Update the **log file** (`logs/log.txt`) with development details.

---

## Testing & Deployment
- **Automated Unit Testing**: JUnit framework for business logic testing.
- **Manual GUI Testing**: Validate interface functionality.
- **Deployment Readiness**:  
  - Ensure the repository includes all necessary dependencies.  
  - The project should be **easily executable** (`Compile` and `Run`).

---

## Contributions
Each team member must:
- **Regularly contribute** to the repository.
- **Log all development activities** in `logs/log.txt`.
- **Follow GitHub best practices** (branching, pull requests, issue tracking).

---
