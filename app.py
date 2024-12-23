import os
import sys
import time
from subprocess import Popen
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, restart_callback):
        super().__init__()
        self.restart_callback = restart_callback

    def on_modified(self, event):
        # Restart the app on any file modification
        if event.src_path.endswith(".py"):  # Monitor only Python files
            print(f"File changed: {event.src_path}")
            self.restart_callback()

def restart_flet_app():
    global process
    if process:
        print("Stopping Flet app...")
        process.terminate()
        process.wait()
    print("Starting Flet app...")
    process = Popen([sys.executable, "./Controllers/main.py"])  # Replace with your Flet app's filename

if __name__ == "__main__":
    # Initialize the app process
    process = None
    restart_flet_app()

    # Watch for file changes in the current directory
    path_to_watch = "."  # Adjust this to your project's directory
    event_handler = FileChangeHandler(restart_flet_app)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping watcher...")
        observer.stop()
        if process:
            process.terminate()
    observer.join()
