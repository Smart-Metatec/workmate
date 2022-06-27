import sqlite3
import os
import sys
from cryptography.fernet import Fernet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from utils.globals import DB_PATH
from utils.encryption import Encryption
from database.tables import Tables

encryption = Encryption()

class Model:
    def __init__(self):
        self.db = sqlite3.connect(f"{DB_PATH}test.db")
        self.cur = self.db.cursor()
        self.create_table_names()
        self.create_tables()
        self.fill_defaults()
        

    def create_tables(self):      
        
        self.create_table("apps", Tables.apps)
        self.create_table("notes", Tables.notes)
        self.create_table("todos", Tables.todos)
        self.create_table("settings", Tables.settings)
        self.create_table("user", Tables.users)
        self.create_table("vault", Tables.vault)
        
    def create_table(self, tablename: str, fields: object):
        encrypted_table_name = encryption.encrypt(tablename)
        
        new_table = self.insert_table_name(encrypted_table_name)
        
        names = list(fields.keys())
        definitions = list(fields.values())
        
        table_definition = ""
        
        for i in range(len(names)):
            encrypted_name = encryption.encrypt(names[i])
            table_definition += f"[{encrypted_name}] {definitions[i]}"
            if i < len(names) - 1: table_definition += ",\n\t\t"

        table_query = f"""
            CREATE TABLE IF NOT EXISTS [{encrypted_table_name}](
                {table_definition}
            )
        """
        if new_table: self.cur.execute(table_query)

    def save(self, table, data):
        # Generate the question marks required
        values = ", ".join(list(map(lambda v: "?", data.keys())))
        
        # Get the encrypted names of the columns and table
        table_cols = self.get_encrypted_table_cols(table)
        encrypted_tablename = self.get_encrypted_table_name(table)
        
        field_name_list = []
        for name in list(data.keys()):
            # If the column exists in the table add the encrypted name to list
            if name in table_cols: 
                field_name_list.append(f"[{table_cols[name]}]")
            # Throw an error if an invalid column name was passed to this method
            else:
                raise Exception("Invalid colum name provided")
                
        # Create a string from the encrypted column names that will be used to reference the columns names 
        keys = ", ".join(field_name_list)
        
        # encrypt the data and add it to the list of data that must be added
        values_list = []
        for entry in data.values():
            values_list.append(f'{encryption.encrypt(entry)}')
        
        # Convert to tuple for proper sqlite handling
        values_list = tuple(values_list)
            
        query = f"INSERT INTO [{encrypted_tablename}]({keys}) VALUES ({values})"

        self.cur.executemany(query, [values_list])
        self.db.commit()
        self.db.close()
        
        

    def read(self, table):
        if table != "tablenames":
            encrypted_table = self.get_encrypted_table_name(table)
            
        query = f"SELECT * FROM [{encrypted_table}]"
        self.cur.execute(query)
        data = self.cur.fetchall()
        decrypted_data = []
        if table != "tablenames":
            for entry in data:
                entry_list = []
                for i in range(len(list(entry))):
                    if (table == "user" or table == "settings"):
                            decrypted = encryption.decrypt(entry[i])
                            entry_list.append(decrypted)
                    else:
                        if i > 0:
                            decrypted = encryption.decrypt(entry[i])
                            entry_list.append(decrypted)
                        else:
                            entry_list.append(entry[i])
                decrypted_data.append(entry_list)
            
        self.db.close()

        return decrypted_data

    def delete(self, table, id):
        encrypted_table = self.get_encrypted_table_name(table)
        
        encrypted_cols = self.get_encrypted_table_cols(table)
        # The id identifier is encrypted change this
        query = f"DELETE FROM [{encrypted_table}] WHERE [{encrypted_cols['id']}] = (?)"
        
        # print(query)
        self.cur.execute(query, (id,))
        self.db.commit()
        self.db.close()

    def update(self, table, data, id):
        # Get the field names
        fields = data.keys()
        # Get the encrypted cols
        encrypted_cols = self.get_encrypted_table_cols(table)
        
        # Create list of encrypted values and append id for query
        values = list(map(lambda v: encryption.encrypt(v), list(data.values())))
        values.append(id)
        
        # Create the data string that will set the data in the query
        data_string_list = []
        for field in fields:
            if field in encrypted_cols:
                data_string_list.append(f"[{encrypted_cols[field]}] = ?")
            else:
                raise Exception(" Invalid column name provided")
        data_string = ", ".join(data_string_list)
        
        # Get the encrypted table name
        encrypted_table = self.get_encrypted_table_name(table)
 
        query = f"UPDATE [{encrypted_table}] SET {data_string} WHERE [{encrypted_cols['id']}] = ?"

        self.cur.execute(query, values)
        self.db.commit()
        self.db.close()
    # Start fixing from here
    def clearTable(self, table):
        query = f"""
            DROP TABLE IF EXISTS {table}
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def reset(self):
        query = """
            UPDATE settings SET nightmode = 0, font = 'Arial', color = '#000000' WHERE id = 'settings'
        """

        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def start(self):
        settings = Model().read("settings")
        if len(settings) == 0:
            data = {
                'nightmode': 0,
                'font': "Arial",
                'color': "#000000"
            }
            self.save('settings', data)

    def add_column(self, table_name, column_name, column_definition):
        query = f"ALTER TABLE {table_name} ADD {column_name} {column_definition}"
        self.cur.execute(query)
    
    def drop_table(self, table):
        self.cur.execute(f"DROP TABLE {table}")
        
    def create_table_names(self):
        query = """CREATE TABLE IF NOT EXISTS tablenames(
                name TEXT NOT NULL
            )"""
        self.cur.execute(query)
        
    def insert_table_name(self, value: str):
        get_query = "SELECT * FROM tablenames"
        self.cur.execute(get_query)
        tables = self.cur.fetchall()
        
        for table in tables:
            existing_decrypted_table = encryption.decrypt(table[0])
            decrypted_table = encryption.decrypt(value)
            if existing_decrypted_table == decrypted_table:
                return False
        
        query = "INSERT INTO tablenames (name) VALUES (?)"
        self.cur.execute(query, (value,))
        self.db.commit()
        return True

    def get_encrypted_table_name(self, tablename):
        self.cur.execute("SELECT * FROM tablenames")
        tables = self.cur.fetchall()
        
        for table in tables:
            decrypted_table = encryption.decrypt(table[0])
            if tablename == decrypted_table:
                return table[0]
            
        return None
    
    # get a dict of the table names that map to the encrypted table names
    def get_encrypted_table_cols(self, table: str) -> object:
        decrypted_table = self.get_encrypted_table_name(table)
        
        query = f"SELECT * FROM [{decrypted_table}]"
        data = self.cur.execute(query)
        table_columns = {}
        
        for meta in data.description:
            name = encryption.decrypt(meta[0])
            table_columns[name] = meta[0]
            
        return table_columns
        
    
    def fill_defaults(self):
        enc = encryption.encrypt
        settings = self.get_encrypted_table_name("settings")
        
        get_query = f"SELECT * FROM [{settings}]"
        self.cur.execute(get_query)
        settings_data = self.cur.fetchall()
        
        if len(settings_data) < 1:
            query = f"INSERT INTO [{settings}] VALUES ('{enc('settings')}', '{enc('0')}', '{enc('Arial')}', '{enc('#000000')}', '{enc('0')}', '{enc('5')}', '{enc('0')}', '{enc('0')}')"
            self.cur.execute(query)
            self.db.commit()
        
model = Model()
settings = model.read("user")
# print(settings)
# model.save("apps", {"name": "another test", "path": "https://hello2.com", "sequence": "2"})

# model.update("apps", {"name": "changed name", "path": "https://hi.com"}, 1)
# model.delete("apps", 2)
# print(model.read("apps"))