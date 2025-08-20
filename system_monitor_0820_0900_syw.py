# 代码生成时间: 2025-08-20 09:00:27
import psutil
import platform
import gr

"""
System Performance Monitor using Gradio and Python.
This tool allows users to monitor system performance metrics such as CPU usage, memory usage, and disk usage.
"""

class SystemMonitor:
    """Class to monitor system performance."""
    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0

    def get_cpu_usage(self):
        """Get the current CPU usage percentage."""
        try:
            self.cpu_usage = psutil.cpu_percent()
            return self.cpu_usage
        except Exception as e:
            print(f"Error fetching CPU usage: {e}")
            return None

    def get_memory_usage(self):
        """Get the current memory usage percentage."""
        try:
            memory = psutil.virtual_memory()
            self.memory_usage = memory.percent
            return self.memory_usage
        except Exception as e:
            print(f"Error fetching memory usage: {e}")
            return None

    def get_disk_usage(self):
        """Get the current disk usage percentage."""
        try:
            disk_usage = psutil.disk_usage('/')
            self.disk_usage = disk_usage.percent
            return self.disk_usage
        except Exception as e:
            print(f"Error fetching disk usage: {e}")
            return None

def main():
    """Main function to create a Gradio interface for the system monitor."""
    monitor = SystemMonitor()

    # Create Gradio interface
    iface = gr.Interface(
        fn=monitor.get_cpu_usage,
        inputs=[],
        outputs="number",
        title="CPU Usage Monitor",
        description="Monitor the CPU usage of your system."
    )

    iface.launch()

if __name__ == "__main__":
    main()