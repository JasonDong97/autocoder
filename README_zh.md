# AI 代码生成器

AI 代码生成器是一个基于 Python 的终端工具，利用先进的语言模型根据用户输入生成 Python 代码，并在隔离环境中执行生成的代码。它支持多种语言模型 API 的灵活配置，包括 OpenAI 和本地托管的模型（如 Ollama）。该工具还包括调试功能，可根据执行错误优化和改进生成的代码。

---

## **功能**

### **1. 代码生成**

- 根据用户提供的自然语言任务描述动态生成 Python 脚本。

### **2. 代码执行**

- 使用预配置的执行服务在隔离环境中运行生成的脚本。

### **3. 调试支持**

- 在遇到执行错误时，自动生成调试提示并优化代码。

### **4. 灵活的 API 支持**

- 无缝支持 OpenAI API 或通过灵活配置选项使用自定义 API。

### **5. 交互式终端界面**

- 使用 `rich` 库提供直观的终端交互体验和增强的视觉反馈。

### **6. 日志记录**

- 生成详细的日志用于调试和监控，包括提示、API 响应和执行结果。

---

## **项目结构**

```plaintext
project/
├── config/
│   └── config.yaml           # API 和服务的配置文件
├── logs/                     # 日志目录
│   └── *.log                 # 日志文件（模型行为、执行结果、错误）
├── scripts/
│   ├── model_interface.py    # 处理语言模型 API 交互
│   ├── execute_service.py    # 处理代码执行服务交互
│   ├── utils.py              # 工具函数（日志记录、配置加载）
├── main.py                   # 应用程序的主入口
├── requirements.txt          # Python 依赖
└── README.md                 # 文档
```

---

## **安装**

### **1. 克隆仓库**

```bash
git clone <repository_url>
cd project/
```

### **2. 安装依赖**

```bash
pip install -r requirements.txt
```

---

## **配置**

编辑 `config/config.yaml` 文件以设置 API 密钥、服务 URL 和其他配置。

```yaml
model_service:
  api_key: "your_api_key_here"           # 语言模型的 API 密钥
  api_base: "https://api.openai.com/v1"  # OpenAI 或自定义 API 的基础 URL
  model: "gpt-4"                         # 模型名称（例如 gpt-4, llama2-13b-chat）

execution_service:
  url: "http://192.168.100.207:22499/submit_code"  # 代码执行服务的 URL

logging:
  directory: "logs"                      # 日志文件目录
  level: "INFO"                          # 日志级别（例如 INFO, DEBUG）
```

---

## **使用方法**

### **1. 运行应用程序**

```bash
python main.py
```

### **2. 输入任务描述**

在提示时，输入您希望 AI 解决的任务。例如：

```plaintext
生成一个 Python 脚本，计算小于给定输入数字的所有素数之和。
```

### **3. 查看结果**

终端将显示：

- 发送给语言模型的构造提示。
- 生成的 Python 脚本。
- 执行结果（或错误信息）以精美的表格格式展示。

### **4. 调试**

如果初次执行失败，工具将自动：

- 使用错误信息和初始代码生成调试提示。
- 调用语言模型优化代码。
- 使用优化后的代码重新尝试执行。

---

## **日志**

应用程序会生成日志用于调试和监控：

- **模型行为日志：** 包含提示和 API 响应。
- **执行日志：** 包含提交的代码和执行结果。
- **错误日志：** 记录 API 调用或服务交互中的任何错误。

日志存储在 `logs/` 目录中。

---

## **自定义**

### **切换 API**

要使用本地托管的模型（如 Ollama）：

- 将 `config.yaml` 中的 `api_base` 更新为您的本地 API URL（例如 `http://127.0.0.1:8000/v1`）。
- 指定模型名称（例如 `llama2-13b-chat`）。

### **调整执行服务**

修改 `config.yaml` 中 `execution_service` 下的 `url`，指向您的执行服务。

---

## **依赖**

此项目需要以下 Python 包：

- `openai`：用于与 OpenAI 或自定义语言模型交互。
- `requests`：用于向 API 和服务发送 HTTP 请求。
- `pyyaml`：用于加载配置文件。
- `rich`：用于增强终端界面。

使用以下命令安装所有依赖：

```bash
pip install -r requirements.txt
```

---

## **示例输出**

### **用户输入**

```plaintext
生成一个 Python 脚本，打印斐波那契数列的前 50 项。
```

### **生成代码**

```python
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_sequence(50))
```

### **执行结果**

```plaintext
📊 执行结果:
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 键          ┃ 值                                         ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 输出        │ [0, 1, 1, 2, 3, 5, 8, ...]                  │
│ 错误        │                                             │
└─────────────┴─────────────────────────────────────────────┘
```

---

## **许可证**

此项目基于 MIT 许可证。详情请参阅 `LICENSE` 文件。

---

## **反馈**

如果您遇到任何问题或有改进建议，请提交 issue 或 pull request！
