# The code is written by Shibo Li, @Miqroera in Shanghai.
# Date: 2025-01-16

from openai import OpenAI
from .utils import log_to_file


def call_model_api(prompt, api_key, api_base, model, max_tokens=4096, temperature=0):
    """
    Call the language model API using the OpenAI Python library with a local Ollama backend.

    Parameters:
        prompt (str): The prompt to send to the language model.
        api_key (str): API key for authentication (can be 'ollama' for local services).
        api_base (str): The base URL for the API (e.g., http://localhost:11434/v1 for Ollama).
        model (str): The model name to use (e.g., qwen2.5-coder:7b-instruct).
        max_tokens (int): Maximum number of tokens in the response.
        temperature (float): The randomness of the output (default: 0.7).

    Returns:
        str: The generated content from the language model.
    """
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key, base_url=api_base)

        # Call the ChatCompletion API
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # Extract the generated content
        generated_content = response.choices[0].message.content

        # Log the result
        log_to_file("model.log", f"PROMPT:\n{prompt}\n\nRESPONSE:\n{generated_content}")
        return generated_content
    except Exception as e:
        error_message = f"Error calling model API: {e}"
        log_to_file("error.log", error_message)
        print(error_message)
        return None
