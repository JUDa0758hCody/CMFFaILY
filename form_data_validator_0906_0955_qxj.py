# 代码生成时间: 2025-09-06 09:55:48
import gradio as gr

# 定义一个表单数据验证器类
class FormDataValidator:
    """
    用于验证表单数据的类。
    
    Attributes:
        error_messages (list): 存储验证错误消息。
    """
    def __init__(self):
        self.error_messages = []

    def validate_name(self, name):
        """
        验证名字是否至少包含2个字符。
        
        Args:
            name (str): 需要验证的名字。
        """
        if len(name) < 2:
            self.error_messages.append("Name must be at least 2 characters long.")

    def validate_email(self, email):
        """
        验证邮箱是否符合标准格式。
        
        Args:
            email (str): 需要验证的邮箱地址。
        """
        import re
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            self.error_messages.append("Invalid email format.")

    def validate_age(self, age):
        """
        验证年龄是否在18到100之间。
        
        Args:
            age (int): 需要验证的年龄。
        """
        if age < 18 or age > 100:
            self.error_messages.append("Age must be between 18 and 100.")

    def validate(self, data):
        """
        对表单数据进行验证，并返回错误消息列表。
        
        Args:
            data (dict): 包含表单数据的字典。
        
        Returns:
            list: 验证错误消息列表。
        """
        self.error_messages.clear()
        self.validate_name(data.get('name'))
        self.validate_email(data.get('email'))
        self.validate_age(data.get('age'))
        return self.error_messages

# 创建Gradio接口
def gradio_interface():
    validator = FormDataValidator()
    
    def validate_form(data):
        errors = validator.validate(data)
        if errors:
            return {"errors": errors}
        return {"success": True}
    
    demo = gr.Interface(
        fn=validate_form,
        inputs=["text", "text", "number"],
        outputs="json",
        title="Form Data Validator",
        description="Validate form data using Gradio."
    )
    demo.launch()

# 运行Gradio接口
if __name__ == '__main__':
    gradio_interface()