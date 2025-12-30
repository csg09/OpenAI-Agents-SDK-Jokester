"""
Setup Verification Script
Run this to verify your environment is configured correctly.
"""

import sys
import os


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version >= (3, 8):
        print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version {version.major}.{version.minor} is too old. Need 3.8+")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    required = {
        "agents": "openai-agents-python",
        "dotenv": "python-dotenv"
    }
    
    all_installed = True
    for module, package in required.items():
        try:
            __import__(module)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            all_installed = False
    
    return all_installed


def check_env_file():
    """Check if .env file exists and has API key."""
    if not os.path.exists(".env"):
        print("✗ .env file not found")
        print("  → Copy .env.example to .env and add your API key")
        return False
    
    print("✓ .env file exists")
    
    with open(".env", "r") as f:
        content = f.read()
    
    if "your_openai_api_key_here" in content:
        print("✗ API key not configured (still has placeholder)")
        print("  → Edit .env and replace with your actual OpenAI API key")
        return False
    
    if "OPENAI_API_KEY=" in content and "sk-" in content:
        print("✓ API key appears to be configured")
        return True
    
    print("⚠ API key may not be configured correctly")
    return False


def main():
    """Run all verification checks."""
    print("="*60)
    print("OpenAI Agents SDK Jokester - Setup Verification")
    print("="*60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Environment Variables", check_env_file)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        results.append(check_func())
    
    print("\n" + "="*60)
    if all(results):
        print("✓ All checks passed! You're ready to run the agent.")
        print("\nRun: python jokester.py")
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        print("\nSee QUICKSTART.md for setup instructions.")
    print("="*60)


if __name__ == "__main__":
    main()
