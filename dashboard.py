from flet import *
import sqlite3

#conectando ao banco de dados
conexao = sqlite3.connect("dbDatabase3.db", check_same_thread=False)

class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()