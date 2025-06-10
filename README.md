# 🐳 Coderco Containers Challenge - Dockerized Solution

**A Flask web application with Redis visitor counter, containerized with Docker and Nginx**

## 📝 Project Overview
This project containerizes a Flask web application that:
- Displays a welcome page at `/`
- Shows a Redis-powered visitor counter at `/count`
- Uses Nginx as a reverse proxy

*Note: The original application was created by Coderco for their containers challenge - my contribution was containerizing it and adding persistence.*

## 🛠️ Technical Stack
- **Web Framework**: Flask (Python)
- **Database**: Redis (for visit counter persistence)
- **Web Server**: Nginx (reverse proxy)
- **Containerization**: Docker + Docker Compose

## 📂 File Structure# Docker Learning

/
├── app.py # Flask application
├── Dockerfile # Flask container configuration
├── docker-compose.yml # Orchestrates all services
└── nginx.conf # Nginx reverse proxy config


## 🚀 Quick Start

### Prerequisites
- Docker installed
- Docker Compose installed

### Installation
1. Clone this repository
2. Navigate to the project directory

### Running the Application
```bash
docker-compose up --build

Accessing the Application
Welcome page: http://localhost:5004

Visitor counter: http://localhost:5004/count

🔧 Key Implementation Details
Containerization
Dockerized the Flask app with Python 3.8-slim base image

Configured Redis as a separate service

Set up Nginx as reverse proxy with custom configuration

Persistence Features
Redis container maintains visitor count between restarts

Proper volume management for data persistence

Network Architecture
Flask app runs internally on port 5000

Nginx exposes the app externally on port 5004

Services communicate through Docker's internal network

⚠️ Troubleshooting
Common issues and solutions:

Port conflicts:

Ensure port 5004 is available

Change the port in docker-compose.yml if needed

Build failures:

Run docker-compose build --no-cache to rebuild from scratch

Redis connection issues:

Verify the Redis service is running in Docker

Check the Flask app's Redis connection settings

📚 Learning Outcomes
Through this project, I learned:

Docker containerization best practices

Multi-service Docker Compose configurations

Redis integration for persistent data

Nginx reverse proxy setup

Docker networking concepts