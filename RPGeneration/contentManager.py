import json
import os
import networkx as nx

class ContentManager:
    def __init__(self, storage_dir='content_storage'):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def save_content(self, content_type, content_id, content_data):
        """Save content to a JSON file."""
        filepath = self._get_filepath(content_type, content_id)
        with open(filepath, 'w') as file:
            json.dump(content_data, file)

    def read_content(self, content_type, content_id):
        """Read content from a JSON file."""
        filepath = self._get_filepath(content_type, content_id)
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return json.load(file)
        return None

    def update_content(self, content_type, content_id, new_content_data):
        """Update existing content."""
        self.save_content(content_type, content_id, new_content_data)

    def delete_content(self, content_type, content_id):
        """Delete content file."""
        filepath = self._get_filepath(content_type, content_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def _get_filepath(self, content_type, content_id):
        """Construct the file path for content."""
        filename = f"{content_id}.json"
        return os.path.join(self.storage_dir, content_type, filename)
    
    def build_graph_from_json(data):
        G = nx.Graph()
        
        for item in data:
            # Assuming 'type' and 'id' are fields in your JSON data
            G.add_node(item['id'], type=item['type'])
            
            # Assuming 'relations' is a list of IDs this item is related to
            for related_id in item.get('relations', []):
                G.add_edge(item['id'], related_id)
        
        return G

# Example usage
if __name__ == "__main__":
    cmm = ContentManager()

    # Example content
    adventure = {
        'title': 'The Lost Dungeon of Rokak',
        'description': 'A perilous journey into the heart of the ancient Rokak dungeon.',
        'objectives': ['Find the ancient artifact', 'Defeat the dungeon guardian'],
    }

    # Saving an adventure
    cmm.save_content('adventures', 'adventure1', adventure)

    # Reading the saved adventure
    loaded_adventure = cmm.read_content('adventures', 'adventure1')
    print(loaded_adventure)

    # Updating the adventure
    adventure['objectives'].append('Escape the dungeon')
    cmm.update_content('adventures', 'adventure1', adventure)

    # Deleting the adventure
    # cmm.delete_content('adventures', 'adventure1')
