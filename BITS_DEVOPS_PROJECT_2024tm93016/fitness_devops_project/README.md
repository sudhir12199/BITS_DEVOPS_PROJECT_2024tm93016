# ACEest_Fitness DevOps Assignment

## Run locally
bash
pip install -r requirements.txt
flask --app wsgi:app run -p 8000

Run tests

pytest -q

Docker
docker build -t aceest_fitness .
docker run --rm -p 8000:8000 aceest_fitness

Endpoints
GET / → Welcome message
GET /health → Health check
POST /add_workout → Add workout ({"workout":"Running","duration":30})
GET /workouts → List all workouts

GitHub Actions
Runs on every push/PR
Builds Docker image
Runs Pytest inside Docker

Overview

This repository illustrates the practical use of essential DevOps concepts by creating a compact yet production-like project for ACEest_Fitness and Gym, a mock fitness startup. The key objective is to establish an efficient and automated workflow that guarantees code quality, uniformity across environments, and rapid delivery of updates.

The solution brings together Flask for application development, Git and GitHub for version control, Pytest for automated testing, Docker for containerization, and a CI/CD pipeline implemented with GitHub Actions. Completing this project highlights how DevOps methodologies streamline the way teams develop, validate, and release software.

Application Development

At the core of this project is a Flask-based web service. It delivers simple but representative features of a gym management system, including routes for a welcome page, system health check, adding workout records, and retrieving stored workouts.

Using Flask keeps the project lightweight and beginner-friendly while still reflecting real-world API practices. Unlike a desktop-based interface, this web design can be containerized, tested automatically, and integrated into continuous delivery pipelines — key elements of the DevOps toolkit.

Version Control System

The project is maintained using Git for version control. All artifacts — source code, unit tests, Dockerfile, and workflows — are tracked through commits. The repository is hosted on GitHub, providing collaboration, visibility, and automation through Actions. This ensures full traceability of changes and easy integration with CI/CD workflows, while keeping the repository public for evaluation.

Unit Testing with Pytest

Testing underpins reliability. The project uses Pytest to confirm expected behavior across all endpoints:

The index route ensures the application is up.

The health check route verifies service status.

The workout endpoints confirm workouts can be added and retrieved correctly.

Running tests locally is straightforward:

pytest -q


These automated checks safeguard the codebase, ensuring faulty changes are caught early before merging or deployment.

Containerization with Docker

Consistency across machines is achieved with Docker. The Dockerfile creates a minimal image using Python 3.11 slim, installs dependencies, and serves the app using Gunicorn.

Commands to build and run:

docker build -t aceest_fitness .
docker run --rm -p 8000:8000 aceest_fitness


This guarantees identical behavior in development, testing, and production.

CI/CD with GitHub Actions

Automation is handled by a GitHub Actions workflow (.github/workflows/ci.yml). The pipeline runs on every push or pull request and executes:

Checkout of the repository

Build of the Docker image

Execution of Pytest inside the container

Failures are reported immediately, enforcing quality gates and mirroring industry-standard CI/CD practices.

Documentation

This README serves as comprehensive documentation. It details project goals, installation instructions, testing commands, container usage, and the CI/CD workflow. Following it, users and evaluators can run the app locally, execute tests, or review automated pipeline runs on GitHub.

Conclusion

This project demonstrates a full DevOps pipeline: building a Flask app, managing it with GitHub, verifying it via Pytest, packaging it in Docker, and automating everything through GitHub Actions. Together, these practices enable faster, safer, and more dependable delivery of software — exactly what a startup like ACEest_Fitness and Gym would require to scale effectively.