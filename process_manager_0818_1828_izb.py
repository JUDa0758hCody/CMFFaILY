# 代码生成时间: 2025-08-18 18:28:40
import psutil
import gradio as gr
def list_processes():
    """
    List all the processes running on the system.
    
    Returns:
        list: A list of dictionaries containing process information.
    """
# 改进用户体验
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_percent', 'cpu_percent']):
        try:
            proc_info = proc.info
            if proc_info is not None:
                processes.append({
# FIXME: 处理边界情况
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'status': proc_info['status'],
                    'create_time': proc_info['create_time'],
                    'memory_percent': proc_info['memory_percent'],
# TODO: 优化性能
                    'cpu_percent': proc_info['cpu_percent'],
# NOTE: 重要实现细节
                })
# 优化算法效率
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
def terminate_process(pid):
    """
# 扩展功能模块
    Terminate a process based on its PID.
    
    Args:
        pid (int): The process ID of the process to terminate.
    
    Returns:
        str: A message indicating the result of the termination attempt.
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait()
        return f"Process {pid} terminated successfully."
    except psutil.NoSuchProcess:
        return f"No such process with PID {pid}."
    except psutil.AccessDenied:
# 扩展功能模块
        return f"Permission denied to terminate process with PID {pid}."
    except Exception as e:
        return f"An error occurred: {str(e)}"interface = gr.Interface(
# 增强安全性
    fn=list_processes,
    inputs=[],
    outputs=['json'],
    title="Process Manager",
    description="A simple process manager to list and terminate processes."
)
def terminate_process_callback(pid):
# NOTE: 重要实现细节
    result = terminate_process(pid)
    return {"result": result}
# 增强安全性
terminate_button = gr.Button("Terminate Process")
terminate_input = gr.Number(label="PID", value=0)
terminate_output = gr.Textbox(label="Result")
terminate_interface = gr.Interface(
    fn=terminate_process_callback,
    inputs=[terminate_input, terminate_button],
    outputs=[terminate_output],
    title="Terminate Process",
    description="Terminate a process by entering its PID."
)
def main():
    interface.launch()
# 增强安全性
    terminate_interface.launch()
if __name__ == "__main__":
    main()