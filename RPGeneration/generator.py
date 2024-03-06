import sys
from openai import OpenAI

def load_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def generate_rpg_content(content_type, engine='gpt-3.5-turbo-0125', max_tokens=150, temperature=0.7):
    """
    Generates RPG content based on the specified content type.
    
    Parameters:
    - content_type (str): The type of RPG content to generate ("adventure", "campaign", "NPC").
    - engine (str): The OpenAI GPT engine to use.
    - max_tokens (int): The maximum number of tokens in the output.
    - temperature (float): The randomness of the output.
    
    Returns:
    - str: The generated RPG content.
    """
    prompts = {
        "adventure": "Generate a brief outline for a fantasy adventure where the players must retrieve an ancient artifact from a ruined temple, guarded by a dragon. Include potential plot twists.",
        "campaign": "Create a description of a fantasy world which includes regular humans as well as many nonhuman species, focusing on the political intrigue and the role of magic.",
        "npc": "Describe an interesting NPC who can become either an ally or an adversary to the players, including motivations, strengths, and weaknesses."
    }

    if content_type not in prompts:
        return "Content type not found in prompts list. Please choose 'adventure', 'campaign', or 'NPC'."
    
    prompt = prompts[content_type]

    response = client.chat.completions.create(
    model=engine,
    messages=[{"role": "system", "content": "You are a helpful, creative assistant."},
            {"role":"user","content":prompt}]
    )
asd
    return response.choices[0].message.content.strip()

client = OpenAI(api_key=load_api_key('../../5560key'))

def main():   
     
    print("Welcome to RPG Content Generator!")
    loop = True
    choice_ary = {
        '1':'adventure',
        '2':'campaign',
        '3':'npc'
    }

    while(loop):

        print("What would you like to generate?")
        print("1. Adventure")
        print("2. Campaign")
        print("3. NPC")
        print("4. Quit")

        choice = input("Enter your choice (adventure, campaign, NPC, quit): ").lower()
        
        valid_choices = {"1","2","3"}
        if choice == "quit" or choice == "4":
            loop = False
            break
        if choice not in valid_choices:
            print("Invalid choice. Exiting program.")
            sys.exit(1)

        # Generate the RPG content
        content = generate_rpg_content(choice_ary[choice])
        print("\nGenerated Content:\n", content,"\n")

if __name__ == "__main__":
    main()
