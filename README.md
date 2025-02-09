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

Before running the application, set your API keys as environment variables:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
export ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
export FIREWORKS_API_KEY="YOUR_FIREWORKS_API_KEY"
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

This `README.md` provides a comprehensive overview of your project, including installation and usage instructions, which should help users get started with your chatbot. Adjust the content as needed to better fit your project's specifics or any additional features you may have.
