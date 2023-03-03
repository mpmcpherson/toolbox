#!/bin/bash

# Set the path to the file to watch
FILE_TO_WATCH=/path/to/your/file.txt

# Set the endpoint URL for the ChatGPT API
CHATGPT_API_URL="https://api.openai.com/v1/engines/davinci-codex/completions"

# Set your OpenAI API key
OPENAI_API_KEY="your-api-key-here"

# Get the initial content of the file
initial_content=$(cat "$FILE_TO_WATCH")

# Start the file watcher loop
while true; do
  # Get the current content of the file
  current_content=$(cat "$FILE_TO_WATCH")

  # Check if the file has changed
  if [[ "$current_content" != "$initial_content" ]]; then
    # Submit the changed text to ChatGPT for a response
    response=$(curl -s -X POST "$CHATGPT_API_URL" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
          "prompt": "'"$current_content"'",
          "max_tokens": 128,
          "temperature": 0.5,
          "n": 1,
          "stop": "."
      }')

    # Extract the response text from the JSON response
    response_text=$(echo "$response" | jq -r '.choices[0].text')

    # Print the response text
    echo "$response_text"

    # Set the initial content of the file to the current content
    initial_content="$current_content"
  fi

  # Wait for 1 second before checking the file again
  sleep 1
done
