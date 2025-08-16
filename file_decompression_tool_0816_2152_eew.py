# 代码生成时间: 2025-08-16 21:52:47
import os
import zipfile
import tarfile
import gradio as gr

"""
压缩文件解压工具，支持ZIP和TAR格式的文件。
使用GRADIO框架创建一个简单的用户界面，允许用户上传压缩文件，并选择解压格式进行解压。
"""

def unzip_file(file_path, extract_path):
    """
    解压ZIP文件。
    
    参数:
    file_path (str): ZIP文件路径。
    extract_path (str): 解压后文件存放路径。
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        return f"ZIP file extracted to {extract_path}"
    except zipfile.BadZipFile:
        return "Invalid ZIP file."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def untar_file(file_path, extract_path):
    """
    解压TAR文件。
    
    参数:
    file_path (str): TAR文件路径。
    extract_path (str): 解压后文件存放路径。
    """
    try:
        with tarfile.TarFile(file_path, 'r') as tar_ref:
            tar_ref.extractall(extract_path)
        return f"TAR file extracted to {extract_path}"
    except tarfile.TarError:
        return "Invalid TAR file."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# 创建GRADIO界面
iface = gr.Interface(
    title="File Decompression Tool",
    description="Upload a compressed file and choose the format to extract.",
    inputs=[
        gr.File(label="Upload compressed file"),
        gr.Dropdown(label="Choose format", choices=["ZIP", "TAR"])
    ],
    outputs=gr.Textbox(label="Result"),
)

# 定义处理函数
def process_file(input_file, file_format):
    if file_format == "ZIP":
        return unzip_file(input_file.name, "./extracted/")
    elif file_format == "TAR":
        return untar_file(input_file.name, "./extracted/")
    else:
        return "Unsupported file format."

# 注册处理函数
iface.register(process_file)

# 运行GRADIO界面
iface.launch()