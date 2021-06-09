import time
from watchdog.observers import Observer
from os.path import dirname, abspath

from handler import Handler


class Watcher:
    dir_to_watch = dirname(dirname(abspath(__file__)))

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.dir_to_watch, recursive=False)
        self.observer.start()

        print("watching over : "+self.dir_to_watch)

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")
        
        self.observer.join()
