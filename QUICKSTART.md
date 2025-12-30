# Quick Start Guide

Get up and running with OpenAI Agents SDK Jokester in 5 minutes!

## Prerequisites

- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation (3 steps)

### 1. Clone and Setup
```bash
git clone https://github.com/csg09/openai-agents-jokester.git
cd openai-agents-jokester
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Run It!

```bash
python jokester.py
```

You should see a joke about Autonomous AI Agents! 🎉

## Next Steps

- Check out `advanced_example.py` for more features
- Modify the agent instructions in `jokester.py`
- View traces at https://platform.openai.com/traces
- Read the full [README](README.md) for detailed documentation

## Troubleshooting

**"ModuleNotFoundError: No module named 'agents'"**
```bash
pip install -r requirements.txt
```

**"Authentication error"**
- Check your `.env` file has `OPENAI_API_KEY=sk-...`
- Verify the API key is valid at https://platform.openai.com/api-keys

**Need help?** Open an issue on GitHub!
