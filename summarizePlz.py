import sys
import openai

def load_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def summarize_text(text, engine='text-davinci-003', max_tokens=100):
    """
    Summarizes the given text using OpenAI's GPT model.
    
    Parameters:
    - text (str): The text to be summarized.
    - engine (str): The OpenAI GPT engine to use.
    - max_tokens (int): The maximum number of tokens in the output.
    
    Returns:
    - str: The summarized text.
    """
    response = openai.Completion.create(
        engine=engine,
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python summarizePlz.py targetfile.txt")
        sys.exit(1)
    
    text_file_path = sys.argv[1]
    try:
        with open(text_file_path, 'r') as file:
            text_to_summarize = file.read()
    except FileNotFoundError:
        print(f"Error: The file {text_file_path} was not found.")
        sys.exit(1)

    # Load the API key from a file
    api_key_path = '../5560key'
    openai.api_key = load_api_key(api_key_path)
    
    # Summarize the text
    summary = summarize_text(text_to_summarize)
    print("Summary:", summary)

if __name__ == "__main__":
    main()