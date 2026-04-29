#!/usr/bin/env python3
"""Calculator Agent — a Claude-powered agent that performs mathematical calculations.

Usage:
    # Interactive mode
    python calculator_agent.py

    # Single query mode
    python calculator_agent.py "What is 15% of 840?"
"""

import sys
import anthropic
from calculator_tools import ALL_TOOLS

SYSTEM_PROMPT = """You are a precise and helpful calculator assistant powered by mathematical tools.
When the user asks you to compute something:
1. Break complex expressions into steps using the available tools.
2. Use multiple tool calls when needed (e.g., compute sub-expressions first).
3. Show the final answer clearly and explain the steps taken.
4. If a calculation is ambiguous, state your interpretation before computing.

You have access to: basic arithmetic, powers, roots, modulo, factorial,
logarithms (natural, base-10, custom base), trigonometry (degrees, including inverses),
absolute value, percentage helpers, rounding, GCD, LCM, and primality testing."""

client = anthropic.Anthropic()


def calculate(query: str) -> str:
    """Run the calculator agent on a query and return the final text response."""
    runner = client.beta.messages.tool_runner(
        model="claude-opus-4-7",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=ALL_TOOLS,
        messages=[{"role": "user", "content": query}],
    )

    final_message = None
    for message in runner:
        final_message = message

    if final_message is None:
        return "No response received."

    for block in final_message.content:
        if block.type == "text":
            return block.text

    return "Calculation complete."


def print_banner():
    print("╔══════════════════════════════════════════════════════╗")
    print("║          Calculator Agent  (powered by Claude)       ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  Supports: arithmetic · powers · roots · trig        ║")
    print("║            logs · factorial · GCD/LCM · percentages  ║")
    print("║  Type 'help' for examples  ·  'quit' to exit         ║")
    print("╚══════════════════════════════════════════════════════╝")


HELP_TEXT = """
Example queries:
  Basic          : 1234 × 5678
  Powers/roots   : What is the cube root of 512?
  Trig           : sin(30°) + cos(60°)
  Logarithms     : log base 2 of 1024
  Factorial      : 10!
  Percentages    : What is 17.5% of £240?
  Multi-step     : (√144 + 3²) × log₁₀(1000)
  Number theory  : Is 97 prime? / GCD of 48 and 36
  Rounding       : Round 3.14159 to 3 decimal places
"""


def interactive_loop():
    """Run an interactive REPL for the calculator agent."""
    print_banner()

    while True:
        try:
            query = input("\n▶  ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not query:
            continue

        lower = query.lower()
        if lower in ("quit", "exit", "q", "bye"):
            print("Bye!")
            break
        if lower in ("help", "?", "h"):
            print(HELP_TEXT)
            continue

        print()
        try:
            result = calculate(query)
            print(result)
        except anthropic.AuthenticationError:
            print("Error: Invalid ANTHROPIC_API_KEY. Check your .env file.")
            break
        except anthropic.RateLimitError:
            print("Error: Rate limit hit. Please wait a moment and try again.")
        except anthropic.APIError as e:
            print(f"API error: {e}")


def main():
    # If a query is passed on the command line, run in single-query mode.
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(calculate(query))
    else:
        interactive_loop()


if __name__ == "__main__":
    main()
