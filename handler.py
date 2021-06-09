from watchdog.events import FileSystemEventHandler
from file_manager import File_Manager

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            file_manager = File_Manager()
            file_manager.file_manage()
