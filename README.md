# OpenAI Agents SDK Jokester 🤖

A lightweight demonstration of the OpenAI Agents SDK, showcasing how simple it is to create and run AI agents with just a few lines of code.

## Overview

This project demonstrates the core functionality of the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), a remarkably lightweight framework for building AI agents. The example creates a joke-telling agent that responds to prompts with humor about Autonomous AI Agents.

### What You'll Learn

- How to create an AI agent with custom instructions
- Using the Runner to execute agent tasks
- Implementing tracing for observability
- Working with async/await patterns in Python

## Features

- **Simple Agent Creation**: Define agents with name, instructions, and model selection
- **Async Execution**: Leverages Python's asyncio for efficient operation
- **Built-in Tracing**: Automatic trace logging to OpenAI's platform for debugging
- **Minimal Code**: Demonstrates the SDK's lightweight nature

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Basic understanding of async Python (helpful but not required)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/csg09/openai-agents-jokester.git
   cd openai-agents-jokester
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   **Important**: Never commit your `.env` file to version control!

## Usage

Run the joke-telling agent:

```bash
python jokester.py
```

### Expected Output

```
==================================================
JOKE OUTPUT:
==================================================
[Agent's joke about Autonomous AI Agents]
==================================================

View the trace at: https://platform.openai.com/traces
```

## Understanding the Code

The core implementation is remarkably simple:

```python
from agents import Agent, Runner, trace

# Create an agent
agent = Agent(
    name="Jokester",
    instructions="You are a joke teller",
    model="gpt-4o-mini"
)

# Run the agent with tracing
with trace("Telling a joke"):
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)
```

### Key Components

1. **Agent**: Defines the AI agent with a name, instructions, and model
2. **Runner**: Executes the agent with a given prompt
3. **Trace**: Provides observability by logging execution to OpenAI's trace platform

## Tracing and Observability

The SDK automatically logs traces to the OpenAI platform. After running the agent, visit:

**[https://platform.openai.com/traces](https://platform.openai.com/traces)**

Here you can:
- View execution steps
- Debug agent behavior
- Monitor performance
- Analyze prompt/response patterns

## Customization

### Change the Agent's Behavior

Modify the instructions in `jokester.py`:

```python
agent = Agent(
    name="Storyteller",
    instructions="You are a creative storyteller who writes short tales",
    model="gpt-4o-mini"
)
```

### Use a Different Model

The SDK supports various OpenAI models:
- `gpt-4o-mini` (default, cost-effective)
- `gpt-4o` (more capable)
- `gpt-4-turbo`

### Modify the Prompt

Change the prompt passed to `Runner.run()`:

```python
result = await Runner.run(agent, "Your custom prompt here")
```

## Cost Considerations

This example uses `gpt-4o-mini`, which is cost-effective for development:
- Input: ~$0.15 per 1M tokens
- Output: ~$0.60 per 1M tokens

A single joke typically costs less than $0.001.

## Project Structure

```
openai-agents-jokester/
│
├── jokester.py          # Main application
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## Resources

- **OpenAI Agents SDK Documentation**: [https://openai.github.io/openai-agents-python/](https://openai.github.io/openai-agents-python/)
- **OpenAI Traces**: [https://platform.openai.com/traces](https://platform.openai.com/traces)
- **OpenAI API Reference**: [https://platform.openai.com/docs](https://platform.openai.com/docs)

## Troubleshooting

### Import Error: `ModuleNotFoundError: No module named 'agents'`

Make sure you've installed the dependencies:
```bash
pip install -r requirements.txt
```

### Authentication Error

Verify your `.env` file contains a valid OpenAI API key:
```bash
OPENAI_API_KEY=sk-...
```

### Async Runtime Error

The code requires Python 3.8+ for async/await support. Check your version:
```bash
python --version
```

## Next Steps

After mastering this basic example, explore:

1. **Multi-turn conversations**: Building agents that maintain context
2. **Tool integration**: Adding custom functions for agents to use
3. **Agent orchestration**: Coordinating multiple agents
4. **Advanced tracing**: Custom trace attributes and debugging

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- Inspired by the simplicity and power of the Agents framework
- Part of a learning journey in AI agent development

---

**Happy Agent Building! 🚀**

*For questions or issues, please open an issue on GitHub.*
