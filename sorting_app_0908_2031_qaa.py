# 代码生成时间: 2025-09-08 20:31:29
import gradio as gr
# 添加错误处理
import numpy as np

# 排序算法选择
SORT_OPTIONS = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
# NOTE: 重要实现细节

# 冒泡排序算法实现
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
# NOTE: 重要实现细节
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 改进用户体验
    return arr

# 选择排序算法实现
def selection_sort(arr):
    for i in range(len(arr)):
# 优化算法效率
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
# NOTE: 重要实现细节
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 插入排序算法实现
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 归并排序算法实现
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
# 增强安全性
                arr[k] = R[j]
# NOTE: 重要实现细节
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# 快速排序算法实现
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 排序函数选择器
def sort_function(arr, sort_type):
    try:
        if sort_type == SORT_OPTIONS[0]:
# 添加错误处理
            return bubble_sort(arr)
        elif sort_type == SORT_OPTIONS[1]:
# FIXME: 处理边界情况
            return selection_sort(arr)
        elif sort_type == SORT_OPTIONS[2]:
            return insertion_sort(arr)
        elif sort_type == SORT_OPTIONS[3]:
            return merge_sort(arr)
# FIXME: 处理边界情况
        elif sort_type == SORT_OPTIONS[4]:
            return quick_sort(arr)
        else:
            raise ValueError("Invalid sorting type")
    except Exception as e:
        return str(e)
# NOTE: 重要实现细节

# Gradio界面定义
# 增强安全性
def main():
    with gr.Blocks() as demo:
# 扩展功能模块
        gr.Markdown("# Sorting Algorithm Demo")
        with gr.Row():
            input_box = gr.Number(label="Enter numbers separated by commas")
            sort_dropdown = gr.Dropdown(label="Choose a sorting method", choices=SORT_OPTIONS)
        output_box = gr.Textbox()
# 扩展功能模块
        with gr.Row():
            submit_btn = gr.Button("Sort")
# 优化算法效率
        output_box.change(lambda arr, sort_type: sort_function([float(x) for x in arr.split(',')], sort_type), inputs=[input_box, sort_dropdown], outputs=output_box)
# TODO: 优化性能
        submit_btn.click(lambda: None, None, None)
    demo.launch()

if __name__ == "__main__":
    main()