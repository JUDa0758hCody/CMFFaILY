# 代码生成时间: 2025-08-15 16:46:03
import sqlite3
from gradio.inputs import TextInput, NumberInput
from gradio.outputs import Label
from gradio.app import App

# 函数：防止SQL注入的查询
def safe_query(connection, query, parameters):
    """执行防止SQL注入的数据库查询。"""
    try:
        cursor = connection.cursor()
        # 使用参数化查询以防止SQL注入
        cursor.execute(query, parameters)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

# 函数：演示防止SQL注入的接口
def query_database(input_text, input_number):
    """演示接口，接收文本和数字输入，返回数据库查询结果。"""
    # 连接数据库
    conn = sqlite3.connect("example.db")
    
    # 构建参数化查询以防止SQL注入
    query = "SELECT * FROM users WHERE name = ? AND age > ?"
    parameters = (input_text, input_number)
    
    # 执行查询
    result = safe_query(conn, query, parameters)
    
    # 关闭数据库连接
    conn.close()
    
    # 将结果转换为字符串列表，便于显示
    result_str = ", ".join([f"{name}: {age}" for (name, age) in result]) if result else "No results found."
    return result_str

# 创建Gradio应用
iface = App()

# 输入组件：文本和数字输入
iface.add_component(TextInput(label="Name", placeholder="Enter name", lines=1), "input_text")
iface.add_component(NumberInput(label="Age", placeholder="Enter age", lines=1), "input_number\)

# 输出组件：显示查询结果
iface.add_component(Label(label="Results"), "output")

# 注册接口
iface.link("query_database", inputs=["input_text", "input_number"], outputs="output")

# 运行应用
iface.launch()