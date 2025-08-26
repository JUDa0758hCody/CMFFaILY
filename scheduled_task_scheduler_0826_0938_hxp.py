# 代码生成时间: 2025-08-26 09:38:27
import gradio as gr
import schedule
import time
from threading import Thread

"""
A simple Python script to demonstrate a scheduled task scheduler using Gradio and schedule library.
This program allows users to set up tasks that will be executed at specified times.
"""

class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, schedule_str, task_func):
        """
        Add a task to the scheduler.
        :param name: Name of the task
        :param schedule_str: Schedule string in the format 'seconds hours minutes'
        :param task_func: Function to be executed as the task
        """
        schedule.every(schedule_str).do(task_func)
        self.tasks[name] = schedule_str

    def run(self):
        """
        Run the scheduler in a separate thread to avoid blocking.
        """
        Thread(target=schedule.every().run_all).start()

    def display_tasks(self):
        """
        Display the list of scheduled tasks.
        :return: List of tasks
        """
        return self.tasks

    def clear_tasks(self):
        "