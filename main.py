import os, sys
from daemonize import Daemonize

from watcher import Watcher


def main():
    watcher = Watcher();
    watcher.run();


if __name__ == '__main__':
        myname=os.path.basename(sys.argv[0])
        pidfile='/tmp/%s' % myname       # any name
        daemon = Daemonize(app=myname,pid=pidfile, action=main)
        daemon.start()