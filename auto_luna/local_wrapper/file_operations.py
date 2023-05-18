import os
import os.path


class file_operations:

    def __init__(self, working_directory="auto_gpt_workspace"):
        # Set a dedicated folder for file I/O
        self.working_directory = working_directory

        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)


    def safe_join(self, base, *paths):
        new_path = os.path.join(base, *paths)
        norm_new_path = os.path.normpath(new_path)

        if os.path.commonprefix([base, norm_new_path]) != base:
            raise ValueError("Attempted to access outside of working directory.")

        return norm_new_path


    def read_file(self, filename):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            with open(filepath, "r") as f:
                content = f.read()
            return content
        except Exception as e:
            return "Error: " + str(e)


    def write_to_file(self, filename, text):
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


    def append_to_file(self, filename, text):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            with open(filepath, "a") as f:
                f.write(text)
            return "Text appended successfully."
        except Exception as e:
            return "Error: " + str(e)


    def delete_file(self, filename):
        try:
            filepath = self.safe_join(self.working_directory, filename)
            os.remove(filepath)
            return "File deleted successfully."
        except Exception as e:
            return "Error: " + str(e)

    def search_files(self, directory):
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

    def get_luna_functions(self):

        return {"wrapper name":"file_operations","functions":[{"name":"safe_join", "description":"parameters: base - the base directory, paths - an additional directory; description: the function joins the given path components in a safe manner to prevent accessing files or directories outside the specified base directory.; return: unless an error is triggered the function returns the normalized new path","function":self.safe_join()}, {"name":"read_file", "description":"parameters: filename - the name of the file; description: The method first calls the 'safe_join' method to obtain the full path to the file, which ensures that the file is located within the working directory and prevents access to files outside of the working directory. It then opens the file in read mode and reads the contents of the file using the 'read' method.; return: If the file cannot be opened or read for any reason, the method returns an error message as a string.","function":self.read_file()}, {"name":"write_to_file", "description":"parameters: filename - the name of the file to write to, text - the text to write to the file; description: The 'write_to_file' method writes a given text to a file with the specified filename in the current working directory. If the file does not exist, the method creates a new file with the given filename. If the directory to write the file does not exist, it creates the directory. If the file already exists, the method overwrites its contents with the new text.; return: If the file was written to successfully, the method returns the string 'File written to successfully.', If an error occurred while writing to the file, the method returns a string containing an error message.","function":self.write_to_file()}, {"name":"append_to_file", "description":"parameters: filename - the name of the file to which 'text' will be appended to, text - the text appended to the file; description: This function appends the given 'text' to the end of the file with the given 'filename' in the working directory. If the file does not exist, it is created. If the file exists but is empty, the 'text' is written to the file as the first line. If the file exists and already has content, the 'text' is appended to the end of the file. The 'safe_join' method is used to ensure that the file is located within the working directory and not outside of it. If an error occurs during the file operation, the function returns an error message with the specific error details.; return: If the function is able to append 'text' to the file, the function returns the string 'Text appended successfully.'. If the function is not able to append 'text' to the file due to an error, the function returns the string 'Error:' followed by the error message as a string.","function":self.append_to_file()}, {"name":"delete_file", "description":"parameters: filename - The name of the file to be deleted; description: The 'delete_file' method takes a 'filename' string as input and attempts to delete the file with that name from the 'working_directory' attribute of the class instance. If successful, it returns a string message indicating that the file was deleted successfully. If unsuccessful, it returns a string message indicating the error encountered during the file deletion attempt.; return: A message indicating whether the file was deleted successfully or if an error occurred.","function":self.delete_file()}, {"name":"search_files", "description":"parameters: directory - parameter is an optional argument that specifies a subdirectory to search files in, relative to the working directory.; description: This method searches for files in a specified directory and returns a list of the relative paths to each file found.; return: a list of strings representing the relative paths to each file found in the directory and its subdirectories.","function":self.search_files()}]}