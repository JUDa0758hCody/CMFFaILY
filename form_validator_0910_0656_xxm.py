# 代码生成时间: 2025-09-10 06:56:20
import gr

# 表单数据验证器
class FormValidator:
    """
    用于验证表单输入的类
    """
    def validate(self, data):
        """
        验证表单数据
        
        :param data: 表单数据字典
        :return: 验证结果，True 或 False
        """
        try:
            # 检查数据是否为空
            if not all(data.values()):
                return False
            
            # 验证邮箱地址
            if not self.is_valid_email(data.get('email', '')):
                return False
            
            # 验证用户名长度
            if len(data.get('username', '')) < 3 or len(data.get('username', '')) > 20:
                return False
            
            # 验证密码长度
            if len(data.get('password', '')) < 6 or len(data.get('password', '')) > 20:
                return False
            
            return True
        except Exception as e:
            print(f"验证错误: {e}")
            return False
  
    def is_valid_email(self, email):
        """
        验证邮箱地址是否有效
        
        :param email: 邮箱地址
        :return: 邮箱地址是否有效
        """
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

# 使用Gradio创建表单验证器界面
def validate_interface():
    """
    创建表单验证器界面
    """
    validator = FormValidator()
    
    with gr.Blocks() as demo:
        gr.Markdown("## 表单数据验证器")
        gr.Markdown("输入表单数据进行验证")
        
        # 创建表单输入
        username = gr.Textbox(label='用户名')
        email = gr.Textbox(label='邮箱')
        password = gr.Textbox(label='密码', password=True)
        
        # 创建提交按钮
        submit = gr.Button('提交')
        
        # 创建结果输出
        result = gr.Textbox(label='验证结果')
        
        # 注册回调函数
        def validate_callback(username, email, password):
            data = {
                'username': username,
                'email': email,
                'password': password
            }
            return '验证通过' if validator.validate(data) else '验证失败'
        
        submit.click(validate_callback, inputs=[username, email, password], outputs=result)
        
    demo.launch()

if __name__ == '__main__':
    validate_interface()