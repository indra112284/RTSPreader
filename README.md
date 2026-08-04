# RTSP Camera Reader

## Project Overview

This project is a Production-Ready RTSP Camera Reader developed using Python and OpenCV.

The application connects to an RTSP camera stream, displays the live video, automatically reconnects if the connection is lost, saves snapshots every 30 seconds, logs application events, and can be containerized using Docker.

---

## Features

- Connects to an RTSP camera stream
- Displays live video using OpenCV
- Calculates and displays FPS
- Automatically reconnects if the stream is lost
- Saves snapshots every 30 seconds
- Creates application logs
- Docker support using Dockerfile and Docker Compose
- Simple and modular project structure

---

## Project Structure

```
RTSPReader/
│
├── config.py
├── logger.py
├── main.py
├── rtsp_reader.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── .dockerignore
├── README.md
│
├── logs/
│   └── app.log
│
└── snapshots/
```

---

## Technologies Used

- Python 3
- OpenCV
- Docker
- Docker Compose
- RTSP
- Git
- GitHub

---

## Installation

Clone the repository.

```bash
git clone https://github.com/indra112284/RTSPreader.git
```

Move into the project folder.

```bash
cd RTSPreader
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Configuration

Open `config.py`.

Replace the RTSP URL with your camera URL.

```python
RTSP_URL = "rtsp://your_camera_url"
```

---

## Run the Application

```bash
python main.py
```

---

## Docker

Build the Docker image.

```bash
docker build -t rtsp-reader .
```

Run the Docker container.

```bash
docker-compose up
```

---

## Logging

Application logs are stored inside:

```
logs/app.log
```

---

## Snapshots

Snapshots are automatically saved every 30 seconds inside:

```
snapshots/
```

---

## Reconnection Logic

If the RTSP connection is interrupted:

- The application detects the failure.
- Waits for the configured reconnect delay.
- Attempts to reconnect automatically.
- Continues streaming once the RTSP stream becomes available.

---

## Author

**Indra Sena Chittiboina**

