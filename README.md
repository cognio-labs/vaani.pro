# Vaani

Vaani is an agentic voice-enabled chatbot that leverages multiple language models to generate responses based on user queries. It supports various models from OpenAI, Anthropic, Google, and Fireworks.

## Features

- Supports multiple language models:
  - OpenAI's GPT-4o and GPT-3.5-turbo
  - Google's Gemini
  - Anthropic's Claude
  - Fireworks' Llama
- Configurable model selection
- Simple command-line interface for interaction

## Installation

To install the necessary dependencies, ensure you have Python 3.12 or higher, and then run:

```bash
pip install -r requirements.txt
```

Alternatively, if you are using Poetry, you can install the dependencies with:

```bash
poetry install
```

## Configuration

Before running the application, set your API keys in a `.env` file. You can use the provided `.env.example` as a template:

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Fill in your API keys in the `.env` file:

   ```plaintext
   OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
   ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"
   GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   FIREWORKS_API_KEY="YOUR_FIREWORKS_API_KEY"
   LANGCHAIN_API_KEY="YOUR_LANGCHAIN_API_KEY"
   ```

## Usage

To start the chatbot, run the following command:

```bash
python chat.py
```

You will be prompted to enter the model name and your query. The available models are:

- gpt-4o
- gpt-4o-mini
- gpt3-mini
- gemini-flash-2.0
- claude-3.5-haiku
- llama-3.3-70b

## Example

```plaintext
Available models: gpt-4o, gpt-4o-mini, gpt3-mini, gemini-flash-2.0, claude-3.5-haiku, llama-3.3-70b
Enter the model name: gpt-4o
Enter your query: What is the capital of France?
Response from gpt-4o: The capital of France is Paris.
```

## License

This project is licensed under a Private License. See the `pyproject.toml` for more details.

## Authors

- Ashutosh Upadhyay
- Shivam Upadhyay
- Cognio Labs

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

```