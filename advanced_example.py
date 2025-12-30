"""
Advanced OpenAI Agents SDK Example
Demonstrates additional features like custom parameters and error handling.
"""

import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace


async def advanced_jokester():
    """
    Advanced example with error handling and customization.
    """
    load_dotenv(override=True)
    
    try:
        # Create agent with more detailed instructions
        agent = Agent(
            name="ComedyExpert",
            instructions="""You are a professional comedian who specializes in tech humor.
            Your jokes should be:
            - Clever and witty
            - Accessible to both technical and non-technical audiences
            - Appropriate for all ages
            - About 2-3 sentences long""",
            model="gpt-4o-mini"
        )
        
        # Example 1: Technical joke
        print("\n" + "="*60)
        print("EXAMPLE 1: Technical Humor")
        print("="*60)
        
        with trace("Tech Joke"):
            result = await Runner.run(
                agent,
                "Tell me a joke about autonomous AI agents and debugging"
            )
            print(result.final_output)
        
        # Example 2: Pun-based joke
        print("\n" + "="*60)
        print("EXAMPLE 2: Pun-based Humor")
        print("="*60)
        
        with trace("Pun Joke"):
            result = await Runner.run(
                agent,
                "Tell me a pun about machine learning models"
            )
            print(result.final_output)
        
        # Example 3: Observational humor
        print("\n" + "="*60)
        print("EXAMPLE 3: Observational Humor")
        print("="*60)
        
        with trace("Observational Joke"):
            result = await Runner.run(
                agent,
                "Tell me an observational joke about AI developers"
            )
            print(result.final_output)
        
        print("\n" + "="*60)
        print("View all traces at: https://platform.openai.com/traces")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Make sure your OPENAI_API_KEY is set in the .env file")


async def custom_agent_example():
    """
    Example of creating different types of agents.
    """
    load_dotenv(override=True)
    
    # Create multiple agents for different purposes
    agents = {
        "Poet": Agent(
            name="Poet",
            instructions="You write short, beautiful haikus about technology",
            model="gpt-4o-mini"
        ),
        "Explainer": Agent(
            name="Explainer",
            instructions="You explain complex AI concepts in simple terms",
            model="gpt-4o-mini"
        ),
        "Critic": Agent(
            name="Critic",
            instructions="You provide constructive feedback on ideas",
            model="gpt-4o-mini"
        )
    }
    
    print("\n" + "="*60)
    print("MULTIPLE AGENTS DEMO")
    print("="*60)
    
    for name, agent in agents.items():
        print(f"\n--- {name} ---")
        with trace(f"{name} Response"):
            if name == "Poet":
                result = await Runner.run(agent, "Write about AI agents")
            elif name == "Explainer":
                result = await Runner.run(agent, "What is an AI agent?")
            else:
                result = await Runner.run(agent, "Is building AI agents a good idea?")
            print(result.final_output)


async def main():
    """
    Main function to run all examples.
    """
    print("="*60)
    print("ADVANCED OPENAI AGENTS SDK EXAMPLES")
    print("="*60)
    
    # Run advanced jokester
    await advanced_jokester()
    
    # Uncomment to run custom agent examples
    # await custom_agent_example()


if __name__ == "__main__":
    asyncio.run(main())
