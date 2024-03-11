import sqlite3
import re
from PySide6.QtWidgets import QApplication, QMessageBox

class DataBase:
    def __init__(self, name="banco_de_dados.db"):
        self.name = name
    
    def connecta(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print("Erro ao fechar conexão:", e)
    
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Usuário TEXT UNIQUE NOT NULL,
                    Senha TEXT NOT NULL,
                    Acesso TEXT NOT NULL,
                    Endereço TEXT,
                    CEP TEXT,
                    CPF TEXT,
                    Número TEXT,
                    Estado TEXT,
                    Email TEXT
                )
            """)
        except:
            pass

    def insert_user(self, nome, usuario, senha, acesso, endereco, cep, cpf, numero, estado, email):
        try:           
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users(Nome, Usuário, Senha, Acesso, Endereço, CEP, CPF, Número, Estado, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome, usuario, senha, acesso, endereco, cep, cpf, numero, estado, email))
            self.connection.commit()
            print("Usuário inserido com sucesso!")

        except Exception as e:
            print("Erro ao inserir usuário:", e)

    def check_user(self, usuario, senha):
        try:
            print("Verificando usuário e senha no banco de dados...")
            print("Usuário fornecido:", usuario)
            print("Senha fornecida:", senha)
            
            query = "SELECT Acesso FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"  # Comparação insensível a maiúsculas e minúsculas
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            print("Resultado da consulta:", result)
            if result:
                print("Usuário autenticado com sucesso")
                return result[0]  # Retorna o tipo de usuário
            else:
                return ""  # Retorna uma string vazia se as credenciais não corresponderem
        except Exception as e:
            print("Erro ao verificar usuário:", e)
            return ""

    def user_exists(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (usuario,))
            result = cursor.fetchone()
            return bool(result)  # Retorna True se o usuário existir, False caso contrário
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
            return False
    
    def insert_data(self, full_dataset):

        cursor = self.connection.cursor()

        campos_tabela = (
            'NFe','serie','data_emissao','chave','cnpj_emitente','nome_emitente',
             'valorNfe','itemNota','cod','qntd','descricao','unidade_medida','valorProd',
             'data_importacao','usuario','data_saida' )  
        qntd = ','.join(map(str, '?'*16))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES ({qntd})"""

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')

    def create_table_nfe(self):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Notas(

            NFe TEXT,
            serie TEXT,
            data_emissao TEXT,
            chave TEXT,
            cnpj_emitente TEXT,
            nome_emitente TEXT,                
            valorNfe TEXT,
            itemNota TEXT,
            cod TEXT,
            qntd TEXT,
            descricao TEXT,
            unidade_medida TEXT,
            valorProd TEXT,
            data_importacao TEXT,
            usuario TEXT,
            data_saida TEXT,
        
        PRIMARY KEY(Chave, Nfe, itemNota)                

            );

        """)

if __name__ == "__main__":
    db = DataBase()
    db.connecta()
    db.create_table_users()
    db.create_table_nfe()
    db.close_connection()
