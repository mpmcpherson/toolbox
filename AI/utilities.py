from transformers import pipeline
from transformers import AutoTokenizer


def indexTokenizer(inputText):
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(inputText)
    return tokens


def import_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except IOError:
        print(f"Error reading file: {file_path}")
        return None


def get_sentiment_score(text):
    sentModel = "distilbert-base-uncased-finetuned-sst-2-english"
    # Initialize the sentiment analyzer
    sentiment_analyzer = pipeline("sentiment-analysis",
                                  model=sentModel)
    # Get the sentiment score of the input text
    sentiment_score = sentiment_analyzer(text)[0]
    return sentiment_score
