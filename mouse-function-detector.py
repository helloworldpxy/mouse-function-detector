import tkinter as tk
from tkinter import ttk, messagebox

class MouseFunctionDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标功能检测器 v1.0")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 初始化计数器
        self.left_click_count = 0
        self.right_click_count = 0
        self.middle_click_count = 0
        self.forward_click_count = 0
        self.back_click_count = 0
        self.wheel_count = 0
        
        # 创建界面
        self.create_menu()
        self.create_detection_areas()
        
    def create_menu(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self.show_help)
        help_menu.add_separator()
        help_menu.add_command(label="关于", command=self.show_about)
        
    def create_detection_areas(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # 左键检测区
        left_frame = ttk.LabelFrame(main_frame, text="左键检测区", padding="10")
        left_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        self.left_label = ttk.Label(left_frame, text="点击次数: 0", font=("Arial", 14))
        self.left_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 右键检测区
        right_frame = ttk.LabelFrame(main_frame, text="右键检测区", padding="10")
        right_frame.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        self.right_label = ttk.Label(right_frame, text="点击次数: 0", font=("Arial", 14))
        self.right_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 中键检测区
        middle_frame = ttk.LabelFrame(main_frame, text="中键检测区", padding="10")
        middle_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.rowconfigure(0, weight=1)
        
        self.middle_label = ttk.Label(middle_frame, text="点击次数: 0", font=("Arial", 14))
        self.middle_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 前进键检测区
        forward_frame = ttk.LabelFrame(main_frame, text="前进键检测区", padding="10")
        forward_frame.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        forward_frame.columnconfigure(0, weight=1)
        forward_frame.rowconfigure(0, weight=1)
        
        self.forward_label = ttk.Label(forward_frame, text="点击次数: 0", font=("Arial", 14))
        self.forward_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 后退键检测区
        back_frame = ttk.LabelFrame(main_frame, text="后退键检测区", padding="10")
        back_frame.grid(row=2, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        back_frame.columnconfigure(0, weight=1)
        back_frame.rowconfigure(0, weight=1)
        
        self.back_label = ttk.Label(back_frame, text="点击次数: 0", font=("Arial", 14))
        self.back_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 滚轮检测区
        wheel_frame = ttk.LabelFrame(main_frame, text="滚轮检测区", padding="10")
        wheel_frame.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        wheel_frame.columnconfigure(0, weight=1)
        wheel_frame.rowconfigure(0, weight=1)
        
        # 创建文本框用于滚轮检测
        self.text_area = tk.Text(wheel_frame, wrap=tk.WORD, height=8, width=40)
        scrollbar = ttk.Scrollbar(wheel_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 添加一些文本内容
        sample_text = """请在此区域使用鼠标滚轮进行测试。

滚动鼠标滚轮，观察文本是否能够正常滚动。

如果文本能够流畅地上下滚动，说明您的鼠标滚轮功能正常。

您可以继续滚动以测试滚轮的各种功能，包括快速滚动和慢速滚动。

这是一个测试滚轮功能的示例文本区域。通过滚动，您可以检查滚轮是否正常工作，是否有卡顿或跳跃现象。

继续滚动以完成测试。

请在此区域使用鼠标滚轮进行测试。

滚动鼠标滚轮，观察文本是否能够正常滚动。

如果文本能够流畅地上下滚动，说明您的鼠标滚轮功能正常。

您可以继续滚动以测试滚轮的各种功能，包括快速滚动和慢速滚动。

这是一个测试滚轮功能的示例文本区域。通过滚动，您可以检查滚轮是否正常工作，是否有卡顿或跳跃现象。

继续滚动以完成测试。

请在此区域使用鼠标滚轮进行测试。

滚动鼠标滚轮，观察文本是否能够正常滚动。

如果文本能够流畅地上下滚动，说明您的鼠标滚轮功能正常。

您可以继续滚动以测试滚轮的各种功能，包括快速滚动和慢速滚动。

这是一个测试滚轮功能的示例文本区域。通过滚动，您可以检查滚轮是否正常工作，是否有卡顿或跳跃现象。

继续滚动以完成测试。

请在此区域使用鼠标滚轮进行测试。

滚动鼠标滚轮，观察文本是否能够正常滚动。

如果文本能够流畅地上下滚动，说明您的鼠标滚轮功能正常。

您可以继续滚动以测试滚轮的各种功能，包括快速滚动和慢速滚动。

这是一个测试滚轮功能的示例文本区域。通过滚动，您可以检查滚轮是否正常工作，是否有卡顿或跳跃现象。

继续滚动以完成测试。"""
        
        self.text_area.insert(tk.END, sample_text)
        self.text_area.config(state=tk.DISABLED)  # 设置为只读
        
        # 绑定鼠标事件
        left_frame.bind("<Button-1>", self.on_left_click)
        self.left_label.bind("<Button-1>", self.on_left_click)
        
        right_frame.bind("<Button-3>", self.on_right_click)
        self.right_label.bind("<Button-3>", self.on_right_click)
        
        middle_frame.bind("<Button-2>", self.on_middle_click)
        self.middle_label.bind("<Button-2>", self.on_middle_click)
        
        # 绑定前进和后退按钮（通常这些是鼠标侧键）
        forward_frame.bind("<Button-4>", self.on_forward_click)
        self.forward_label.bind("<Button-4>", self.on_forward_click)
        
        back_frame.bind("<Button-5>", self.on_back_click)
        self.back_label.bind("<Button-5>", self.on_back_click)
        
        # 配置所有框架的网格权重
        for i in range(3):
            main_frame.rowconfigure(i, weight=1)
        for i in range(2):
            main_frame.columnconfigure(i, weight=1)
            
    def on_left_click(self, event):
        self.left_click_count += 1
        self.left_label.config(text=f"点击次数: {self.left_click_count}")
        
    def on_right_click(self, event):
        self.right_click_count += 1
        self.right_label.config(text=f"点击次数: {self.right_click_count}")
        
    def on_middle_click(self, event):
        self.middle_click_count += 1
        self.middle_label.config(text=f"点击次数: {self.middle_click_count}")
        
    def on_forward_click(self, event):
        self.forward_click_count += 1
        self.forward_label.config(text=f"点击次数: {self.forward_click_count}")
        
    def on_back_click(self, event):
        self.back_click_count += 1
        self.back_label.config(text=f"点击次数: {self.back_click_count}")
        
    def show_help(self):
        help_text = """鼠标功能检测器使用说明

1. 左键检测区：在此区域单击鼠标左键，计数器会增加
2. 右键检测区：在此区域单击鼠标右键，计数器会增加
3. 中键检测区：在此区域单击鼠标中键（滚轮按下），计数器会增加
4. 前进键检测区：在此区域单击鼠标前进侧键（如果有），计数器会增加
5. 后退键检测区：在此区域单击鼠标后退侧键（如果有），计数器会增加
6. 滚轮检测区：在此区域滚动鼠标滚轮，测试滚轮功能是否正常

注意：某些鼠标可能没有前进和后退侧键。"""
        
        messagebox.showinfo("帮助", help_text)
        
    def show_about(self):
        about_text = """鼠标功能检测器 v1.0

开发者: HelloWorld05
GitHub: https://github.com/helloworldpxy
项目地址: https://github.com/helloworldpxy/mouse-function-detector

开源协议: MPL-2.0 license"""
        
        messagebox.showinfo("关于", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseFunctionDetector(root)
    root.mainloop()