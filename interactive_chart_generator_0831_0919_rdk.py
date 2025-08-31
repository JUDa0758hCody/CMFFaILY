# 代码生成时间: 2025-08-31 09:19:08
import gradio as gr
def generate_chart(x, y, chart_type):
    """Generates an interactive chart based on user input."""
    try:
        import plotly.graph_objects as go
        import pandas as pd
        
        # Create a dataframe from the input lists
        df = pd.DataFrame({'x': x, 'y': y})
        
        # Generate chart based on the chart type
        if chart_type == 'line':
            chart = go.Figure(data=[go.Scatter(x=df['x'], y=df['y'])])
        elif chart_type == 'bar':
            chart = go.Figure(data=[go.Bar(x=df['x'], y=df['y'])])
        elif chart_type == 'scatter':
            chart = go.Figure(data=[go.Scatter(x=df['x'], y=df['y'], mode='markers')])
        else:
            raise ValueError("Unsupported chart type. Choose 'line', 'bar', or 'scatter'.")
        
        # Update layout to be more readable
        chart.update_layout(title=f'{chart_type.capitalize()} Chart', xaxis_title='X Axis', yaxis_title='Y Axis')
        
        # Return the chart
        return chart
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """Main function to create a Gradio interface."""
    demo = gr.Interface(
        fn=generate_chart,
        inputs=[gr.Slider(label='X values', label='X Axis', value=[1, 2, 3, 4]), 
                gr.Slider(label='Y values', label='Y Axis', value=[10, 15, 13, 17]), 
                gr.Radio(label='Chart Type', choices=['line', 'bar', 'scatter'], value='line')],
        outputs="plot",
        examples=[[[1, 2, 3, 4], [10, 15, 13, 17], 'line']],
    )
    demo.launch()

def __name__ == "__main__":
    main()
