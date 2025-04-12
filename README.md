# Nuts Subscriber App

##  Project Description
A 3-layered app that listens to a message bus (Nuts), processes messages, and stores them in PostgreSQL.

##  Architecture
- **API Layer** — Subscribes to Nuts and forwards messages.
- **Service Layer** — Validates and processes the message.
- **Data Layer** — Persists data into PostgreSQL.

##  How to Run

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/nuts-subscriber-app.git
cd nuts-subscriber-app
