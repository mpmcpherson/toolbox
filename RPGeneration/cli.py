import os
import networkx as nx
import matplotlib.pyplot as plt
import json
import ContentManager

class UserInterface:
    def __init__(self, content_manager, content_generator):
        self.content_manager = content_manager
        self.content_generator = content_generator

    def start(self):
        print("Welcome to the RPG Content Management System!")
        while True:
            print("\nOptions:")
            print("1. Generate New Adventure")
            print("2. View Existing Adventures")
            print("3. Edit Adventure")
            print("4. Delete Adventure")
            print("5. Generate and Display Graph")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.generate_new_adventure()
            elif choice == '2':
                self.view_adventures()
            elif choice == '3':
                self.edit_adventure()
            elif choice == '4':
                self.delete_adventure()
            elif choice == '5':
                self.cli_generate_graph_option()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def generate_new_adventure(self):
        # Placeholder for function to generate new adventure
        title = input("Enter title for the new adventure: ")
        description = self.content_generator.generate_content(f"Generate a brief adventure titled '{title}'")
        print(f"Generated Adventure: {description}")
        # Here, you would call the content_generator to generate an adventure and then save it using content_manager

    def view_adventures(self):
        # Placeholder for function to list existing adventures
        print("Listing adventures...")
        # Here, you would list adventures stored by the content_manager

    def edit_adventure(self):
        # Placeholder for function to edit an existing adventure
        print("Editing adventure...")
        # Here, you would allow the user to select and edit an adventure

    def delete_adventure(self):
        # Placeholder for function to delete an existing adventure
        print("Deleting adventure...")
        # Here, you would allow the user to select and delete an adventure

    def cli_generate_graph_option():
        # This is where you integrate the new option in your existing CLI structure
        print("Generating RPG Graph...")
        json_data = read_json_file('your_data_file.json')  # Specify your JSON data file
        G = ContentManager.build_graph_from_json(json_data)
        draw_rpg_graph(G)  # Assuming you have a draw_rpg_graph function as previously discussed



def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def generate_graph_from_json(data_dir):
    G = nx.Graph()
    
    # Assuming a directory structure: data_dir/type/id.json
    for content_type in ['campaigns', 'adventures', 'npcs']:
        content_dir = os.path.join(data_dir, content_type)
        for file_name in os.listdir(content_dir):
            file_path = os.path.join(content_dir, file_name)
            content_data = read_json_file(file_path)
            
            # Add nodes and relationships based on content type
            if content_type == 'campaigns':
                G.add_node(content_data['title'], type='campaign')
                for adventure_id in content_data['adventures']:
                    adventure_data = read_json_file(os.path.join(data_dir, 'adventures', f"{adventure_id}.json"))
                    G.add_node(adventure_data['title'], type='adventure')
                    G.add_edge(content_data['title'], adventure_data['title'])
            elif content_type == 'adventures':
                for npc_id in content_data.get('npcs', []):
                    npc_data = read_json_file(os.path.join(data_dir, 'npcs', f"{npc_id}.json"))
                    G.add_node(npc_data['name'], type='NPC')
                    G.add_edge(content_data['title'], npc_data['name'])
                    
    # Visualization (similar to the previous example)
    draw_rpg_graph(G)

def draw_rpg_graph(G):
    # Position nodes using the spring layout
    pos = nx.spring_layout(G)

    # Draw nodes with different shapes based on their 'type'
    nx.draw_networkx_nodes(G, pos, node_size=1000,
                           nodelist=[n for n in G.nodes if G.nodes[n]['type'] == 'campaign'],
                           node_color='lightblue', node_shape='s', label='Campaign')
    nx.draw_networkx_nodes(G, pos, node_size=750,
                           nodelist=[n for n in G.nodes if G.nodes[n]['type'] == 'adventure'],
                           node_color='lightgreen', node_shape='o', label='Adventure')
    nx.draw_networkx_nodes(G, pos, node_size=500,
                           nodelist=[n for n in G.nodes if G.nodes[n]['type'] == 'NPC'],
                           node_color='salmon', node_shape='^', label='NPC')

    # Draw edges and labels
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Show legend and plot
    plt.legend(scatterpoints=1)
    plt.axis('off')
    plt.show()