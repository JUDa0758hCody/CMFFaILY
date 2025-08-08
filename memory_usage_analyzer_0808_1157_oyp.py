# 代码生成时间: 2025-08-08 11:57:20
import psutil
import gradio as gr


def analyze_memory_usage():
    '''
    This function analyzes the current memory usage of the system.
    It calculates the percentage of memory used and provides a brief
    overview of the memory consumption.
    '''
    try:
        # Get the memory usage stats
        mem = psutil.virtual_memory()
        
        # Calculate memory usage percentage
        used_memory_percent = mem.percent
        
        # Prepare memory usage report
        memory_report = f"Total Memory: {mem.total / (1024 * 1024):.2f} MB
"
                 f"Available Memory: {mem.available / (1024 * 1024):.2f} MB
"
                 f"Used Memory: {mem.used / (1024 * 1024):.2f} MB
"
"
                 f"Memory Usage Percentage: {used_memory_percent}%"
        
        return memory_report
    except Exception as e:
        # Handle any exceptions that occur during memory analysis
        return f"Error analyzing memory usage: {str(e)}"

# Create a Gradio interface for the memory usage analyzer
iface = gr.Interface(
    fn=analyze_memory_usage,
    inputs=[],
    outputs="text",
    title="Memory Usage Analyzer",
    description="This app analyzes the current memory usage of your system."
)

if __name__ == "__main__":
    iface.launch()