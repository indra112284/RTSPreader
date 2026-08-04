from rtsp_reader import run_rtsp_reader


def main():

    print("=" * 60)
    print("      RTSP CAMERA READER APPLICATION")
    print("=" * 60)

    try:
        run_rtsp_reader()

    except KeyboardInterrupt:
        print("\nApplication stopped by user.")


if __name__ == "__main__":
    main()