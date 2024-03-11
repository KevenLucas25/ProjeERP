import re
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication,QFileDialog, QMainWindow, QWidget, QMessageBox
from ui_login_2 import Ui_Login
from mane_python import Ui_MainWindow
from database import DataBase
import sys
from arquivo_xml import ReadXml



class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        if not self.txt_usuario.text() or not self.txt_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('ERRO')
            msg.setText("Por favor, insira o nome de usuário e senha")
            msg.exec()
            return

        self.users = DataBase()
        self.users.connecta()
        
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        
        tipo_usuario = self.users.check_user(usuario, senha)
        print("Tipo de usuário:", tipo_usuario)
        self.users.close_connection()
        if tipo_usuario:  
            print("Login bem sucedido!")
            self.w = MainWindow(tipo_usuario.lower())
            self.w.show()
            self.close()
        else:
            print("Login falhou!")
            if self.tentativas < 3:
                self.tentativas += 1
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f"Login ou senha incorretos \n\nTentativa: {self.tentativas} de 3")
                msg.exec()
            if self.tentativas == 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText("Número máximo de tentativas excedido. O aplicativo será encerrado.")
                msg.exec()
                sys.exit()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        print("Tipo de usuário recebido:",user)
    
        
        if user.lower() == "usuário" or user.lower() == "user":  # Verificando se o tipo de usuário é "Usuário" ou "user"
            self.btn_cadastro_usuario.setVisible(False)

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.home_pag))
        self.btn_verificar_estoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_estoque))
        self.btn_clientes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cliente))
        self.btn_cadastro_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuario))
        self.btn_configuracoes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_configuracoes))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_fazer_cadastro.clicked.connect(self.subscribe_user)

        #ARQUIVO XML
        self.btn_abrir_planilha.clicked.connect(self.open_path)
        self.btn_importar.clicked.connect(self.import_xml_files)

    def subscribe_user(self):
    # Verificar se todas as caixas de texto estão preenchidas
        if not all([self.txt_nome.text(), self.txt_usuario.text(), self.txt_senha.text(), 
                    self.txt_confirmar_senha.text(), self.txt_endereco.text(), self.txt_cep.text(), self.txt_cpf.text(), 
                    self.txt_numero.text(), self.txt_estado.text(), self.txt_email.text()]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos são obrigatórios.")
            msg.exec()
            return
        
        # Verificar se as senhas coincidem
        if self.txt_senha.text() != self.txt_confirmar_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("As senhas não são iguais")
            msg.exec()
            return
        if not self.is_valid_email(self.txt_email.text()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Erro')
            msg.setText("Por favor, insira um e-mail correto")
            msg.exec()
            return

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        senha = self.txt_senha.text()
        acesso = self.comboBox.currentText()
        endereco = self.txt_endereco.text()
        cep = self.txt_cep.text()
        cpf = self.txt_cpf.text()
        numero = self.txt_numero.text()
        estado = self.txt_estado.text()
        email = self.txt_email.text()

        db = DataBase()
        db.connecta()
        
        try:
            db.insert_user(nome, user, senha, acesso, endereco, cep, cpf, numero, estado, email)
            db.close_connection()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Usuário")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()
        except Exception as e:
            error_message = f"Erro ao cadastrar usuário: {str(e)}"
            QMessageBox.critical(None, "Erro", f"O  usuário {user} já está cadastrado no sistema")

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar_senha.setText("")
        self.txt_cpf.setText("")
        self.txt_email.setText("")
        self.txt_estado.setText("")
        self.txt_numero.setText("")
        self.txt_endereco.setText("")
        self.txt_cep.setText("")

    def is_valid_email(self, email):
        email = email.strip()
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$')
        return bool(email_pattern.match(email))
    
    def open_path(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Explorador de Arquivos", "/home", "Todos os Arquivos (*);;Arquivos XML (*.xml)")
        self.linha_de_abrir_planilha.setText(self.path)


    def import_xml_files(self):
        xml = ReadXml(self.txt_filtro.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.connecta()
        cont = 1

        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont+=1

        #ATUALIZA A TABELA

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("importação concluída!")
        msg.exec_()
        self.progressBar.setValue(0)
    















if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
