# 代码生成时间: 2025-09-03 14:38:46
import gradio as gr
import random
# TODO: 优化性能

"""
# 添加错误处理
Random Number Generator using Gradio framework

This application generates a random number between two specified bounds.
It includes error handling to ensure the inputs are valid and the program is robust.
"""

# Define the function to generate a random number
def generate_random_number(min_value: int, max_value: int) -> int:
# 扩展功能模块
    """Generates a random number between min_value and max_value."""
    if min_value >= max_value:
        raise ValueError("Minimum value should be less than maximum value.")
    return random.randint(min_value, max_value)

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_random_number,
    inputs=[
        gr.Slider(minimum=0, maximum=100, default=0, label="Minimum Value"),
# FIXME: 处理边界情况
        gr.Slider(minimum=0, maximum=100, default=100, label="Maximum Value")
    ],
    outputs="number",
    title="Random Number Generator",
    description="Generate a random number between two specified bounds."
)

# Run the interface
iface.launch()