import networkx as nx
import matplotlib.pyplot as plt

def create_rpg_graph():
    # Create a graph
    G = nx.Graph()

    # Add nodes with the 'type' attribute (adventure, NPC, campaign)
    G.add_node("Campaign: Dragon's Doom", type='campaign')
    G.add_node("Adventure: The Cursed Cave", type='adventure')
    G.add_node("Adventure: The Lost City", type='adventure')
    G.add_node("NPC: Aldren the Wise", type='NPC')
    G.add_node("NPC: Miria the Brave", type='NPC')

    # Add edges to represent relationships
    G.add_edge("Campaign: Dragon's Doom", "Adventure: The Cursed Cave")
    G.add_edge("Campaign: Dragon's Doom", "Adventure: The Lost City")
    G.add_edge("Adventure: The Cursed Cave", "NPC: Aldren the Wise")
    G.add_edge("Adventure: The Lost City", "NPC: Miria the Brave")

    return G

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

# Create the RPG graph
G = create_rpg_graph()

# Draw the graph
draw_rpg_graph(G)
