# Contributing to OpenAI Agents SDK Jokester

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please open an issue describing:
- The enhancement you'd like to see
- Why it would be useful
- Any implementation ideas you have

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines below
3. **Test your changes** thoroughly
4. **Update documentation** if you've changed functionality
5. **Submit a pull request** with a clear description of your changes

## Code Style Guidelines

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Comment complex logic

## Example Contribution Ideas

- Add new agent personalities
- Create different joke categories
- Implement conversation history
- Add unit tests
- Improve error handling
- Enhance documentation
- Add examples for advanced features

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/csg09/openai-agents-jokester.git
   cd openai-agents-jokester
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API key

5. Make your changes and test

## Testing

Before submitting a pull request:
- Run the main script: `python jokester.py`
- Test the advanced example: `python advanced_example.py`
- Verify all new features work as expected

## Code Review Process

All submissions require review. We'll review your PR and may suggest changes or improvements. Once approved, we'll merge your contribution!

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for helping make this project better! 🎉
