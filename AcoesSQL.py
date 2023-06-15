import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Cria campos de entrada
        self.ativo_label = QLabel("Nome do Ativo:")
        self.ativo_input = QLineEdit()
        self.data_compra_label = QLabel("Data da Compra:")
        self.data_compra_input = QLineEdit()
        self.quantidadeCompra_label = QLabel("Quantidade de Compra")
        self.quantidadeCompra_input = QLineEdit()
        self.valor_compra_label = QLabel("Valor da Compra:")
        self.valor_compra_input = QLineEdit()
        self.quantidadeVenda_label = QLabel("Quantidade de Venda")
        self.quantidadeVenda_input = QLineEdit()
        self.data_venda_label = QLabel("Data da Venda:")
        self.data_venda_input = QLineEdit()
        self.valor_venda_label = QLabel("Valor da Venda:")
        self.valor_venda_input = QLineEdit()

        # Cria botão de salvar
        self.salvar_button = QPushButton("Salvar")
        self.salvar_button.clicked.connect(self.salvar_dados)

        # layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.ativo_label)
        layout.addWidget(self.ativo_input)
        layout.addWidget(self.data_compra_label)
        layout.addWidget(self.data_compra_input)
        layout.addWidget(self.quantidadeCompra_label)
        layout.addWidget(self.quantidadeCompra_input)
        layout.addWidget(self.valor_compra_label)
        layout.addWidget(self.valor_compra_input)
        layout.addWidget(self.quantidadeVenda_label)
        layout.addWidget(self.quantidadeVenda_input)
        layout.addWidget(self.data_venda_label)
        layout.addWidget(self.data_venda_input)
        layout.addWidget(self.valor_venda_label)
        layout.addWidget(self.valor_venda_input)
        layout.addWidget(self.salvar_button)

        # Layout
        self.setLayout(layout)
        self.setWindowTitle("Controle de Ações")

    def salvar_dados(self):
        # Conecta com o banco
        server = 'nome do server'
        database = 'nome da tabela do banco'
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')

        # Cria a tabela
        cursor = cnxn.cursor()
        cursor.execute("IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'ControleAcoes') CREATE TABLE ControleAcoes (Ativo VARCHAR(50), DataCompra DATE, QuantidadeCompra INT NULL, ValorCompra FLOAT, QuantidadeVenda INT NULL, DataVenda DATE, ValorVenda FLOAT)")

        print(self.ativo_input.text(), self.data_compra_input.text(), self.quantidadeCompra_input.text(), self.valor_compra_input.text(), self.quantidadeVenda_input.text(), self.data_venda_input.text(), self.valor_venda_input.text())
        
        #Insere os dados 
        cursor.execute("INSERT INTO ControleAcoes (Ativo, DataCompra, QuantidadeCompra, ValorCompra, QuantidadeVenda, DataVenda, ValorVenda) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.ativo_input.text(), self.data_compra_input.text(), self.quantidadeCompra_input.text(), self.valor_compra_input.text(), self.quantidadeVenda_input.text(), self.data_venda_input.text(), self.valor_venda_input.text()))
        cnxn.commit()

        #Fecha o banco
        cnxn.close()

        # Limpa os dados
        self.ativo_input.setText('')
        self.data_compra_input.setText('')
        self.quantidadeCompra_input.setText('')
        self.valor_compra_input.setText('')
        self.quantidadeVenda_input.setText('')
        self.data_venda_input.setText('')
        self.valor_venda_input.setText('')

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())