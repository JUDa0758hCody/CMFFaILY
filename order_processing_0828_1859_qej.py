# 代码生成时间: 2025-08-28 18:59:42
import gradio as gr
def process_order(order_details):
    """
    Process an order based on provided details.

    Args:
        order_details (dict): A dictionary containing details of the order.
            Expected keys are 'customer_name', 'order_id', 'items', 'total_price'.

    Returns:
        dict: A dictionary containing the processing result.
    """
    try:
        # Check if all required details are present
        required_keys = ['customer_name', 'order_id', 'items', 'total_price']
        if not all(key in order_details for key in required_keys):
            raise ValueError("Missing required order details")

        # Process the order
        result = {
            "status": "success",
            "message": "Order processed successfully",
            "order_details": order_details,
        }
        return result
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }

# Set up Gradio interface
iface = gr.Interface(
    fn=process_order,
    inputs=gr.Textbox(label="Order Details", placeholder="Enter order details as JSON"),
    outputs="json",
    title="Order Processing System",
    description="A simple order processing system using Gradio."
)

# Run the Gradio interface
iface.launch()