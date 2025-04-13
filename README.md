
#  Nuts Subscriber App

A 3-layered application built for the Software Engineering course. It subscribes to a local Nuts message bus, processes messages, and persists them in a PostgreSQL database.



##  Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Clone Repository](#1-clone-repository)
  - [2. Start PostgreSQL and Nuts using Docker Compose](#2-start-postgresql-and-nuts-using-docker-compose)
  - [3. Set up Database Schema](#3-set-up-database-schema)
  - [4. Run the Application](#4-run-the-application)
- [Tests (Bonus)](#tests-bonus)
- [Dependencies](#dependencies)
- [Notes](#notes)



##  Overview

This application performs the following:

- Subscribes to messages from a Nuts service (local message bus).
- Processes each incoming message.
- Persists processed data into a PostgreSQL database.
- Follows a clean 3-layer architecture for maintainability and separation of concerns.



##  Architecture

The project is divided into three main layers:

### 1. **API Layer**
- **Path:** `api/subscriber.py`
- Subscribes to the Nuts service and receives messages.
- Forwards messages to the service layer.

### 2. **Service Layer**
- **Path:** `service/processor.py`
- Handles business logic and validation.
- Sends clean data to the data layer.

### 3. **Data Layer**
- **Path:** `data/repository.py`
- Interacts with PostgreSQL database.
- Stores incoming messages in a `messages` table (content + timestamp).



##  Folder Structure

```bash
nuts-subscriber-app/
│
├── api/             
│   └── subscriber.py
│
├── service/          
│   └── processor.py
│
├── data/             
│   └── repository.py
│
├── db/              
│   └── schema.sql
│
├── tests/            
│   └── test_service.py
│   └── test_data.py
│
├── docker-compose.yml
├── publisher.py 
├── Dockerfile
├── main.py          
├── requirements.txt
└── README.md        
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/nuts-subscriber-app.git
cd nuts-subscriber-app
```



### 2. Start PostgreSQL and Nuts using Docker Compose

Make sure you have **Docker** and **Docker Compose** installed.

```bash
docker-compose up -d
```

This will start:
- PostgreSQL database
- Local Nuts service
- Your subscriber app container



### 3. Set up Database Schema

Once the PostgreSQL container is running, apply the schema:

```bash
docker exec -i <postgres_container_name> psql -U postgres -d messages_db < db/schema.sql
```

Replace `<postgres_container_name>` with the actual container name from `docker ps`.



### 4. Run the Application

If you're not using the Docker container for the app:

```bash
pip install -r requirements.txt
python main.py
```

This starts the app and begins listening for messages from Nuts.



##  Tests 

To run unit tests:

```bash
pytest tests/
```

Ensure test coverage includes:
- Message processing (service layer)
- Data persistence (data layer)



##  Dependencies

Key Python libraries used:

- `psycopg2` — PostgreSQL adapter
- `datetime` — Timestamp processing
- `pytest` — Testing framework


