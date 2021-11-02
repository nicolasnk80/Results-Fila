import sys
from PyQt5 import uic, QtWidgets
import data_base


class GUI:
    def salvar_dados(self):
        my_id = janela.lineEdit_3.text()
        senha = janela.lineEdit_4.text()

        if my_id and senha:
            if data_base.DataBaseUser().insert_into(nome=my_id, senha=senha):
                janela.label_7.setText("")
                janela.lineEdit_3.setText("")
                janela.lineEdit_4.setText("")
                self.tela_login()
            else:
                janela.label_7.setText("Ops, Informações Invalidas")
                janela.lineEdit_4.setText("")
        else:
            janela.label_7.setText("Ops, Informações Invalidas")
            janela.lineEdit_4.setText("")

    def tela_de_cadastro(self):
        janela.manager.setCurrentWidget(janela.sign_up)
        janela.lineEdit_3.setText("")
        janela.lineEdit_4.setText("")
        janela.lineEdit.setText("")
        janela.lineEdit_2.setText("")
        janela.label_7.setText("")

    def entrar(self):
        my_id = janela.lineEdit.text()
        senha = janela.lineEdit_2.text()

        if data_base.DataBaseUser().select_values(my_id, senha):
            self.nome = janela.lineEdit.text()
            janela.lineEdit.setText("")
            janela.lineEdit_2.setText("")
            janela.label_5.setText("")
            janela.manager.setCurrentWidget(janela.iniciar)
        else:
            janela.label_5.setText("Ops, ID ou senha invalido")
            janela.lineEdit_2.setText("")

    def tela_login(self):
        janela.label_5.setText("")
        janela.manager.setCurrentWidget(janela.login)

    def voltar_tela_login(self):
        janela.label_8.setText("")
        janela.manager.setCurrentWidget(janela.login)

    def iniciar(self):
        janela.label_8.setText(f"Atende {self.nome} está em atendimento!")


app = QtWidgets.QApplication([])
janela = uic.loadUi("gui.ui")

gui = GUI()


janela.pushButton_2.clicked.connect(gui.tela_de_cadastro)
janela.pushButton_4.clicked.connect(gui.salvar_dados)
janela.pushButton_3.clicked.connect(gui.voltar_tela_login)
janela.pushButton.clicked.connect(gui.entrar)
janela.pushButton_4.clicked.connect(gui.tela_login)
janela.pushButton_5.clicked.connect(gui.voltar_tela_login)
janela.pushButton_6.clicked.connect(gui.iniciar)


janela.show()
sys.exit(app.exec_())
