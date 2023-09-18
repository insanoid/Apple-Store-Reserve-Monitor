#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import os
import signal
import sys
import time

from store_checker import StoreChecker


def signal_handler(signal, frame):
    print(" - Stop Monitoring")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class Monitor:
    """A class to constantly monitor stock at periodic intervals."""

    POLLING_INTERVAL_SECONDS = 30

    def __init__(self):
        """Initializer."""
        print("Apple Store Monitoring \n")
        self.store_checker = StoreChecker()

    def start_monitoring(self):
        """Start monitoring store's stock."""
        while True:
            self.store_checker.refresh()
            time.sleep(300)


if __name__ == "__main__":
    monitor = Monitor()
    monitor.start_monitoring()
