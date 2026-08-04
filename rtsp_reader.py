import cv2
import os
import time

from config import (
    RTSP_URL,
    RECONNECT_DELAY,
    SNAPSHOT_INTERVAL,
    WINDOW_NAME,
    SNAPSHOT_FOLDER
)

from logger import logger


def connect_camera():
    """
    Connect to the RTSP camera.
    If the camera is unavailable, keep retrying.
    """

    while True:

        logger.info(f"Trying to connect to {RTSP_URL}")
        print("Trying to connect to RTSP Camera...")

        cap = cv2.VideoCapture(RTSP_URL)

        if cap.isOpened():

            logger.info("Connected Successfully")
            print("Connected Successfully")

            return cap

        logger.error("Unable to connect.")
        print("Unable to connect.")

        logger.info(f"Retrying after {RECONNECT_DELAY} seconds...")

        time.sleep(RECONNECT_DELAY)


def save_snapshot(frame):

    filename = os.path.join(
        SNAPSHOT_FOLDER,
        f"snapshot_{int(time.time())}.jpg"
    )

    cv2.imwrite(filename, frame)

    logger.info(f"Snapshot Saved : {filename}")

    print(f"Snapshot Saved : {filename}")


def run_rtsp_reader():

    logger.info("RTSP Reader Started")

    os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)

    cap = connect_camera()

    previous_time = time.time()

    last_snapshot = time.time()

    frame_count = 0

    reconnect_count = 0

    while True:
        try:

            ret, frame = cap.read()

            if not ret:

                logger.warning("Frame not received from RTSP stream.")
                print("Frame not received.")

                reconnect_count += 1

                cap.release()

                logger.info("Trying to reconnect...")

                time.sleep(RECONNECT_DELAY)

                cap = connect_camera()

                continue

            frame_count += 1

            current_time = time.time()

            fps = 1 / (current_time - previous_time)

            previous_time = current_time

            cv2.putText(
                frame,
                f"FPS : {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Frames : {frame_count}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                f"Reconnects : {reconnect_count}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            # ------------------------------------------
            # Save Snapshot Every 30 Seconds
            # ------------------------------------------

            if current_time - last_snapshot >= SNAPSHOT_INTERVAL:

                save_snapshot(frame)

                last_snapshot = current_time

            # ------------------------------------------
            # Display Video
            # ------------------------------------------

            cv2.imshow(WINDOW_NAME, frame)

            # ------------------------------------------
            # Exit Application
            # ------------------------------------------

            if cv2.waitKey(1) & 0xFF == ord("q"):

                logger.info("Application Closed by User")

                print("Application Closed")

                break

        except Exception as e:

            logger.exception(f"Unexpected Error: {e}")

            print(f"Unexpected Error: {e}")

            reconnect_count += 1

            cap.release()

            logger.info("Trying to reconnect after exception...")

            time.sleep(RECONNECT_DELAY)

            cap = connect_camera()

    # ------------------------------------------
    # Cleanup
    # ------------------------------------------

    cap.release()

    cv2.destroyAllWindows()