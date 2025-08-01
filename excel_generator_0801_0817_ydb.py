# 代码生成时间: 2025-08-01 08:17:41
import gradio as gr
def generate_excel(data):
    # 尝试生成Excel文件
    try:
        import pandas as pd
        df = pd.DataFrame(data)
        excel_file = "output.xlsx"
        df.to_excel(excel_file, index=False)
        return excel_file
    except Exception as e:
        return str(e)

# Gradio界面设置
iface = gr.Interface(
    fn=generate_excel,
    inputs=gr.DataFrame(label="Input Data"),
    outputs="file",
    title="Excel Table Generator",
    description="A tool to generate Excel tables from provided data.",
)

# 启动界面
iface.launch()