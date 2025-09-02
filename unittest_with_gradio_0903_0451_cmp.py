# 代码生成时间: 2025-09-03 04:51:21
import unittest
import gr
from gr import *


# 定义一个简单的测试用例类
class SimpleMathTests(unittest.TestCase):
    """测试简单的数学运算"""
    def test_addition(self):
        """测试加法"""
        self.assertEqual(add(1, 2), 3)

    def test_subtraction(self):
        """测试减法"""
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication(self):
        """测试乘法"""
        self.assertEqual(multiply(4, 3), 12)

    def test_division(self):
        """测试除法"""
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
            

# 定义数学运算函数
def add(a, b):
    """返回两个数的和"""
    return a + b


def subtract(a, b):
    """返回两个数的差"""
    return a - b


def multiply(a, b):
    """返回两个数的积"""
    return a * b


def divide(a, b):
    """返回两个数的商"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# 定义Gradio界面
def create_interface():
    """创建Gradio界面"""
    with gr.Blocks() as demo:
        gr.Markdown("### Gradio Unit Test Example")
        with gr.Row():
            gr.Markdown("**Addition**"), gr.Number(label="a"), gr.Number(label="b"), gr.Button("Test")
            gr.Markdown(label="Result")

        with gr.Row():
            gr.Markdown("**Subtraction**"), gr.Number(label="c"), gr.Number(label="d"), gr.Button("Test")
            gr.Markdown(label="Result")

        with gr.Row():
            gr.Markdown("**Multiplication**"), gr.Number(label="e"), gr.Number(label="f"), gr.Button("Test")
            gr.Markdown(label="Result")

        with gr.Row():
            gr.Markdown("**Division**"), gr.Number(label="g"), gr.Number(label="h"), gr.Button("Test")
            gr.Markdown(label="Result")

    return demo.launch()


if __name__ == '__main__':
    print("Running tests...")
    unittest.main()
    create_interface()