# from var_dump import var_dump
import mneumosyne
import utilities as u
import responses as r


memory = mneumosyne.LongTermMemory()


# Example usage:
user_input = "Can you explain the movie 'The Last Unicorn' to me?"
sentiment_score = u.get_sentiment_score(user_input)
print("Sentiment Score:", sentiment_score)

gpt3_response = r.generate_gpt3_response(user_input, sentiment_score)
# var_dump(gpt3_response)
print("GPT-3 Response:")
print(gpt3_response)
