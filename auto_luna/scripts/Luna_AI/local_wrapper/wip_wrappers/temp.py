def google(self):
            
            # Check if the Google API key is set and use the official search method
            # If the API key is not set or has only whitespaces, use the unofficial search method
            if cfg.google_api_key and (cfg.google_api_key.strip() if cfg.google_api_key else None):
                google_official_search(arguments["input"])
            else:
                google_search(arguments["input"])
        def memory_add(self):
            memory.add(arguments["string"])
        def start_agent(self):
            start_agent(
                arguments["name"],
                arguments["task"],
                arguments["prompt"])
        def message_agent(self):
            message_agent(arguments["key"], arguments["message"])
        def list_agents(self):
            list_agents()
        def delete_agent(self):
            delete_agent(arguments["key"])
        def get_text_summary(self):
            get_text_summary(arguments["url"], arguments["question"])
        def get_hyperlinks(self):
            get_hyperlinks(arguments["url"])
        def read_file(self):
            read_file(arguments["file"])
        def write_to_file(self):
            write_to_file(arguments["file"], arguments["text"])
        def append_to_file(self):
            append_to_file(arguments["file"], arguments["text"])
        def delete_file(self):
            delete_file(arguments["file"])
        def search_files(self):
            search_files(arguments["directory"])
        def browse_website(self):
            browse_website(arguments["url"], arguments["question"])
        # TODO: Change these to take in a file rather than pasted code, if
        # non-file is given, instructions "Input should be a python
        # filepath, write your code to file and try again"
        def evaluate_code(self):
            ai.evaluate_code(arguments["code"])
        def improve_code(self):
            ai.improve_code(arguments["suggestions"], arguments["code"])
        def write_tests(self):
            ai.write_tests(arguments["code"], arguments.get("focus"))
        def execute_python_file(self):  # Add this command
            execute_python_file(arguments["file"])
        def generate_image(self):
            generate_image(arguments["prompt"])
        def task_complete(self):
            shutdown()def google(self):
            
                google_official_search(arguments["input"])
            else:
                google_search(arguments["input"])
        def memory_add(self):
            memory.add(arguments["string"])
        def start_agent(self):
            start_agent(
                arguments["name"],
                arguments["task"],
                arguments["prompt"])
        def message_agent(self):
            message_agent(arguments["key"], arguments["message"])
        def list_agents(self):
            list_agents()
        def delete_agent(self):
            delete_agent(arguments["key"])
        def get_text_summary(self):
            get_text_summary(arguments["url"], arguments["question"])
        def get_hyperlinks(self):
            get_hyperlinks(arguments["url"])
        def read_file(self):
            read_file(arguments["file"])
        def write_to_file(self):
            write_to_file(arguments["file"], arguments["text"])
        def append_to_file(self):
            append_to_file(arguments["file"], arguments["text"])
        def delete_file(self):
            delete_file(arguments["file"])
        def search_files(self):
            search_files(arguments["directory"])
        def browse_website(self):
            browse_website(arguments["url"], arguments["question"])
        # TODO: Change these to take in a file rather than pasted code, if
        # non-file is given, instructions "Input should be a python
        # filepath, write your code to file and try again"
        def evaluate_code(self):
            ai.evaluate_code(arguments["code"])
        def improve_code(self):
            ai.improve_code(arguments["suggestions"], arguments["code"])
        def write_tests(self):
            ai.write_tests(arguments["code"], arguments.get("focus"))
        def execute_python_file(self):  # Add this command
            execute_python_file(arguments["file"])
        def generate_image(self):
            generate_image(arguments["prompt"])
        def task_complete(self):
            shutdown()