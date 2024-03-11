# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maine2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1794, 996)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_verificar_estoque = QPushButton(self.frame)
        self.btn_verificar_estoque.setObjectName(u"btn_verificar_estoque")
        self.btn_verificar_estoque.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_verificar_estoque)

        self.btn_clientes = QPushButton(self.frame)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_clientes)

        self.btn_cadastro_usuario = QPushButton(self.frame)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
        self.btn_cadastro_usuario.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_cadastro_usuario)

        self.btn_configuracoes = QPushButton(self.frame)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        self.btn_configuracoes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_configuracoes)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_contato)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.home_pag = QWidget()
        self.home_pag.setObjectName(u"home_pag")
        self.verticalLayout_5 = QVBoxLayout(self.home_pag)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.home_pag)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 400, 651, 391))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_imagem = QLabel(self.frame_5)
        self.label_imagem.setObjectName(u"label_imagem")
        self.label_imagem.setGeometry(QRect(540, 60, 351, 321))
        self.label_imagem.setPixmap(QPixmap(u"sistema-de-gerenciamento-de-conteudo.png"))
        self.label_imagem.setScaledContents(True)
        self.label_bem_vindo = QLabel(self.frame_5)
        self.label_bem_vindo.setObjectName(u"label_bem_vindo")
        self.label_bem_vindo.setGeometry(QRect(520, 470, 331, 61))
        self.label_bem_vindo.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.frame_5)

        self.Pages.addWidget(self.home_pag)
        self.page_estoque = QWidget()
        self.page_estoque.setObjectName(u"page_estoque")
        self.horizontalLayout_7 = QHBoxLayout(self.page_estoque)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tb_base = QTabWidget(self.page_estoque)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.tables_estoque = QWidget()
        self.tables_estoque.setObjectName(u"tables_estoque")
        self.verticalLayout_3 = QVBoxLayout(self.tables_estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.linha_de_abrir_planilha = QLineEdit(self.tables_estoque)
        self.linha_de_abrir_planilha.setObjectName(u"linha_de_abrir_planilha")
        self.linha_de_abrir_planilha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.linha_de_abrir_planilha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.linha_de_abrir_planilha)

        self.btn_abrir_planilha = QPushButton(self.tables_estoque)
        self.btn_abrir_planilha.setObjectName(u"btn_abrir_planilha")
        self.btn_abrir_planilha.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_abrir_planilha)

        self.label_estoque = QLabel(self.tables_estoque)
        self.label_estoque.setObjectName(u"label_estoque")
        self.label_estoque.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_estoque)

        self.tabela_estoque = QTreeWidget(self.tables_estoque)
        self.tabela_estoque.setObjectName(u"tabela_estoque")

        self.verticalLayout_3.addWidget(self.tabela_estoque)

        self.frame_3 = QFrame(self.tables_estoque)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_importar = QPushButton(self.frame_3)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_importar)

        self.btn_gerar_saida = QPushButton(self.frame_3)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        self.btn_gerar_saida.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_gerar_saida)

        self.btn_estorno = QPushButton(self.frame_3)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_estorno)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.label_saida = QLabel(self.tables_estoque)
        self.label_saida.setObjectName(u"label_saida")
        self.label_saida.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_saida)

        self.tabela_saida = QTreeWidget(self.tables_estoque)
        self.tabela_saida.setObjectName(u"tabela_saida")

        self.verticalLayout_3.addWidget(self.tabela_saida)

        self.tb_base.addTab(self.tables_estoque, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.label_estoque_2 = QLabel(self.tab_2)
        self.label_estoque_2.setObjectName(u"label_estoque_2")
        self.label_estoque_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.label_estoque_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_grafico)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_excel)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_filtro)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_4 = QSpacerItem(100, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.tb_base.addTab(self.tab_2, "")

        self.horizontalLayout_7.addWidget(self.tb_base)

        self.Pages.addWidget(self.page_estoque)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        self.label_cliente = QLabel(self.pg_cliente)
        self.label_cliente.setObjectName(u"label_cliente")
        self.label_cliente.setGeometry(QRect(370, 340, 47, 13))
        self.Pages.addWidget(self.pg_cliente)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        self.pg_cadastro_usuario.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_tela = QLabel(self.pg_cadastro_usuario)
        self.label_tela.setObjectName(u"label_tela")
        self.label_tela.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label_tela)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.label_cadastro = QLabel(self.pg_cadastro_usuario)
        self.label_cadastro.setObjectName(u"label_cadastro")
        self.label_cadastro.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label_cadastro)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.txt_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.txt_usuario, 0, 4, 1, 1)

        self.txt_nome = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.txt_nome, 0, 2, 1, 1)

        self.label_nome = QLabel(self.pg_cadastro_usuario)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout.addWidget(self.label_nome, 0, 1, 1, 1)

        self.label_usuario = QLabel(self.pg_cadastro_usuario)
        self.label_usuario.setObjectName(u"label_usuario")

        self.gridLayout.addWidget(self.label_usuario, 0, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cpf = QLabel(self.pg_cadastro_usuario)
        self.label_cpf.setObjectName(u"label_cpf")

        self.horizontalLayout_3.addWidget(self.label_cpf)

        self.txt_cpf = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_cpf)

        self.label_endereco = QLabel(self.pg_cadastro_usuario)
        self.label_endereco.setObjectName(u"label_endereco")

        self.horizontalLayout_3.addWidget(self.label_endereco)

        self.txt_endereco = QLineEdit(self.pg_cadastro_usuario)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_endereco)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_email = QLabel(self.pg_cadastro_usuario)
        self.label_email.setObjectName(u"label_email")

        self.horizontalLayout_5.addWidget(self.label_email)

        self.txt_email = QLineEdit(self.pg_cadastro_usuario)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.txt_email)

        self.label_estado = QLabel(self.pg_cadastro_usuario)
        self.label_estado.setObjectName(u"label_estado")

        self.horizontalLayout_5.addWidget(self.label_estado)

        self.txt_estado = QLineEdit(self.pg_cadastro_usuario)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.txt_estado)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_numero = QLabel(self.pg_cadastro_usuario)
        self.label_numero.setObjectName(u"label_numero")

        self.horizontalLayout_6.addWidget(self.label_numero)

        self.txt_numero = QLineEdit(self.pg_cadastro_usuario)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_numero)

        self.label_cep = QLabel(self.pg_cadastro_usuario)
        self.label_cep.setObjectName(u"label_cep")

        self.horizontalLayout_6.addWidget(self.label_cep)

        self.txt_cep = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_cep)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_senha = QLabel(self.pg_cadastro_usuario)
        self.label_senha.setObjectName(u"label_senha")

        self.horizontalLayout_9.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_senha)

        self.label_confirmar_senha = QLabel(self.pg_cadastro_usuario)
        self.label_confirmar_senha.setObjectName(u"label_confirmar_senha")

        self.horizontalLayout_9.addWidget(self.label_confirmar_senha)

        self.txt_confirmar_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_confirmar_senha)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_perfil = QLabel(self.pg_cadastro_usuario)
        self.label_perfil.setObjectName(u"label_perfil")
        self.label_perfil.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.label_perfil)

        self.comboBox = QComboBox(self.pg_cadastro_usuario)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #999;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    selection-background-color: #ddd;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px; /* Aumenta a largura do bot\u00e3o de dropdown */\n"
"    border-left: 1px solid #999; /* Adiciona uma borda \u00e0 esquerda do bot\u00e3o de dropdown */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #eee, stop:1 #ddd);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png); /* \u00cdcone do bot\u00e3o de dropdown */\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.btn_fazer_cadastro = QPushButton(self.pg_cadastro_usuario)
        self.btn_fazer_cadastro.setObjectName(u"btn_fazer_cadastro")
        self.btn_fazer_cadastro.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.btn_fazer_cadastro)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pag_sobre = QLabel(self.pg_sobre)
        self.pag_sobre.setObjectName(u"pag_sobre")
        self.pag_sobre.setGeometry(QRect(300, 160, 181, 131))
        self.Pages.addWidget(self.pg_sobre)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        self.label_configuracoes = QLabel(self.pg_configuracoes)
        self.label_configuracoes.setObjectName(u"label_configuracoes")
        self.label_configuracoes.setGeometry(QRect(310, 230, 291, 161))
        self.Pages.addWidget(self.pg_configuracoes)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-240, -260, 1911, 1251))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_informacoes = QLabel(self.frame_4)
        self.label_informacoes.setObjectName(u"label_informacoes")
        self.label_informacoes.setGeometry(QRect(850, 330, 371, 281))
        self.label_informacoes.setScaledContents(False)
        self.label_informacoes.setAlignment(Qt.AlignCenter)
        self.Pages.addWidget(self.pg_contato)

        self.gridLayout_2.addWidget(self.Pages, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tb_base.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_verificar_estoque.setText(QCoreApplication.translate("MainWindow", u"Verificar estoque", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\"><br/>SISTEMA DE GERENCIAMENTO </span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\">DO CONTROLE DE ESTOQUE</span></p></body></html>", None))
        self.label_imagem.setText("")
        self.label_bem_vindo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\">Bem vindo(a) ao</span></p></body></html>", None))
        self.linha_de_abrir_planilha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"O arquivo excel aparecer\u00e1 aqui", None))
        self.btn_abrir_planilha.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.label_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tabela_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor NFE", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Esp\u00e9cie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFE", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.label_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tabela_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFE", None));
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables_estoque), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_estoque_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_cliente.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_tela.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">TELA PARA CADASTRAMENTO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO:", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-MAIL:", None))
        self.label_estado.setText(QCoreApplication.translate("MainWindow", u"ESTADO:", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO:", None))
        self.label_cep.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"SENHA:", None))
        self.label_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR SENHA:", None))
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"PERFIL:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.btn_fazer_cadastro.setText(QCoreApplication.translate("MainWindow", u"Fazer Cadastro", None))
        self.pag_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">SOBRE</span></p></body></html>", None))
        self.label_configuracoes.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        self.label_informacoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#000000;\">DESENVOLVIDO E PUBLICADO POR:</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#0000ff;\">KEVEN LUCAS</span></p></body></html>", None))
    # retranslateUi

