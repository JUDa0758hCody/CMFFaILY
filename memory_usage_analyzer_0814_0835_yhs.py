# 代码生成时间: 2025-08-14 08:35:53
import psutil
from gradio import Interface, outputs

"""
Memory Usage Analyzer using Gradio Framework

This script creates a GUI application that displays the memory usage of the system.
It utilizes the Gradio framework for creating the interface and psutil for gathering system memory information.
"""

# Function to get memory usage
def get_memory_usage():
    """
    Get the memory usage of the system.

    Returns:
        dict: A dictionary containing total memory, available memory, and used memory in bytes.
    """
    try:
        # Get memory information using psutil
        mem_info = psutil.virtual_memory()
        # Return a dictionary with memory information
        return {
            "total_memory": mem_info.total,
            "available_memory": mem_info.available,
            "used_memory": mem_info.used
        }
    except Exception as e:
        # Handle any exceptions that occur and return a message
        return {
            "error": f"An error occurred: {str(e)}"
        }

# Create a Gradio interface with a text output
iface = Interface(
    fn=get_memory_usage,
    outputs=outputs.JSON(label="Memory Usage"),
    title="Memory Usage Analyzer",
    description="Analyze the memory usage of your system."
)

# Run the interface
iface.launch()