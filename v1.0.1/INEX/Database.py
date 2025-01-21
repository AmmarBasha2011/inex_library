import sqlite3

class Database:
    '''
    Class for creating and managing SQLite databases.

    Attributes:
    - connection: sqlite3 connection object
    - database_name: name of the database file

    Methods:
    - __init__: Initializes the database with a name and optional password.
    - create_table: Creates a table in the database with the given name and columns.
    - fetch: Fetches data from the database table based on the given conditions.

    Notes:
    - If the password is not provided, the database will not be encrypted.
    - The password should be kept confidential to ensure the security of the database.
    '''
    
    def __init__(self, database_name, password=None):
        '''
        Initializes the database with a name and optional password.

        Args:
        - database_name (str): Name of the database file.
        - password (str): Password for encrypting the database. If not provided, the database will not be encrypted.

        Returns:
        - A Database object.
        '''
        
        try:
            if password:
                self.connection = sqlite3.connect(f'{database_name}?key={password}', uri=True)
            else:
                self.connection = sqlite3.connect(database_name)
            self.connection.row_factory = sqlite3.Row
            self.database_name = database_name
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            self.connection = None
    
    def create_table(self, table_name, columns=[{"id": "INTEGER PRIMARY KEY AUTOINCREMENT"}]):
        '''
        Creates a table in the database with the given name and columns.

        Args:
        - table_name (str): Name of the table to create.
        - columns (list): List of dictionaries containing the column names and types. Each dictionary should have the column name as the key and the column type as the value.

        Returns:
        - True if the table was created successfully, False otherwise.

        Notes:
        - The table will be created with the given columns and an "id" column as the primary key with auto increment.
        - The columns should be a list of dictionaries, where each dictionary contains the column name and type.
        '''
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join([f"{column_name} {column_type}" for column_name, column_type in columns.items()])})')
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        
    def fetch(self, table_name, columns=["*"], where=[None], type="all"):
        '''
        Fetches data from the database table based on the given conditions.

        Args:
        - table_name (str): Name of the table to fetch from.
        - columns (list): List of column names to fetch. If not provided, all columns will be fetched.
        - where (list): List of conditions to filter the data. Each condition should be a string with the column name, operator, and value.
        - type (str): Type of fetch to perform. If "one", only one row will be fetched. If "all", all rows will be fetched.

        Returns:
        - If type is "one", a single row as a dictionary. If type is "all", a list of dictionaries containing all the rows.

        Notes:
        - The where parameter should be a list of strings with the column name, operator, and value.
        - The type parameter should be "one" or "all".
        '''
        
        try:
            if type == "one":
                cursor = self.connection.cursor()
                cursor.execute(f'SELECT {", ".join(columns)} FROM {table_name} WHERE {" AND ".join(where)}', (where[1],))
                return cursor.fetchone()
            elif type == "all":
                cursor = self.connection.cursor()
                cursor.execute(f'SELECT {", ".join(columns)} FROM {table_name} WHERE {" AND ".join(where)}', (where[1],))
                return cursor.fetchall()
            else:
                print("Invalid type")
                return []
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []