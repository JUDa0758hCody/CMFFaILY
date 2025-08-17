# 代码生成时间: 2025-08-17 18:40:43
import psutil
import gradio as gr

"""
A simple program to analyze memory usage using the GRADIO framework.
"""

# Define a function to get memory usage statistics
def get_memory_usage():
    """
    Retrieves the memory usage statistics from the system.
    Returns a dictionary containing the memory usage data.
    """
    try:
        # Get the memory usage statistics
        mem = psutil.virtual_memory()
        # Create a dictionary with the memory usage data
        memory_usage = {
            "total": mem.total / (1024 ** 3),  # Convert bytes to GB
            "available": mem.available / (1024 ** 3),  # Convert bytes to GB
            "used": mem.used / (1024 ** 3),  # Convert bytes to GB
            "percentage": mem.percent
        }
        return memory_usage
    except Exception as e:
        # Handle exceptions and return an error message
        return {"error": str(e)}

# Create a Gradio interface for the memory usage function
iface = gr.Interface(
    fn=get_memory_usage,
    inputs=[],  # No input required for this function
    outputs="json",  # Output will be in JSON format
    title="Memory Usage Analysis",
    description="Analyze your system's memory usage with this tool."
)

# Launch the Gradio interface
iface.launch()