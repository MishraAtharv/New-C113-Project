import os, shutil, sys, time, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/infos/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey there! {event.src_path} has been created")
    def on_deleted(self, event):
        print(f"Hey there! {event.src_path} has been deleted")
    def on_modified(self, event):
        print(f"Hey there! {event.src_path} has been modified, please verify if it was you")
    def on_moved(self, event):
        print(f"Hey there! {event.src_path} has been moved to {event.dest_patt}, please verify if it was you")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()







