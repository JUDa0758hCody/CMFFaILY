# 代码生成时间: 2025-08-02 02:34:39
import gradio as gr
from PIL import Image
import os

"""
Image Resizer is a Python program that allows users to batch resize images using the GRADIO framework.
It is designed to be user-friendly, with error handling and clear code structure.
"""

def resize_images(image_dir, output_dir, desired_height, desired_width):
    """
    Resize images in the specified directory to a desired height and width.

    Parameters:
    image_dir (str): Directory containing images to be resized.
    output_dir (str): Directory where resized images will be saved.
    desired_height (int): The desired height of the resized images.
    desired_width (int): The desired width of the resized images.
    """
    try:
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(image_dir, filename)
                with Image.open(image_path) as img:
                    resized_img = img.resize((desired_width, desired_height))
                    resized_img.save(os.path.join(output_dir, filename))
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to set up the GRADIO interface for the image resizer.
    """
    with gr.Blocks() as demo:
        # Interface components
        gr.Markdown("## Image Resizer")
        input_dir = gr.Folder(label="Select the directory containing images", type="folder")
        output_dir = gr.Folder(label="Select or create a directory to save resized images", type="folder")
        height = gr.Slider(1, 1000, default=100, label="Desired Height")
        width = gr.Slider(1, 1000, default=100, label="Desired Width")
        submit_button = gr.Button("Resize Images")
        output_dir = gr.Folder(label="Resized Images", type="folder")

        # Define the function to be executed when the button is clicked
        def resize_on_click(input_dir, output_dir, height, width):
            return resize_images(input_dir, output_dir, height, width)

        submit_button.click(resize_on_click, inputs=[input_dir, output_dir, height, width], outputs=output_dir)

    demo.launch()

if __name__ == "__main__":
    main()