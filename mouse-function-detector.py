'''
鼠标功能检测器 v1.5
作者: HelloWorld05
日期: 2026-01-02
GitHub: https://github.com/helloworldpxy
'''
import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

class MouseFunctionDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标功能检测器 v1.5")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        
        # 设置主题颜色
        self.bg_color = "#f0f0f0"
        self.primary_color = "#4a6fa5"
        self.secondary_color = "#6b8cbc"
        self.accent_color = "#ff6b6b"
        self.success_color = "#51a351"
        
        self.root.configure(bg=self.bg_color)
        
        # 初始化计数器
        self.left_click_count = 0
        self.right_click_count = 0
        self.middle_click_count = 0
        self.forward_click_count = 0
        self.back_click_count = 0
        self.wheel_up_count = 0
        self.wheel_down_count = 0
        
        # 点击时间记录
        self.last_click_time = {"left": None, "right": None, "middle": None, 
                                "forward": None, "back": None}
        
        # 创建界面
        self.create_menu()
        self.create_header()
        self.create_detection_areas()
        self.create_control_panel()
        self.create_status_bar()
        
        # 绑定全局鼠标事件
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)
        
    def create_menu(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root, bg=self.bg_color, fg="black")
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0, bg=self.bg_color, fg="black")
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="重置计数器", command=self.reset_counters)
        file_menu.add_separator()
        file_menu.add_command(label="导出报告", command=self.export_report)
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 视图菜单
        view_menu = tk.Menu(menubar, tearoff=0, bg=self.bg_color, fg="black")
        menubar.add_cascade(label="视图", menu=view_menu)
        view_menu.add_command(label="统计信息", command=self.show_statistics)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0, bg=self.bg_color, fg="black")
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self.show_help)
        help_menu.add_separator()
        help_menu.add_command(label="关于", command=self.show_about)
        
    def create_header(self):
        # 创建标题栏
        header_frame = ttk.Frame(self.root, style="Header.TFrame")
        header_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        title_label = tk.Label(
            header_frame, 
            text="鼠标功能检测器 v1.5", 
            font=("微软雅黑", 20, "bold"),
            fg=self.primary_color,
            bg=self.bg_color
        )
        title_label.pack(side=tk.LEFT)
        
        # 添加时间显示
        self.time_label = tk.Label(
            header_frame,
            text="",
            font=("Arial", 10),
            fg="gray",
            bg=self.bg_color
        )
        self.time_label.pack(side=tk.RIGHT)
        
        # 更新时间显示
        self.update_time()
        
    def create_detection_areas(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 配置网格权重
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        for i in range(3):
            main_frame.rowconfigure(i, weight=1)
        
        # 定义检测区域创建函数
        def create_detection_area(row, col, title, button_num, color, icon):
            frame = tk.Frame(
                main_frame,
                bg=color,
                relief=tk.RAISED,
                bd=2,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            frame.grid(row=row, column=col, padx=8, pady=8, sticky=(tk.W, tk.E, tk.N, tk.S))
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)
            
            # 图标和标题
            title_frame = tk.Frame(frame, bg=color)
            title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=(10, 5))
            
            icon_label = tk.Label(title_frame, text=icon, font=("Arial", 16), bg=color)
            icon_label.pack(side=tk.LEFT, padx=(0, 5))
            
            title_label = tk.Label(
                title_frame, 
                text=title, 
                font=("微软雅黑", 12, "bold"),
                bg=color,
                fg="white"
            )
            title_label.pack(side=tk.LEFT)
            
            # 计数器标签
            count_var = tk.StringVar(value="点击次数: 0")
            count_label = tk.Label(
                frame,
                textvariable=count_var,
                font=("Arial", 14, "bold"),
                bg=color,
                fg="white",
                pady=20
            )
            count_label.grid(row=1, column=0)
            
            # 最后点击时间标签
            time_label = tk.Label(
                frame,
                text="最后点击: 从未",
                font=("Arial", 9),
                bg=color,
                fg="white"
            )
            time_label.grid(row=2, column=0, pady=(0, 10))
            
            return frame, count_var, time_label
        
        # 创建各个检测区域
        self.left_frame, self.left_var, self.left_time = create_detection_area(
            0, 0, "左键检测区", 1, "#4a6fa5", "🖱️"
        )
        self.right_frame, self.right_var, self.right_time = create_detection_area(
            0, 1, "右键检测区", 3, "#6b8cbc", "🖱️"
        )
        self.middle_frame, self.middle_var, self.middle_time = create_detection_area(
            1, 0, "中键检测区", 2, "#51a351", "🖱️"
        )
        self.forward_frame, self.forward_var, self.forward_time = create_detection_area(
            1, 1, "前进键检测区", 4, "#ff9966", "⏩"
        )
        self.back_frame, self.back_var, self.back_time = create_detection_area(
            2, 0, "后退键检测区", 5, "#ff6b6b", "⏪"
        )
        
        # 滚轮检测区（特殊处理）
        self.wheel_frame = tk.Frame(
            main_frame,
            bg="#9b59b6",
            relief=tk.RAISED,
            bd=2,
            highlightbackground=self.primary_color,
            highlightthickness=1
        )
        self.wheel_frame.grid(row=2, column=1, padx=8, pady=8, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.wheel_frame.columnconfigure(0, weight=1)
        self.wheel_frame.rowconfigure(1, weight=1)
        
        # 滚轮标题
        wheel_title_frame = tk.Frame(self.wheel_frame, bg="#9b59b6")
        wheel_title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=(10, 5))
        
        wheel_icon = tk.Label(wheel_title_frame, text="🔄", font=("Arial", 16), bg="#9b59b6")
        wheel_icon.pack(side=tk.LEFT, padx=(0, 5))
        
        wheel_title = tk.Label(
            wheel_title_frame, 
            text="滚轮检测区", 
            font=("微软雅黑", 12, "bold"),
            bg="#9b59b6",
            fg="white"
        )
        wheel_title.pack(side=tk.LEFT)
        
        # 滚轮计数器
        wheel_count_frame = tk.Frame(self.wheel_frame, bg="#9b59b6")
        wheel_count_frame.grid(row=1, column=0, pady=10)
        
        self.wheel_up_var = tk.StringVar(value="向上滚动: 0")
        self.wheel_down_var = tk.StringVar(value="向下滚动: 0")
        
        wheel_up_label = tk.Label(
            wheel_count_frame,
            textvariable=self.wheel_up_var,
            font=("Arial", 11, "bold"),
            bg="#9b59b6",
            fg="white"
        )
        wheel_up_label.pack()
        
        wheel_down_label = tk.Label(
            wheel_count_frame,
            textvariable=self.wheel_down_var,
            font=("Arial", 11, "bold"),
            bg="#9b59b6",
            fg="white"
        )
        wheel_down_label.pack()
        
        # 滚轮测试文本区域
        text_frame = tk.Frame(self.wheel_frame, bg="#9b59b6")
        text_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=(0, 10))
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.text_area = tk.Text(
            text_frame, 
            wrap=tk.WORD, 
            height=8, 
            width=40,
            bg="white",
            fg="black",
            font=("Arial", 10),
            relief=tk.SUNKEN,
            bd=1
        )
        
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 添加示例文本
        sample_text = """请在此区域使用鼠标滚轮进行测试。

滚动鼠标滚轮，观察文本是否能够正常滚动。

如果文本能够流畅地上下滚动，说明您的鼠标滚轮功能正常。

您可以继续滚动以测试滚轮的各种功能，包括快速滚动和慢速滚动。

这是一个测试滚轮功能的示例文本区域。通过滚动，您可以检查滚轮是否正常工作，是否有卡顿或跳跃现象。

继续滚动以完成测试。"""
        
        for _ in range(3):  # 重复文本以增加长度
            self.text_area.insert(tk.END, sample_text + "\n\n")
        
        self.text_area.config(state=tk.DISABLED)
        
        # 绑定鼠标事件
        self.bind_click_events()
        
    def bind_click_events(self):
        # 绑定点击事件
        for frame, button_num, func in [
            (self.left_frame, 1, self.on_left_click),
            (self.right_frame, 3, self.on_right_click),
            (self.middle_frame, 2, self.on_middle_click),
            (self.forward_frame, 4, self.on_forward_click),
            (self.back_frame, 5, self.on_back_click)
        ]:
            frame.bind(f"<Button-{button_num}>", func)
            for child in frame.winfo_children():
                child.bind(f"<Button-{button_num}>", func)
    
    def create_control_panel(self):
        # 创建控制面板
        control_frame = ttk.Frame(self.root, style="Control.TFrame")
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # 按钮样式
        button_style = {
            "font": ("微软雅黑", 10),
            "bg": self.secondary_color,
            "fg": "white",
            "activebackground": self.primary_color,
            "activeforeground": "white",
            "relief": tk.RAISED,
            "bd": 2,
            "padx": 15,
            "pady": 8
        }
        
        # 重置按钮
        reset_btn = tk.Button(
            control_frame,
            text="重置所有计数器",
            command=self.reset_counters,
            **button_style
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        # 测试所有按钮
        test_all_btn = tk.Button(
            control_frame,
            text="快速测试所有功能",
            command=self.quick_test_all,
            **button_style
        )
        test_all_btn.pack(side=tk.LEFT, padx=5)
        
        # 统计按钮
        stats_btn = tk.Button(
            control_frame,
            text="显示统计信息",
            command=self.show_statistics,
            **button_style
        )
        stats_btn.pack(side=tk.LEFT, padx=5)
        
        # 导出按钮
        export_btn = tk.Button(
            control_frame,
            text="导出测试报告",
            command=self.export_report,
            **button_style
        )
        export_btn.pack(side=tk.LEFT, padx=5)
        
    def create_status_bar(self):
        # 创建状态栏
        self.status_bar = tk.Label(
            self.root,
            text="就绪 | 点击任意检测区域开始测试",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=self.primary_color,
            fg="white",
            font=("Arial", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 鼠标位置显示
        self.mouse_pos_label = tk.Label(
            self.status_bar,
            text="鼠标位置: (0, 0)",
            bg=self.primary_color,
            fg="white",
            font=("Arial", 9)
        )
        self.mouse_pos_label.pack(side=tk.RIGHT, padx=10)
        
        # 绑定鼠标移动事件
        self.root.bind("<Motion>", self.update_mouse_position)
    
    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"当前时间: {current_time}")
        self.root.after(1000, self.update_time)
    
    def update_mouse_position(self, event):
        self.mouse_pos_label.config(text=f"鼠标位置: ({event.x}, {event.y})")
    
    def update_status(self, message):
        self.status_bar.config(text=f"状态: {message}")
    
    def animate_click(self, frame, original_color):
        # 点击动画效果
        frame.configure(bg=self.accent_color)
        self.root.update()
        self.root.after(100, lambda: frame.configure(bg=original_color))
    
    def on_left_click(self, event):
        self.left_click_count += 1
        self.left_var.set(f"点击次数: {self.left_click_count}")
        self.last_click_time["left"] = datetime.now().strftime("%H:%M:%S")
        self.left_time.config(text=f"最后点击: {self.last_click_time['left']}")
        self.animate_click(self.left_frame, "#4a6fa5")
        self.update_status(f"左键点击 - 总计: {self.left_click_count}")
    
    def on_right_click(self, event):
        self.right_click_count += 1
        self.right_var.set(f"点击次数: {self.right_click_count}")
        self.last_click_time["right"] = datetime.now().strftime("%H:%M:%S")
        self.right_time.config(text=f"最后点击: {self.last_click_time['right']}")
        self.animate_click(self.right_frame, "#6b8cbc")
        self.update_status(f"右键点击 - 总计: {self.right_click_count}")
    
    def on_middle_click(self, event):
        self.middle_click_count += 1
        self.middle_var.set(f"点击次数: {self.middle_click_count}")
        self.last_click_time["middle"] = datetime.now().strftime("%H:%M:%S")
        self.middle_time.config(text=f"最后点击: {self.last_click_time['middle']}")
        self.animate_click(self.middle_frame, "#51a351")
        self.update_status(f"中键点击 - 总计: {self.middle_click_count}")
    
    def on_forward_click(self, event):
        self.forward_click_count += 1
        self.forward_var.set(f"点击次数: {self.forward_click_count}")
        self.last_click_time["forward"] = datetime.now().strftime("%H:%M:%S")
        self.forward_time.config(text=f"最后点击: {self.last_click_time['forward']}")
        self.animate_click(self.forward_frame, "#ff9966")
        self.update_status(f"前进键点击 - 总计: {self.forward_click_count}")
    
    def on_back_click(self, event):
        self.back_click_count += 1
        self.back_var.set(f"点击次数: {self.back_click_count}")
        self.last_click_time["back"] = datetime.now().strftime("%H:%M:%S")
        self.back_time.config(text=f"最后点击: {self.last_click_time['back']}")
        self.animate_click(self.back_frame, "#ff6b6b")
        self.update_status(f"后退键点击 - 总计: {self.back_click_count}")
    
    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.wheel_up_count += 1
            self.wheel_up_var.set(f"向上滚动: {self.wheel_up_count}")
            self.update_status(f"滚轮向上滚动 - 总计: {self.wheel_up_count}")
        else:
            self.wheel_down_count += 1
            self.wheel_down_var.set(f"向下滚动: {self.wheel_down_count}")
            self.update_status(f"滚轮向下滚动 - 总计: {self.wheel_down_count}")
        
        # 轻微动画效果
        original_color = self.wheel_frame.cget("bg")
        self.wheel_frame.configure(bg="#d5a6e7")
        self.root.update()
        self.root.after(50, lambda: self.wheel_frame.configure(bg=original_color))
    
    def reset_counters(self):
        # 重置所有计数器
        self.left_click_count = 0
        self.right_click_count = 0
        self.middle_click_count = 0
        self.forward_click_count = 0
        self.back_click_count = 0
        self.wheel_up_count = 0
        self.wheel_down_count = 0
        
        # 更新显示
        self.left_var.set("点击次数: 0")
        self.right_var.set("点击次数: 0")
        self.middle_var.set("点击次数: 0")
        self.forward_var.set("点击次数: 0")
        self.back_var.set("点击次数: 0")
        self.wheel_up_var.set("向上滚动: 0")
        self.wheel_down_var.set("向下滚动: 0")
        
        # 重置时间显示
        for time_label in [self.left_time, self.right_time, self.middle_time, 
                          self.forward_time, self.back_time]:
            time_label.config(text="最后点击: 从未")
        
        self.update_status("所有计数器已重置")
        messagebox.showinfo("重置成功", "所有计数器已重置为0！")
    
    def quick_test_all(self):
        # 快速测试所有功能
        test_sequence = [
            ("左键", self.on_left_click),
            ("右键", self.on_right_click),
            ("中键", self.on_middle_click),
            ("前进键", self.on_forward_click),
            ("后退键", self.on_back_click)
        ]
        
        self.update_status("开始快速测试所有功能...")
        
        for name, func in test_sequence:
            self.root.after(300, lambda f=func: f(None))
            self.root.update()
            self.root.after(100)
        
        self.root.after(500, lambda: self.update_status("快速测试完成！"))
    
    def show_statistics(self):
        # 显示统计信息
        total_clicks = (self.left_click_count + self.right_click_count + 
                       self.middle_click_count + self.forward_click_count + 
                       self.back_click_count)
        
        total_wheel = self.wheel_up_count + self.wheel_down_count
        
        stats_text = f"""鼠标功能统计报告

基本点击统计:
----------------
左键点击次数: {self.left_click_count}
右键点击次数: {self.right_click_count}
中键点击次数: {self.middle_click_count}
前进键点击次数: {self.forward_click_count}
后退键点击次数: {self.back_click_count}

滚轮统计:
----------------
向上滚动次数: {self.wheel_up_count}
向下滚动次数: {self.wheel_down_count}

汇总信息:
----------------
总点击次数: {total_clicks}
总滚动次数: {total_wheel}
总操作次数: {total_clicks + total_wheel}

最后操作时间:
----------------
左键: {self.last_click_time.get('left', '从未')}
右键: {self.last_click_time.get('right', '从未')}
中键: {self.last_click_time.get('middle', '从未')}
前进键: {self.last_click_time.get('forward', '从未')}
后退键: {self.last_click_time.get('back', '从未')}
"""
        
        # 创建统计窗口
        stats_window = tk.Toplevel(self.root)
        stats_window.title("统计信息")
        stats_window.geometry("400x500")
        stats_window.resizable(False, False)
        
        # 添加文本区域显示统计信息
        text_widget = tk.Text(stats_window, wrap=tk.WORD, font=("Consolas", 10))
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_widget.insert(tk.END, stats_text)
        text_widget.config(state=tk.DISABLED)
        
        # 添加关闭按钮
        close_btn = tk.Button(
            stats_window,
            text="关闭",
            command=stats_window.destroy,
            bg=self.secondary_color,
            fg="white",
            padx=20,
            pady=5
        )
        close_btn.pack(pady=(0, 10))
    
    def export_report(self):
        # 导出测试报告
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"鼠标测试报告_{timestamp}.txt"
            
            report = f"""鼠标功能检测器 - 测试报告
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
版本: v1.5

测试结果:
==========
1. 左键测试: {'正常' if self.left_click_count > 0 else '未测试'}
   点击次数: {self.left_click_count}
   最后点击: {self.last_click_time.get('left', '从未')}

2. 右键测试: {'正常' if self.right_click_count > 0 else '未测试'}
   点击次数: {self.right_click_count}
   最后点击: {self.last_click_time.get('right', '从未')}

3. 中键测试: {'正常' if self.middle_click_count > 0 else '未测试'}
   点击次数: {self.middle_click_count}
   最后点击: {self.last_click_time.get('middle', '从未')}

4. 前进键测试: {'正常' if self.forward_click_count > 0 else '未测试'}
   点击次数: {self.forward_click_count}
   最后点击: {self.last_click_time.get('forward', '从未')}

5. 后退键测试: {'正常' if self.back_click_count > 0 else '未测试'}
   点击次数: {self.back_click_count}
   最后点击: {self.last_click_time.get('back', '从未')}

6. 滚轮测试: {'正常' if (self.wheel_up_count + self.wheel_down_count) > 0 else '未测试'}
   向上滚动: {self.wheel_up_count}
   向下滚动: {self.wheel_down_count}

总结:
==========
总测试操作数: {self.left_click_count + self.right_click_count + self.middle_click_count + 
               self.forward_click_count + self.back_click_count + 
               self.wheel_up_count + self.wheel_down_count}

检测结果: {'所有测试功能正常' if (self.left_click_count > 0 and self.right_click_count > 0) else '部分功能未测试'}

备注:
==========
- 此报告由鼠标功能检测器 v1.5 生成
- 仅显示已执行的测试项目
- 未测试的项目可能表示该功能不可用或未进行测试
"""
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(report)
            
            messagebox.showinfo("导出成功", f"测试报告已保存为: {filename}")
            self.update_status(f"报告已导出: {filename}")
            
        except Exception as e:
            messagebox.showerror("导出失败", f"无法导出报告: {str(e)}")
    
    def show_help(self):
        help_text = """鼠标功能检测器 v1.5 - 使用说明

主要功能区域:
1. 左键检测区 (蓝色) - 测试鼠标左键功能
2. 右键检测区 (浅蓝色) - 测试鼠标右键功能
3. 中键检测区 (绿色) - 测试鼠标中键(滚轮按下)功能
4. 前进键检测区 (橙色) - 测试鼠标前进侧键功能
5. 后退键检测区 (红色) - 测试鼠标后退侧键功能
6. 滚轮检测区 (紫色) - 测试鼠标滚轮上下滚动功能

新增功能:
• 点击动画反馈 - 点击时区域颜色变化
• 实时时间显示 - 界面右上角显示当前时间
• 鼠标位置跟踪 - 状态栏显示鼠标坐标
• 快速测试 - 一键测试所有鼠标功能
• 统计信息 - 查看详细的测试数据
• 导出报告 - 生成文本格式的测试报告
• 状态提示 - 实时显示当前操作状态

使用提示:
• 直接点击对应颜色的区域进行测试
• 使用"快速测试"按钮可以自动测试所有功能
• 所有计数器可以一键重置
• 测试结果可以导出为文本报告

注意: 某些鼠标可能没有前进和后退侧键。"""
        
        messagebox.showinfo("帮助", help_text)
    
    def show_about(self):
        about_text = """鼠标功能检测器 v1.5

开发者: HelloWorld05
发布日期: 2026-01-02
GitHub: https://github.com/helloworldpxy
项目地址: https://github.com/helloworldpxy/mouse-function-detector

主要更新:
• 界面全面美化，采用彩色主题设计
• 新增点击动画反馈效果
• 添加实时时间显示和鼠标位置跟踪
• 新增快速测试功能
• 添加统计信息窗口
• 支持导出测试报告
• 优化用户体验和交互

开源协议: MPL-2.0 license

感谢使用! 如有问题或建议，请在GitHub提交Issue。"""
        
        messagebox.showinfo("关于", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseFunctionDetector(root)
    root.mainloop()