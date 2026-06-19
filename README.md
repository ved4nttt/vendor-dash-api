# Vendor Dash API
A containerized backend inventory management system for the "Vendor Dash" startup project.

## Tech Stack
- **Language:** Python (Flask)
- **Deployment:** Dockerized container
- **Infrastructure:** AWS EC2 (Mumbai Region)
- **CI/CD:** GitHub Actions (Automated deployment on push)

## API Endpoints
- `GET /` : Health check status.
- `GET /inventory` : Returns the current inventory in JSON format.
- `POST /inventory/add` : Adds a new item to the inventory (requires JSON payload).

## Live Demo
[http://13.235.104.68/inventory](http://13.235.104.68/inventory)
(http://13.235.104.68/)
