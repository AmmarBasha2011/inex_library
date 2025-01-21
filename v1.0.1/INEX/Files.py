import os
import subprocess

class Files:
    
    @staticmethod
    def delete_file(filepath):
        """
        Deletes a file if it exists.

        Args:
        - filepath: Path to the file to delete.

        Returns:
        - "Deleted" if file is successfully deleted.
        - Raises an exception if deletion fails.
        """
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                return "Deleted"
            except Exception as error:
                raise error

    @staticmethod
    def open_file(filepath=""):
        """
        Opens a file if it exists using subprocess.

        Args:
        - filepath: Path to the file to open.

        Returns:
        - "open" if file is successfully opened.
        - "Not Found Path" if file path does not exist.
        - "An error occurred" with the error message if an exception occurs.
        """
        try:
            if os.path.exists(filepath):
                subprocess.Popen([str(filepath)])
                return "open"
            else:
                return "Not Found Path"
        except Exception as e:
            print("An error occurred:", e)
            return "An error occurred:", e

    @staticmethod
    def create_file(name=""):
        """
        Creates a new file and writes user input into it.

        Args:
        - name: Name of the file to create.

        Returns:
        - "created" if file is successfully created and written to.
        - Raises an exception if creation fails.
        """
        print("Please enter the text or code (press Ctrl + D on Unix or Ctrl + Z then Enter on Windows to finish):")

        user_input_lines = []
        try:
            while True:
                line = input()
                user_input_lines.append(line)
        except EOFError:
            pass

        user_input = '\n'.join(user_input_lines)
        
        filename = name

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(user_input)
            return "created"
        except Exception as error:
            raise error

    @staticmethod
    def delete_all_files(directory=".", type={}):
        """
        Deletes files in a directory based on specified types.

        Args:
        - directory: Directory path where files are located.
        - type: Dictionary mapping index to file types to delete.

        Returns:
        - "Deleted" if files are successfully deleted.
        - Raises an exception if deletion fails.
        """
        
        for filename in os.listdir(directory):
            for index, filetype in type.items():
                if filename.endswith(filetype):
                    filepath = os.path.join(directory, filename)
                    try:
                        os.remove(filepath)
                    except Exception as error:
                        raise error
        return "Deleted"