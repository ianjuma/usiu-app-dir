import sys
import time
import logging
import files
import dirs
from dirs import software_folders

dir = '.'
populate = []

# event handler
# fs events + handlers
# add file/dir
# remove file/dir
# dir snapshots

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils import dirsnapshot


from watchdog.events import FileSystemEvent
file_created = FileSystemEvent(
    event_type='on_created', src_path=dir, is_directory=False)

file_deleted = FileSystemEvent(
    event_type='on_deleted', src_path=dir, is_directory=False)

folder_created = FileSystemEvent(
    event_type='on_created', src_path=dir, is_directory=True)

folder_deleted = FileSystemEvent(
    event_type='on_deleted', src_path=dir, is_directory=True)

all_events = FileSystemEvent(
    event_type='on_any_event', src_path=dir, is_directory=True)


# daemonise the observer
# on event x call

def refreshDir(populate):
    dirsnapshot.DirectorySnapshot(path=dir, recursive=True,
                                  walker_callback=dirs.getDirs(populate))
    event_handler = dirs.getDirs(populate)
    observer = Observer()
    observer.schedule(event_handler, dir, recursive=True)
    observer.setName('dir-observer')
    observer.start()
    # daemonize
    observer.join()


"""
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else dir
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
"""

if __name__ == "__main__":
    refreshDir(populate)
