## Development Setup

```bash
# Create venv and install flask
python -m venv venv
pip install -r requirements.txt

# Start postgresql and redis server
docker-compose up -d

```

- Access the service from `localhost:5000/<API>` (Check the available api from `server.py`)

