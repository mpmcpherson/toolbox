if __name__ == "__main__":
    # Assuming you have classes ContentGenerator and ContentManager defined elsewhere
    content_generator = ContentGenerator(api_key="your_api_key")
    content_manager = ContentManager(storage_dir="your_storage_directory")
    ui = UserInterface(content_manager, content_generator)
    ui.start()
