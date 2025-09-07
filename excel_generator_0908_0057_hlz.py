# 代码生成时间: 2025-09-08 00:57:55
import gradio as gr
def generate_excel(columns, rows, data):
    """
    Generate an Excel file based on the provided columns, rows, and data.
    Args:
        columns (list): List of column headers.
        rows (int): Number of rows to be generated.
        data (list of lists): Data to fill in the Excel file.
    Returns:
        str: The file path to the generated Excel file.
    Raises:
        ValueError: If invalid input is provided.
    """
    import pandas as pd
    from openpyxl import Workbook

    if not columns or not isinstance(columns, list):
        raise ValueError("Columns must be a non-empty list of headers.")

    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer.")

    if not all(isinstance(item, list) for item in data):
        raise ValueError("Data must be a list of lists, where each inner list represents a row.")

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data, columns=columns)

    # Create an Excel writer using openpyxl as the engine
    writer = pd.ExcelWriter("generated_excel.xlsx", engine='openpyxl')

    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False)

    # Save the Excel file
    writer.save()

    return "generated_excel.xlsx"

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_excel,
    inputs=[
        gr.Dropdown(label="Columns", choices=["Column A", "Column B", "Column C"]),
        gr.Slider(label="Rows", minimum=1, maximum=100, step=1),
        gr.Dataframe(label="Data")
    ],
    outputs="file",
    examples=[[["Column A", "Column B", "Column C"], 5, [["Row 1, Column A", "Row 1, Column B", "Row 1, Column C"], ["Row 2, Column A", "Row 2, Column B", "Row 2, Column C"]]],
)

iface.launch()