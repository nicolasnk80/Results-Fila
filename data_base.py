import mysql.connector


class DataBaseUser:
    def __init__(self):
        self.banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="filas_results"
        )

        self.cursor = self.banco.cursor()

    def create_data_base(self):
        self.cursor.execute("CREATE DATABASE filas_results")

    def create_table(self):
        self.cursor.execute("CREATE TABLE data_user (user VARCHAR(255), senha VARCHAR(255))")

    def insert_into(self, nome, senha):
        try:
            self.cursor.execute(f'''SELECT user FROM data_user WHERE nome = {nome}''')
            return False
        except:
            try:
                self.cursor.execute(f"INSERT INTO data_user (user, senha) VALUES ('{nome}', '{senha}')")
                self.banco.commit()
                return True

            except mysql.connector.Error as erro:
                return False

    def select_values(self, nome="", senha=""):
        try:
            self.cursor.execute(f"SELECT senha FROM data_user WHERE user = '{nome}'")
            values = self.cursor.fetchall()[0][0]

            try:
                if senha == values:
                    return True

                else:
                    return False
            except:
                return False

        except:
            return False
