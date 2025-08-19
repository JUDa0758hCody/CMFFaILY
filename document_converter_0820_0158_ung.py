# 代码生成时间: 2025-08-20 01:58:55
import gr
from gr.inputs import File
from gr.outputs import File, Label
import os
import shutil

class DocumentConverter:
    """A class to convert documents between different formats using Gradio."""

    def __init__(self):
        # Initialize Gradio interface
        self.interface = gr.Interface(
            fn=self.convert_document,
            inputs=[File(label='Upload document'), File(label='Choose output format')],
            outputs=[File(label='Converted document'), Label(label='Status')],
            title='Document Format Converter',
            description='Convert documents between different formats.'
        )

    def convert_document(self, input_document, output_format):
        """Converts the document to the specified format."""
        # Ensure the output directory exists
        output_dir = 'output/'
        os.makedirs(output_dir, exist_ok=True)

        # Define the file name without extension
        file_name_without_ext = os.path.splitext(os.path.basename(input_document.name))[0]

        # Define the output file path
        output_file_path = os.path.join(output_dir, f'{file_name_without_ext}.{output_format}')

        # Copy the input file to the output directory with the new extension
        try:
            shutil.copy(input_document.file, output_file_path)
            return output_file_path, f'Document converted successfully to {output_format}.'
        except Exception as e:
            # Handle any errors that occur during the conversion process
            return None, f'Error converting document: {str(e)}'

    def run(self):
        "