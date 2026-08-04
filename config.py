# ==========================================================
# RTSP Camera Reader Configuration
# ==========================================================

# RTSP Camera URL
RTSP_URL = "rtsp://host.docker.internal:8554/live"

# Delay before reconnecting (seconds)
RECONNECT_DELAY = 5

# Save snapshot every 30 seconds
SNAPSHOT_INTERVAL = 30

# Window title
WINDOW_NAME = "RTSP Camera Reader"

# Folder to store snapshots
SNAPSHOT_FOLDER = "snapshots"

# Log file path
LOG_FILE = "logs/app.log"