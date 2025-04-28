class ScreenRecorder:
    @staticmethod
    def start_recording(driver):
        driver.start_recording_screen()

    @staticmethod
    def stop_and_save_recording(driver, file_path="test_recording.mp4"):
        raw_data = driver.stop_recording_screen()
        with open(file_path, "wb") as f:
            import base64
            f.write(base64.b64decode(raw_data))
