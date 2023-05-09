import os
import os.path

class file_operations:

    def __init__(self, working_directory: str ="auto_gpt_workspace"):
        # Set a dedicated folder for file I/O
        self.working_directory = working_directory

        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)


    def safe_join(self, base: str, *paths: str):
        new_path = os.path.join(base, *paths)
        norm_new_path = os.path.normpath(new_path)

        if os.path.commonprefix([base, norm_new_path]) != base:
            raise ValueError("Attempted to access outside of working directory.")

        return norm_new_path


    def read_file(self, filename: str):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            with open(filepath, "r") as f:
                content = f.read()
            return content
        except Exception as e:
            return "Error: " + str(e)


    def write_to_file(self, filenam: str, text: str):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(filepath, "w") as f:
                f.write(text)
            return "File written to successfully."
        except Exception as e:
            return "Error: " + str(e)


    def append_to_file(self, filename: str, text: str):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            with open(filepath, "a") as f:
                f.write(text)
            return "Text appended successfully."
        except Exception as e:
            return "Error: " + str(e)


    def delete_file(self, filename: str):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            os.remove(filepath)
            return "File deleted successfully."
        except Exception as e:
            return "Error: " + str(e)

    def search_files(self, directory: str):
        found_files = []

        if directory == "" or directory == "/":
            search_directory = self.working_directory
        else:
            search_directory = self.safe_join(self.working_directory, directory)

        for root, _, files in os.walk(search_directory):
            for file in files:
                if file.startswith('.'):
                    continue
                relative_path = os.path.relpath(os.path.join(root, file), self.working_directory)
                found_files.append(relative_path)

        return found_files