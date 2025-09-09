# 代码生成时间: 2025-09-09 23:42:53
import re
import requests
import gradio as gr

def validate_url(url):
    """
    Validates the given URL by checking its format and attempting to reach it.
    
    Args:
        url (str): The URL to validate.
    
    Returns:
        str: A message indicating whether the URL is valid or not.
    """
    # Check if the URL matches a common URL pattern
    if re.match(r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([\w\.-]*)*\/*$', url):
        try:
            # Attempt to reach the URL using a HEAD request
            response = requests.head(url, allow_redirects=True)
            # If the status code is 200, the URL is valid
            if response.status_code == 200:
                return f"The URL {url} is valid."
            else:
                return f"The URL {url} is not reachable. Status code: {response.status_code}."
        except requests.RequestException as e:
            return f"An error occurred while checking the URL {url}: {e}."
    else:
        return f"The URL {url} is not in a valid format."

def main():
    """
    Sets up the Gradio interface for the URL validator.
    """
    with gr.Blocks() as demo:
        url_input = gr.Textbox(label='Enter URL to validate')
        validate_button = gr.Button('Validate')
        url_output = gr.Textbox()
        
        # Define the event flow when the validate button is clicked
        validate_button.click(fn=validate_url, inputs=url_input, outputs=url_output)
    
    # Launch the Gradio interface
    demo.launch()

if __name__ == '__main__':
    main()
