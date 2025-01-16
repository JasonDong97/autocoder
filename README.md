# Autocoder: Unified Code Execution and AI Code Generation

Autocoder is a comprehensive tool that combines secure code execution in a Dockerized environment with AI-driven Python script generation. It enables dynamic script generation using natural language inputs and provides a secure environment for executing those scripts.

---

## Features

### **Code Execution**

* Securely execute Python code inside an isolated Docker container.
* Submit code dynamically through a REST API.

### **AI Code Generation**

* Generate Python scripts from natural language task descriptions using advanced language models like GPT-4.
* Automatically debug and refine generated scripts based on errors during execution.

### **Logging and Feedback**

* Rich feedback with detailed logs, output, and error messages.
* Interactive debugging for AI-generated scripts.

### **Flexible Configuration**

* Support for multiple APIs (OpenAI, custom models).
* Adjustable execution timeouts and environment configurations.

---

## Project Structure

```plaintext
autocoder/
├── CodeExecutor/                     # Secure code execution service
│   ├── app/                          # FastAPI app for code execution
│   ├── host_code/                    # Directory for user-submitted code
│   ├── Dockerfile                    # Docker container definition
│   ├── requirements.txt              # Dependencies for CodeExecutor
│   └── README.md                     # Documentation for CodeExecutor
├── LLMCoder/                         # AI-based code generation tool
│   ├── config/                       # Configuration files (e.g., API keys, URLs)
│   ├── logs/                         # Logs directory
│   ├── scripts/                      # Core scripts for AI code generation
│   │   ├── model_interface.py        # API interactions for language models
│   │   ├── execute_service.py        # Interactions with the execution service
│   │   ├── utils.py                  # Utilities (e.g., logging, config loading)
│   ├── main.py                       # Main entry point for code generation
│   ├── requirements.txt              # Dependencies for LLMCoder
│   └── README.md                     # Documentation for LLMCoder
├── .gitignore                        # Files to ignore in version control
├── LICENSE                           # License information
└── README.md                         # Combined project documentation
```

---

## Installation

### **1. Clone the Repository**

```bash
git clone <repository_url>
cd autocoder/
```

### **2. Build the Docker Image**

Navigate to the `CodeExecutor` directory and build the Docker image:

```bash
cd CodeExecutor
docker build -t code-executor .
```

### **3. Install Dependencies**

Install dependencies for the `LLMCoder` module:

```bash
pip install -r LLMCoder/requirements.txt
```

---

## Usage

### **1. Run the Execution Service**

Start the Docker container to host the execution service:

```bash
docker run --rm -v $(pwd)/host_code:/usr/src/app/host_code -p 8000:8000 code-executor
```

### **2. Run the AI Code Generator**

Start the AI code generator:

```bash
python LLMCoder/main.py
```

Follow the prompts to:

* Generate Python scripts using AI.
* Automatically execute the generated scripts via the `CodeExecutor` service.

---

## Configuration

### **Execution Service**

The `CodeExecutor` module runs on Docker and can be configured in `app/`.

### **AI Code Generator**

Update the `LLMCoder/config/config.yaml` file to customize API keys, service URLs, and logging preferences:

```yaml
model_service:
  api_key: "your_api_key_here"
  api_base: "https://api.openai.com/v1"
  model: "gpt-4"

execution_service:
  url: "http://127.0.0.1:8000/submit_code"

logging:
  directory: "logs"
  level: "INFO"
```

---

## Example Workflows

### **AI-Generated Script**

Task: Generate a Python script to calculate the Fibonacci sequence.

```plaintext
Generate a Python script to calculate the Fibonacci sequence up to the 50th term.
```

Generated Code:

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

Execution Output:

```plaintext
[0, 1, 1, 2, 3, 5, 8, ...]
```

---

## Future Improvements

* Add support for additional programming languages.
* Introduce authentication for API endpoints.
* Expand resource isolation using advanced sandboxing techniques.
* Integrate CI/CD pipelines for streamlined testing and deployment.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
