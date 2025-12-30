"""
OpenAI Agents SDK Jokester
A simple demonstration of the OpenAI Agents SDK for creating AI agents.
"""

import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace


async def main():
    """
    Main function to create and run a joke-telling agent.
    
    This demonstrates the core functionality of the OpenAI Agents SDK:
    - Creating an agent with name, instructions, and model
    - Running the agent with a prompt using Runner
    - Using trace for observability
    """
    # Load environment variables
    load_dotenv(override=True)
    
    # Create an agent with name, instructions, and model
    agent = Agent(
        name="Jokester",
        instructions="You are a joke teller",
        model="gpt-4o-mini"
    )
    
    # Run the agent with tracing enabled
    with trace("Telling a joke"):
        result = await Runner.run(
            agent,
            "Tell a joke about Autonomous AI Agents"
        )
        print("\n" + "="*50)
        print("JOKE OUTPUT:")
        print("="*50)
        print(result.final_output)
        print("="*50 + "\n")
        print("View the trace at: https://platform.openai.com/traces")


if __name__ == "__main__":
    asyncio.run(main())
