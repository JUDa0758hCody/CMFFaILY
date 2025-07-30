# 代码生成时间: 2025-07-30 22:04:01
import os
import shutil
from gradio import interfaces, gr


"""
Folder Organizer App using Gradio framework
This application allows users to select a directory and organize its contents by extensions.
"""

# Define the function to organize files by extension
def organize_files_by_extension(directory: str):
    """
    Organize files in the given directory by their extensions.
    :param directory: The path to the directory to be organized.
    """
    try:
        # List all files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # Extract extensions from filenames and create a dictionary
        extensions = {f.split('.')[-1]: [] for f in files}
        for f in files:
            ext = f.split('.')[-1]
            extensions[ext].append(f)
        
        # Create directories for each extension and move files into them
        for ext, files in extensions.items():
            os.makedirs(os.path.join(directory, ext), exist_ok=True)
            for file in files:
                shutil.move(os.path.join(directory, file), os.path.join(directory, ext, file))

        # Return a success message
        return f"Files organized in: {directory}"
    except Exception as e:
        # Return an error message if something goes wrong
        return f"An error occurred: {str(e)}"

# Create the Gradio interface
iface = gr.Interface(
    # The function to call when the user interacts with the app
    fn=organize_files_by_extension,
    # The input interface, allowing the user to select a directory
    inputs=interfaces.Directory(label="Select a directory"),
    # The output interface, showing the result of the operation
    outputs="text",
    # A title and description for the interface
    title="Folder Organizer",
    description="Select a directory to organize its contents by file extensions."
)

# Run the Gradio interface
iface.launch(share=True)