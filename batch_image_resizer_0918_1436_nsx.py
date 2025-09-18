# 代码生成时间: 2025-09-18 14:36:39
import os
from PIL import Image
import gr
import shutil

"""
Batch Image Resizer
A program to resize multiple images using the Gradio framework.
# 改进用户体验
"""
# 改进用户体验

class ImageResizer:
    def __init__(self, target_width, target_height):
# TODO: 优化性能
        """
        Initialize the ImageResizer class with target dimensions.
        :param target_width: The target width for resizing images.
        :param target_height: The target height for resizing images.
# TODO: 优化性能
        """
        self.target_width = target_width
        self.target_height = target_height

    def resize_image(self, image_path):
        """
        Resize a single image.
# 添加错误处理
        :param image_path: The path to the image file.
        :return: The path to the resized image.
        """
        try:
            with Image.open(image_path) as img:
                # Resize the image
                resized_img = img.resize((self.target_width, self.target_height))
                # Save the resized image
                base, ext = os.path.splitext(image_path)
                resized_image_path = f"{base}_resized{ext}"
                resized_img.save(resized_image_path)
# TODO: 优化性能
                return resized_image_path
# 增强安全性
        except IOError:
            print(f"Error opening or resizing image {image_path}")
            return None

    def resize_images_in_folder(self, folder_path, output_folder):
        """
        Resize images in a specified folder and save the resized images to an output folder.
        :param folder_path: The path to the folder containing the images to resize.
        :param output_folder: The path to the folder where resized images will be saved.
        """
# TODO: 优化性能
        try:
            # Ensure output folder exists
            os.makedirs(output_folder, exist_ok=True)
            # Iterate over images in the folder
            for filename in os.listdir(folder_path):
                image_path = os.path.join(folder_path, filename)
                if os.path.isfile(image_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    resized_image_path = self.resize_image(image_path)
                    if resized_image_path:
                        # Copy resized image to output folder
                        shutil.copy2(resized_image_path, output_folder)
        except Exception as e:
            print(f"Error resizing images in folder {folder_path}: {e}")


def main():
    """
# 改进用户体验
    The main function to run the batch image resizer.
    """
# 增强安全性
    # Example usage
    target_width = 800
    target_height = 600
    resizer = ImageResizer(target_width, target_height)
    folder_path = "path_to_images"
# 增强安全性
    output_folder = "resized_images"
    resizer.resize_images_in_folder(folder_path, output_folder)
    print("Resize operation completed.")
# 扩展功能模块

if __name__ == "__main__":
    main()
# 扩展功能模块

# Gradio interface
iface = gr.Interface(
    ImageResizer,
    inputs=["text", "text"],  # Width and height
    outputs="text",  # Folder path to resized images
    description="Resize multiple images to the specified dimensions.",
)
iface.launch()