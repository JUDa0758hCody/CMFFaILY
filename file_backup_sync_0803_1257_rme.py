# 代码生成时间: 2025-08-03 12:57:39
import os
import shutil
import gr
from gr import Radio, File
from gr import Markdown, File
from gr import Interface

class FileBackupSync:
    """文件备份和同步工具类"""

    def __init__(self, source_path, backup_path):
        self.source_path = source_path
        self.backup_path = backup_path
        # 确保备份路径存在
        os.makedirs(self.backup_path, exist_ok=True)

    def sync(self):
        """同步源文件到备份路径"""
        try:
            # 复制目录
            shutil.copytree(self.source_path, self.backup_path)
            return f"同步完成：源路径 {self.source_path} 已同步到 {self.backup_path}"
        except Exception as e:
            # 错误处理
            return f"同步失败：{str(e)}"

    def restore(self, file_name):
        """从备份路径恢复文件"""
        try:
            # 恢复文件
            shutil.copy2(os.path.join(self.backup_path, file_name), os.path.join(self.source_path, file_name))
            return f"恢复成功：文件 {file_name} 已从备份恢复到源路径"
        except Exception as e:
            # 错误处理
            return f"恢复失败：{str(e)}"

# 创建文件备份和同步工具界面
def create_backup_sync_interface():
    """创建文件备份和同步工具界面"""
    with Interface("文件备份和同步工具", "文件操作") as demo:
        # 参数输入
        source_path = File("源路径", file_count="single")
        backup_path = File("备份路径", file_count="single")
        
        # 操作按钮
        sync_button = gr.Button("同步")
        restore_button = gr.Button("恢复")
        
        # 输出文本
        output_text = gr.Textbox(label="操作结果")
        
        # 同步操作
        def on_sync():
            tool = FileBackupSync(source_path.value, backup_path.value)
            output_text.update(tool.sync())
        
        # 恢复操作
        def on_restore():
            restore_file_name = File("恢复文件名", file_count="single")
            tool = FileBackupSync(source_path.value, backup_path.value)
            output_text.update(tool.restore(restore_file_name.value))
        
        # 绑定事件
        sync_button.click(on_sync, inputs=[], outputs=[output_text])
        restore_button.click(on_restore, inputs=[restore_file_name], outputs=[output_text])
        
        # 显示界面
        demo.launch()

if __name__ == '__main__':
    create_backup_sync_interface()