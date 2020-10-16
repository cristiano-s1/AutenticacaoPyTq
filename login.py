from PyQt5 import uic, QtWidgets
import sqlite3


def chama_segunda_tela():
    login_tela1.label_4.setText("")
    cadastrar.login = login_tela1.lineEdit.text()  # variavel usuario recebendo o valor digitado
    cadastrar.senha = login_tela1.lineEdit_2.text()  # variavel senha recebendo o valor digitado

    #  Condição para o login
    if cadastrar.login == 'admin' and cadastrar.senha == 'admin123':
        login_tela1.close()  # Fechar a primeira tela
        login_tela2.show()  # Chamar a segunda tela
    else:
        login_tela1.label_4.setText("Dados de login incorretos!")


# Sair da segunda tela
def logout():
    login_tela2.close()  # Fechar a segunda tela
    login_tela1.show()  # Chamar a primeira tela
    login_tela1.lineEdit.setText("")
    login_tela1.lineEdit_2.setText("")


# Abrir a tela cadastro
def abre_tela_cadastro():
    cadastro_tela.show()


# Cadastrar usuario
def cadastrar():
    nome = cadastro_tela.lineEdit.text()
    login = cadastro_tela.lineEdit_2.text()
    senha = cadastro_tela.lineEdit_3.text()
    c_senha = cadastro_tela.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')  # Criar banco de dados
            cursor = banco.cursor()  # Objeto para poder manipular as querys do banco de dados
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            cadastro_tela.label_3.setText("Usuario cadastrado com sucesso!")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        cadastro_tela.label_3.setText("As senhas digitadas estão diferentes")


# Chamando as funções
app = QtWidgets.QApplication([])
login_tela1 = uic.loadUi("login_tela1.ui")
login_tela2 = uic.loadUi("login_tela2.ui")
cadastro_tela = uic.loadUi("cadastro_tela.ui")
login_tela1.pushButton.clicked.connect(chama_segunda_tela)
login_tela2.pushButton.clicked.connect(logout)
login_tela1.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # setEchoMode é para esconder a senha digitada
login_tela1.pushButton_2.clicked.connect(abre_tela_cadastro)
cadastro_tela.pushButton.clicked.connect(cadastrar)

login_tela1.show()
app.exec()
