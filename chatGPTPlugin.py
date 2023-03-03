import sublime
import sublime_plugin
import openai
import os


# Set up OpenAI API credentials
openai.api_key = “fx-spPosFminXJDHVEFq98RG3OyoxSWWkEAvzMZCgzGXXljPIqK"


# Define the command for the plugin
class ChatGPTCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get the selected text
        selection = self.view.sel()[0]
        input_text = self.view.substr(selection).strip()

        # Generate a response to the selected text using the OpenAI API
        prompt = f"Conversation with ChatGPT:\nUser: {input_text}\nChatGPT:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip()

        # Insert the generated response below the selected text
        self.view.insert(edit, selection.end(), f"\nChatGPT: {message}")


# Define the key binding for the command
class ChatGPTKeyBinding(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key == "chat_gpt_enabled":
            return True
        return None

    def on_text_command(self, view, command_name, args):
        if command_name == "chat_gpt" and view.match_selector(view.sel()[0].a, "text"):
            return {"command": command_name, "args": args, "context": [{"key": "chat_gpt_enabled"}]}
        return None
