# AI Personal Finance Assistant (CLI)

A simple Python-based CLI tool that helps track daily expenses, analyze spending patterns, and generate AI-powered financial insights using LLaMA3 (Groq API).

## Why I built this

I built this project to understand my own spending habits and explore how AI can be used in simple real-world personal tools.

Most finance apps are either too complex or don’t give meaningful insights. I wanted something lightweight that:

- Tracks daily expenses easily
- Shows where money is actually going
- Gives clear, practical suggestions using AI

This project also helped me learn how to integrate AI into a Python application.

## How I built it

The project is built using a simple modular Python structure:

- A CLI takes daily expense input (category + amount)
- Data is stored locally using JSON
- A separate analysis module processes spending patterns
- AI (Groq LLaMA3) generates structured financial insights
- Output is displayed as a clean terminal report

Each part is separated into different files to keep the system simple and maintainable.

## What I used

- Python (core logic)
- JSON (local storage system)
- Groq API (LLaMA3 for AI insights)
- python-dotenv (secure API key handling)
- CLI (command-line interface)

## How to use it

Run the program:

```bash id="run_clean"
python main.py

## How it works

1. You enter your daily expense (category + amount)
2. The data is saved locally in a JSON file
3. The system analyzes total spending and category patterns
4. AI processes your financial behavior using Groq LLaMA3
5. A structured report is generated in the terminal

---

## Example Output

```text id="example_output"
Spending Overview
Total spent: Rs 2840

Category usage:
food: 2 times
icecream: 2 times

AI Insights:
- Food is your highest expense category
- Small repeated expenses are increasing total spending
- Spending is not strictly controlled

Advice:
- Reduce frequent eating out
- Track small expenses daily
- Set a monthly budget limit
