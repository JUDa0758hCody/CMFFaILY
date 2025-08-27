# 代码生成时间: 2025-08-27 23:41:29
from gradio import Interface
import json

"""
API响应格式化工具

这个程序使用GRADIO框架创建一个界面，
用户可以输入一个API响应字符串，然后工具将其格式化为JSON。
# 增强安全性
"""

def format_json(input_json):
    """
    将输入的JSON字符串格式化为有效的JSON对象。
    
    参数:
    input_json (str): 要格式化的API响应字符串。
    
    返回:
    str: 格式化后的JSON字符串。
    """
    try:
        # 尝试解析输入的JSON字符串
# TODO: 优化性能
        parsed_json = json.loads(input_json)
        # 将解析后的JSON对象格式化为字符串
        formatted_json = json.dumps(parsed_json, indent=4)
        return formatted_json
# 改进用户体验
    except json.JSONDecodeError as e:
        # 如果输入的字符串不是有效的JSON，返回错误信息
        return f"Error: {e}"
# NOTE: 重要实现细节

# 创建GRADIO界面
iface = Interface(
# 改进用户体验
    fn=format_json,
    inputs="textarea",
    outputs="textarea",
    title="API响应格式化工具",
    description="输入API响应字符串，得到格式化后的JSON。",
)

# 启动GRADIO界面
# 增强安全性
iface.launch()