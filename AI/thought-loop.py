import openai
import responses as r
import utilities as u


openAPIKey = u.import_text_file("../../openapikey.txt")
# Replace 'YOUR_OPENAI_API_KEY' with your actual API key from OpenAI
openai.api_key = openAPIKey


# GPT instances representing different expertise
language_instance = "text-davinci-002"       # For processing text inputs
speech_instance = "text-davinci-003"         # For processing audio inputs

# Context to hold shared information across GPT instances
context = []


# Function to process text input using the appropriate GPT instance
def process_input(input_text):
    if input_text.startswith("[AUDIO]"):
        instance = speech_instance
        # Remove the [AUDIO] prefix from audio input
        input_text = input_text[7:]
    else:
        instance = language_instance

    response = r.generate_gpt3_response(input_text,
                                        u.get_sentiment_score(input_text))

    openai.Completion.create(
        engine=instance,
        prompt=input_text,
        context=context,
        max_tokens=100  # Adjust max_tokens as needed
    )

    # Update the context with the response to maintain continuity
    context.append(response.choices[0].text.strip())

    return response.choices[0].text.strip()


# Main loop for the AI to continuously listen and respond
while True:
    user_input = input("User: ")
    response = process_input(user_input)
    print("AI:", response)
