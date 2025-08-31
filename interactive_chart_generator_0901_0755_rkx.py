# 代码生成时间: 2025-09-01 07:55:37
import gradio as gr
import plotly.express as px
import pandas as pd
import numpy as np

# 交互式图表生成器类
class InteractiveChartGenerator:
    def __init__(self):
        # 初始化Gradio界面
        self.interface = gr.Interface(
            fn=self.generate_chart,
            inputs=[
                gr.Textbox(label="X轴数据"),
                gr.Textbox(label="Y轴数据"),
                gr.Dropdown(label="图表类型", choices=["line", "bar", "scatter"]),
            ],
            outputs="chart",
            title="交互式图表生成器",
        )

    def generate_chart(self, x_data, y_data, chart_type):
        # 解析输入数据
        try:
            x_values = np.fromstring(x_data, dtype=float, sep=",")
            y_values = np.fromstring(y_data, dtype=float, sep=",")
        except ValueError:
            return "输入数据格式错误，请使用逗号分隔的数值"

        # 创建数据帧
        df = pd.DataFrame({
            "X": x_values,
            "Y": y_values,
        })

        # 根据图表类型生成图表
        if chart_type == "line":
            chart = px.line(df, x="X", y="Y")
        elif chart_type == "bar":
            chart = px.bar(df, x="X", y="Y")
        elif chart_type == "scatter":
            chart = px.scatter(df, x="X", y="Y")
        else:
            return "未知的图表类型"

        # 返回图表
        return chart

# 创建交互式图表生成器实例并运行
generator = InteractiveChartGenerator()
generator.interface.launch()