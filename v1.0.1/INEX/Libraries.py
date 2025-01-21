import os

class Libraries:
    
    @staticmethod
    class Basic:
        
        def __init__(self):
            pass
        
        @staticmethod
        def init_creator(filesave="__init__.py", filename="", function_class=""):
            """
            Initializes a Python file with import statements.

            Args:
            - filesave: File path to save the initialization.
            - filename: Name of the Python file to import from.
            - function_class: Name of the function or class to import.

            Returns:
            - 'done' if successful.
            - Error message if unsuccessful.
            """
            if filename == "" or function_class == "" or filesave == "":
                return "FileSave or FileName or Function/Class Name is Not Found"
            
            try:
                if os.path.exists(filesave):
                    with open(filesave, "r") as f:
                        text = f.read()
                else:
                    text = ""

                text += f"\nfrom .{filename} import {function_class}\n"
                
                with open(filesave, "w") as f:
                    f.write(text)
                
                return 'done'
            except Exception as e:
                return str(e)

        @staticmethod
        def basic_setup_file_creator(filename="setup.py", folder_name="", readme_name="README.md", library_name="", library_version="", libraries_required=[], description="", creator_name="", creator_email="", License="MIT"):
            """
            Creates a basic setup.py file for a Python library.

            Args:
            - filename: Name of the setup file to create.
            - folder_name: Folder name (not used in function logic).
            - readme_name: Name of the README file.
            - library_name: Name of the Python library.
            - library_version: Version of the Python library.
            - libraries_required: List of required libraries.
            - description: Description of the Python library.
            - creator_name: Name of the library creator.
            - creator_email: Email of the library creator.
            - License: License type (default: MIT).

            Returns:
            - 'done' if successful.
            - 'FileName Found' if filename already exists.
            - Error message if unsuccessful.
            """
            if License == "MIT":
                libraries_required.append("YWP")
                file_data = (
                    "from setuptools import setup, find_packages\n\n"
                    f"setup(\nname='{library_name}',\nversion='{library_version}',\n"
                    f"packages=find_packages(),\ninstall_requires={str(libraries_required)},\n"
                    "classifiers=[\n'Programming Language :: Python :: 3',\n],\n"
                    "python_requires='>=3.6',\ndescription='" + description + "',\n"
                    f"long_description=open('{readme_name}').read(),\n"
                    "long_description_content_type='text/markdown',\n"
                    f"author='{creator_name}',\nauthor_email='{creator_email}',\n"
                    ")"
                )
                
                if os.path.exists(filename):
                    return 'FileName Found'
                
                try:
                    with open(filename, "w") as f:
                        f.write(file_data)
                    return 'done'
                except Exception as e:
                    return str(e)
            else:
                return 'Not From Licenses'

        @staticmethod
        def upload_file_creator(filename="upload_library", pypi_api="", platform="windows"):
            """
            Creates upload scripts for distributing a Python library.

            Args:
            - filename: Name of the upload script file.
            - pypi_api: PyPI API key or token.
            - platform: Platform to generate script for (windows or linux).

            Returns:
            - 'done' if successful.
            - 'FileName Found' if filename already exists.
            - 'Platform Not Supported' if platform is not windows or linux.
            - Error message if unsuccessful.
            """
            platforms = ["windows", "linux"]
            
            if platform in platforms:
                if platform == "windows":
                    filename += ".bat"
                    file_data = (
                        "set TWINE_USERNAME=__token__\n"
                        f"set TWINE_PASSWORD={pypi_api}\n"
                        "python setup.py sdist bdist_wheel\n"
                        "set TWINE_USERNAME=%TWINE_USERNAME% "
                        "set TWINE_PASSWORD=%TWINE_PASSWORD% "
                        "twine upload dist/*"
                    )
                elif platform == "linux":
                    filename += ".sh"
                    file_data = (
                        'export TWINE_USERNAME="__token__"\n'
                        f'export TWINE_PASSWORD="{pypi_api}"\n'
                        'python setup.py sdist bdist_wheel\n'
                        'TWINE_USERNAME="$TWINE_USERNAME" '
                        'TWINE_PASSWORD="$TWINE_PASSWORD" '
                        'twine upload dist/*'
                    )
                
                if os.path.exists(filename):
                    return 'FileName Found'
                
                try:
                    with open(filename, "w") as f:
                        f.write(file_data)
                    return 'done'
                except Exception as e:
                    return str(e)
            else:
                return 'Platform Not Supported'
