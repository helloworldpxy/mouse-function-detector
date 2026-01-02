# 鼠标功能检测器 (Mouse Function Detector)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MPL--2.0-orange)
![Version](https://img.shields.io/badge/Version-1.0-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

一个功能完善的Python应用程序，用于全面检测鼠标各按键和滚轮功能是否正常工作。该工具特别适合测试鼠标是否存在按键连点、滚轮失灵或侧键故障等问题。

## 目录

- [功能特点](#功能特点)
- [安装指南](#安装指南)
- [使用说明](#使用说明)
- [开发指南](#开发指南)
- [常见问题](#常见问题)
- [更新日志](#更新日志)
- [贡献指南](#贡献指南)
- [许可证](#许可证)
- [开发者信息](#开发者信息)

## 功能特点

### 全面的鼠标功能检测
- **左键检测**：测试左键单击功能和连点情况
- **右键检测**：测试右键单击功能和菜单键
- **中键检测**：测试鼠标滚轮按下功能
- **前进侧键检测**：测试鼠标前进侧键功能
- **后退侧键检测**：测试鼠标后退侧键功能
- **滚轮检测**：通过滚动文本测试滚轮流畅度

### 用户友好的界面
- 直观的分区设计，每个功能区明确标识
- 实时计数器显示每种操作的点击次数
- 响应式布局，适应不同窗口大小
- 简洁明了的菜单和帮助系统

### 跨平台兼容性
- 支持 Windows、macOS 和 Linux 系统
- 基于 Python 标准库，无需额外依赖

## 安装指南

### 前提条件
- Python 3.6 或更高版本
- Tkinter 库（通常包含在Python标准库中）

### 安装步骤

1. 克隆或下载本项目到本地：
   ```bash
   git clone https://github.com/helloworldpxy/mouse-function-detector.git
   cd mouse-function-detector
   ```

2. (可选) 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. 运行主程序：
   ```bash
   python mouse-function-detector.py
   ```

### 打包为可执行文件 (可选)

使用 PyInstaller 打包为独立可执行文件：

```bash
pip install pyinstaller
pyinstaller -w -F mouse-function-detector.py
```

打包后的可执行文件将在 `dist` 目录中生成。

## 使用说明

### 基本操作

1. **左键测试**：在左键检测区内单击鼠标左键，计数器会增加
2. **右键测试**：在右键检测区内单击鼠标右键，计数器会增加
3. **中键测试**：在中键检测区内按下鼠标滚轮（中键），计数器会增加
4. **侧键测试**：
   - 在前进键检测区内单击鼠标前进侧键（通常位于鼠标左侧）
   - 在后退键检测区内单击鼠标后退侧键（通常位于鼠标左侧）
5. **滚轮测试**：在滚轮检测区内滚动鼠标滚轮，观察文本滚动是否流畅

### 高级功能

- **连点检测**：快速连续点击某个按键，观察计数器是否准确递增
- **功能验证**：通过多次操作验证鼠标按键是否响应正常
- **问题诊断**：如果某个区域的计数器不增加，可能表示对应的鼠标按键有问题

### 注意事项

- 某些鼠标可能没有前进和后退侧键，这些按钮可能无法在所有鼠标上测试
- 在Linux系统上，可能需要额外配置才能正确检测所有鼠标按键
- 如果遇到检测不准确的情况，请尝试以管理员/root权限运行程序

## 开发指南

### 代码结构

主程序 `mouse-function-detector.py` 包含以下主要组件：

1. **MouseFunctionDetector 类**：主应用程序类
   - `__init__`：初始化界面和计数器
   - `create_menu`：创建菜单栏
   - `create_detection_areas`：创建检测区域
   - 事件处理函数：处理各种鼠标事件
   - `show_help` 和 `show_about`：显示帮助和关于信息

2. **GUI 组件**：
   - 使用 Tkinter 和 ttk 创建现代化界面
   - 使用 LabelFrame 组织各个检测区域
   - 使用网格布局管理器实现响应式设计

## 常见问题

### Q: 为什么侧键检测区没有反应？
A: 某些鼠标驱动程序可能不会将侧键事件传递给应用程序，或者侧键被映射为其他功能。请检查鼠标驱动程序设置。

### Q: 在Linux系统上无法检测到中键点击？
A: 在某些Linux发行版上，可能需要调整系统设置才能正确检测中键点击。尝试在系统设置中检查鼠标配置。

### Q: 如何重置计数器？
A: 当前版本需要重启程序来重置计数器。未来版本可能会添加重置按钮。

## 更新日志
### v1.5 (2026-01-02)

#### 主要更新内容：

1. UI美化
- 采用现代化彩色主题设计
- 每个检测区域有不同颜色标识
- 添加图标和视觉元素
- 优化布局和间距
- 添加状态栏显示鼠标位置
- 添加实时时间显示

2. 新增功能
- 点击动画反馈：点击时区域颜色变化
- 鼠标位置跟踪：状态栏实时显示鼠标坐标
- 快速测试功能：一键自动测试所有鼠标功能
- 统计信息窗口：显示详细的测试数据
- 导出报告功能：生成文本格式的测试报告
- 滚轮详细计数：分别统计向上和向下滚动次数
- 最后点击时间记录：记录每个按钮的最后操作时间

3. 用户体验优化
- 更详细的状态提示
- 改进的帮助文档
- 更多控制按钮
- 更好的错误处理
- 更清晰的界面分区

4. 代码优化
- 模块化设计，便于维护
- 添加更多注释
- 改进事件处理机制
- 添加类型提示和错误处理

### v1.0 (2025-09-01)
- 初始版本发布
- 实现所有鼠标按键检测功能
- 添加滚轮检测区域
- 创建图形用户界面
- 添加帮助和关于页面

### 计划中的功能
- 双击速度测试
- 鼠标移动轨迹记录
- 测试结果导出功能
- 多语言支持
- 暗色主题

## 贡献指南

欢迎为本项目做出贡献！以下是参与方式：

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 报告问题

如果您发现任何错误或有改进建议，请提交 Issue，包括：
- 详细的问题描述
- 重现步骤
- 预期行为和实际行为
- 操作系统和Python版本信息
- 相关截图

## 许可证

本项目采用 Mozilla Public License 2.0 (MPL-2.0) 开源许可证。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

MPL-2.0 许可证允许您自由使用、修改和分发代码，但要求：
1. 如果您修改了源代码，必须公开修改后的源代码
2. 保留原始的版权声明和许可证

## 开发者信息

- **开发者**: HelloWorld05
- **GitHub主页**: [https://github.com/helloworldpxy](https://github.com/helloworldpxy)
- **项目地址**: [https://github.com/helloworldpxy/mouse-function-detector](https://github.com/helloworldpxy/mouse-function-detector)
- **联系方式**: 通过GitHub Issues或Pull Requests联系

感谢使用鼠标功能检测器！如果您觉得这个工具有用，请给项目一个Star以表示支持。
