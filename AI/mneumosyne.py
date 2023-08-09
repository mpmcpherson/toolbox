import time
import difflib
import networkx as nx
import responses as r
import utilities as u
import tiktoken


class LongTermMemory:
    def __init__(self):
        # Initialize the Long-Term Memory, Topic Dictionary, and Memory Graph
        self.long_term_memory = {}
        self.topic_dictionary = {}
        self.memory_graph = nx.Graph()

    def store_memory(self, identifier, content, topic):
        # Store the memory in the long-term memory dictionary
        self.long_term_memory[identifier] = content

        # Create or update the topic in the topic dictionary
        if topic in self.topic_dictionary:
            self.topic_dictionary[topic].append(identifier)
        else:
            self.topic_dictionary[topic] = [identifier]

        # Add the memory as a node in the memory graph
        self.memory_graph.add_node(identifier, content=content, topic=topic)

    def create_relation(self, memory1, memory2, relation):
        # Add a relation between two memories as an edge in the memory graph
        self.memory_graph.add_edge(memory1, memory2, relation=relation)

    def find_similar_memories(self, query, threshold=0.7):
        # Use the difflib library to find similar
        # memories based on content similarity
        similar_memories = []
        for identifier, content in self.long_term_memory.items():
            sim_scr = difflib.SequenceMatcher(None, query, content).ratio()
            if sim_scr >= threshold:
                similar_memories.append(identifier)
        return similar_memories

    def retrieve_memories_by_topic(self, topic):
        # Retrieve all memories linked to a specific
        # topic from the topic dictionary
        return self.topic_dictionary.get(topic, [])

    def gpt3_response(self, prompt, context=None):
        # Generate the GPT-3 response using OpenAI API
        response = r.generate_gpt3_response(prompt,
                                            u.get_sentiment_score(prompt))

        return response['choices'][0]['text']

    def encode_memory(self, identifier, content, topic, response):
        # Store the input (content) as a memory
        self.store_memory(identifier, content, topic)
        # Store the GPT-3 response as a memory
        # with a relation to the input memory
        response_identifier = f"{identifier}_response"
        self.store_memory(response_identifier, response, topic)
        self.create_relation(identifier, response_identifier, "generated")


class ShortTermMemory:
    # Initialize an empty memory store to hold memory units
    memory_store = []

    def __init__(self):
        self.short_term_memory = {}
        self.topic_dictionary = {}
        self.memory_graph = nx.Graph()

    # Function to encode the input and create a memory unit
    def encode_input(self, input_text, context, emotional_content=None):
        # Get the current timestamp
        timestamp = int(time.time())

        # Create a memory unit dictionary
        memory_unit = {
            'content': input_text,
            'context': context,
            'timestamp': timestamp,
            'emotional_content': emotional_content
        }

        return memory_unit

    def index_memory_unit_by_token(self, memory_unit, token):
        related_memory_units = []
        # Iterate through the memory store to find related memory units
        for memory_unit in self.memory_store:
            if memory_unit['token'] == token:
                related_memory_units.append(memory_unit)

        return related_memory_units

    def get_related_memory_units(self, context):
        related_memory_units = []
        # Iterate through the memory store to find related memory units
        for memory_unit in self.memory_store:
            if context in memory_unit['context']:
                related_memory_units.append(memory_unit)

        return related_memory_units

    def count_tokens(self, memory_unit):
        encoder = tiktoken.encoding_for_model("text-davinci-002")
        return len(encoder.encode(memory_unit['content']))

    # Function to encode and index a discrete input
    def encode_and_index_input(self, input_text):
        # Encode the input and create a memory unit
        context = "this is where we put in the topic of the conversation"
        emotional_content = "and this is where we put the calculated emotion"

        memory_unit = self.encode_input(input_text, context, emotional_content)

        # Index the memory unit by individual tokens
        tokens = r.TikTokenTokenize(input_text)
        for token in tokens:
            self.index_memory_unit_by_token(memory_unit, token)

        # Add the memory unit to the memory store
        self.memory_store.append(memory_unit)

    # Function to re-encode the entire input based on
    # full experience, weighted by tokens
    def reencode_full_input(self, context):
        # Get the list of all memory units related
        # to the current full experience
        related_memory_units = self.get_related_memory_units(context)

        # Calculate weights for each memory unit based
        # on the number of tokens they indexed
        total_tokens = 0
        for memory_unit in related_memory_units:
            total_tokens += self.count_tokens(memory_unit)

        # Re-encode the entire input based on the related
        # memory units and their token weights
        full_experience = ""
        for memory_unit in related_memory_units:
            tokens = r.TikTokenTokenize(memory_unit)
            weight = len(tokens) / total_tokens
            weighted_content = memory_unit.content * weight
            full_experience += weighted_content

        return full_experience


# Example Usage:
ltm = LongTermMemory()

# Store an input as a memory and generate a response with GPT-3
input_memory_id = "memory1"
input_memory_content = "How does photosynthesis work?"
input_memory_topic = "science"
ltm.encode_memory(input_memory_id, input_memory_content,
                  input_memory_topic,
                  ltm.gpt3_response(input_memory_content))

# Retrieve the GPT-3 response memory based on the input memory
retrieved_memories = ltm.retrieve_memories_by_topic("science")
for memory_id in retrieved_memories:
    print(f"MemID: {memory_id}, Content: {ltm.long_term_memory[memory_id]}")
