# 代码生成时间: 2025-09-21 08:10:11
import gradio as gr
def add_to_cart(item, quantity):
    """
    将商品添加到购物车。
    
    参数:
    item (str): 商品名称。
    quantity (int): 商品数量。
    
    返回:
    tuple: (购物车列表, 总价格)
    """
    if quantity <= 0:
        raise ValueError("数量必须大于0")
    cart[item] = cart.get(item, 0) + quantity
    total_price = sum(item_prices.get(i, 0) * cart.get(i, 0) for i in cart)
    return cart, total_price

def remove_from_cart(item, quantity):
    """
    从购物车中移除商品。
    
    参数:
    item (str): 商品名称。
    quantity (int): 移除的商品数量。
    
    返回:
    tuple: (购物车列表, 总价格)
    """
    if quantity <= 0:
        raise ValueError("数量必须大于0")
    if cart.get(item, 0) < quantity:
        raise ValueError("购物车中没有足够的商品")
    cart[item] -= quantity
    if cart[item] == 0:
        del cart[item]
    total_price = sum(item_prices.get(i, 0) * cart.get(i, 0) for i in cart)
    return cart, total_price

def clear_cart():
    """
    清空购物车。
    
    返回:
    tuple: (空购物车列表, 总价格)
    """
    cart.clear()
    return cart, 0

def update_quantity(item, new_quantity):
    """
    更新购物车中商品的数量。
    
    参数:
    item (str): 商品名称。
    new_quantity (int): 新的商品数量。
    
    返回:
    tuple: (购物车列表, 总价格)
    """
    if new_quantity <= 0:
        raise ValueError("数量必须大于0")
    if cart.get(item, 0) < new_quantity:
        raise ValueError("购物车中没有足够的商品")
    cart[item] = new_quantity
    total_price = sum(item_prices.get(i, 0) * cart.get(i, 0) for i in cart)
    return cart, total_price

# 商品价格字典
item_prices = {"苹果": 10, "香蕉": 5, "橙子": 8, "西瓜": 20}
# 购物车字典
cart = {}

# 创建Gradio界面
iface = gr.Interface(
    fn=None,
    inputs=[
        gr.Dropdown(label="商品", choices=list(item_prices.keys())),
        gr.Textbox(label="数量"),
        gr.Button(label="添加到购物车")
    ],
    outputs=[
        gr.Textbox(label="购物车"),
        gr.Textbox(label="总价格")
    ],
    live=True
)

# 绑定按钮事件
iface.add_live_component(
    add_to_cart,
    inputs=[
        gr.Dropdown(label="商品", choices=list(item_prices.keys())),
        gr.Textbox(label="数量")
    ],
    outputs=[
        gr.Textbox(label="购物车"),
        gr.Textbox(label="总价格")
    ]
)

iface.launch()
