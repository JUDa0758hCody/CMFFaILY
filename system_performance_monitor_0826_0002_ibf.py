# 代码生成时间: 2025-08-26 00:02:54
import psutil
import gr
import time

"""
System Performance Monitor using GRADIO framework.
This tool provides real-time system performance data.
"""

# Function to calculate CPU usage
def get_cpu_usage():
    """
    Calculates and returns the CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)

# Function to calculate memory usage
def get_memory_usage():
    """
    Calculates and returns the memory usage percentage.
    """
    memory = psutil.virtual_memory()
    return memory.percent

# Function to calculate disk usage
def get_disk_usage():
    """
    Calculates and returns the disk usage percentage.
    """
    disk = psutil.disk_usage('/')
    return disk.percent

# Function to calculate network speed
def get_network_speed():
    """
    Calculates and returns the network speed in bytes per second.
    """
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Function to start the system performance monitor
def start_monitor():
    """
    Starts the system performance monitor and continuously updates the data.
    """
    with gr.Blocks() as demo:
        gr.Markdown("# System Performance Monitor")
        
        # CPU usage
        cpu_usage_label = gr.Textbox(label="CPU Usage (\%)")
        cpu_usage_graph = gr.Line(label="CPU Usage Over Time")
        
        # Memory usage
        memory_usage_label = gr.Textbox(label="Memory Usage (\%)")
        memory_usage_graph = gr.Line(label="Memory Usage Over Time")
        
        # Disk usage
        disk_usage_label = gr.Textbox(label="Disk Usage (\%)")
        disk_usage_graph = gr.Line(label="Disk Usage Over Time")
        
        # Network speed
        net_speed_label = gr.Textbox(label="Network Speed (bytes/s)")
        net_speed_graph = gr.Line(label="Network Speed Over Time")
        
        # Update function to refresh the data every second
        def update():
            try:
                cpu_usage = get_cpu_usage()
                memory_usage = get_memory_usage()
                disk_usage = get_disk_usage()
                net_speed = get_network_speed()

                cpu_usage_label.update(value=str(cpu_usage))
                memory_usage_label.update(value=str(memory_usage))
                disk_usage_label.update(value=str(disk_usage))
                net_speed_label.update(value=f"{net_speed[0]:,.2f}, {net_speed[1]:,.2f}")

                cpu_usage_graph.update([x for x in range(len(cpu_usage_graph.data), len(cpu_usage_graph.data) + 1)], [cpu_usage])
                memory_usage_graph.update([x for x in range(len(memory_usage_graph.data), len(memory_usage_graph.data) + 1)], [memory_usage])
                disk_usage_graph.update([x for x in range(len(disk_usage_graph.data), len(disk_usage_graph.data) + 1)], [disk_usage])
                net_speed_graph.update([x for x in range(len(net_speed_graph.data), len(net_speed_graph.data) + 1)], [net_speed[0] + net_speed[1]])
            except Exception as e:
                print(f"Error updating data: {e}")
        
        # Start the update function every second
        gr.Interval(update, 1000)

    demo.launch()

# Run the monitor
if __name__ == "__main__":
    start_monitor()