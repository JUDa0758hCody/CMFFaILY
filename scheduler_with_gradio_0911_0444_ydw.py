# 代码生成时间: 2025-09-11 04:44:21
import gr
import asyncio
import threading
from datetime import datetime, timedelta
from typing import List, Callable, Dict

# Interval Scheduler
class IntervalScheduler:
    def __init__(self):
        """ Initialize the IntervalScheduler. """
        self.tasks: Dict[str, Dict] = {}
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def add_task(self, name: str, interval: int, callback: Callable) -> None:
        "