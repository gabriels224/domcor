import flet as ft
import sqlite3
import datetime as dt

#conectando ao banco de dados
conexao1 = sqlite3.connect("dbDatabase1.db", check_same_thread=False)
cur1 = conexao1.cursor()

class admin1(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()

        self.todos_dados = ft.Column(auto_scroll=True)
        self.editar_dado = ft.TextField(label="Editar")

        #READ - mostrar todos dados do banco de dados
    def redenrizar_todos(self):
        cur1.execute("SELECT * FROM Database WHERE data = CURRENT_DATE ORDER BY id DESC")
        conexao1.commit()

        meus_dados = cur1.fetchall()

        for dado in meus_dados:
            self.todos_dados.controls.append(
                                  ft.ListTile(
                    subtitle=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Data: {dado[2]}"), 
                                           ft.Text(f"Horário: {dado[3]}")]),
                    title=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Nome: {dado[1]}"), 
                                          ]),
                    ))
        self.update()

        #criar um dado dentro do banco de dados
    def addnovo_dados (self, e):            
        self.todos_dados.controls.clear()
        self.redenrizar_todos()
        self.page.update()

    def ciclo (self):
        self.redenrizar_todos()


    def build(self):
        return  ft.Column(
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[ft.ElevatedButton("Atualizar", on_click=self.addnovo_dados ),self.todos_dados])

                                                                    #exibir todos os dados

    #criar app
def main1 (page):
    page.update()
    #criar pagina de login
    tela = admin1()
    page.title = "Login"
    page.scroll = "always"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(tela)
    page.update()



conexao2 = sqlite3.connect("dbDatabase2.db", check_same_thread=False)
cur2 = conexao2.cursor()

class admin2(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()

        self.todos_dados = ft.Column(auto_scroll=True)
        self.editar_dado = ft.TextField(label="Editar")

        #READ - mostrar todos dados do banco de dados
    def redenrizar_todos(self):
        cur2.execute("SELECT * FROM Database WHERE data = CURRENT_DATE ORDER BY id DESC")
        conexao2.commit()

        meus_dados = cur2.fetchall()

        for dado in meus_dados:
            self.todos_dados.controls.append(
                  ft.Column(alignment='center',
                          horizontal_alignment='center',
                          controls=[ft.ListTile(
                    subtitle=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Data: {dado[2]}"), 
                                           ft.Text(f"Horário: {dado[3]}")]),
                    title=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Nome: {dado[1]}"), 
                                          ]),
                    )]))
        self.update()

        #criar um dado dentro do banco de dados
    def addnovo_dados (self, e):            
        self.todos_dados.controls.clear()
        self.redenrizar_todos()
        self.page.update()

    def ciclo (self):
        self.redenrizar_todos()


    def build(self):
        return ft.Column([ft.Text("", size=20, weight='bold'), 
        ft.ElevatedButton("Atualizar", on_click=self.addnovo_dados ), self.todos_dados])
                                                                    #exibir todos os dados

    #criar app
def main2 (page):
    page.update()
    #criar pagina de login
    tela = admin2()
    page.title = "Login"
    page.scroll = "always"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(tela)
    page.update()



conexao3 = sqlite3.connect("dbDatabase3.db", check_same_thread=False)
cur3 = conexao3.cursor()

class admin3(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()

        self.todos_dados = ft.Column(auto_scroll=True, )
        self.editar_dado = ft.TextField(label="Editar")

        #READ - mostrar todos dados do banco de dados
    def redenrizar_todos(self):
        cur3.execute("SELECT * FROM Database WHERE data = CURRENT_DATE ORDER BY id DESC")
        conexao3.commit()

        meus_dados = cur3.fetchall()

        for dado in meus_dados:
            self.todos_dados.controls.append(
                  ft.Column(alignment='center',
                          horizontal_alignment='center',
                          controls=[ft.ListTile(
                    subtitle=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Data: {dado[2]}"), 
                                           ft.Text(f"Horário: {dado[3]}")]),
                    title=ft.Row(alignment='center',
                                 controls=[ft.Text(f"Nome: {dado[1]}"), 
                                          ]),
                    )]))
            
        self.update()

        #criar um dado dentro do banco de dados
    def addnovo_dados (self, e):            
        self.todos_dados.controls.clear()
        self.redenrizar_todos()
        self.page.update()

    def ciclo (self):
        self.redenrizar_todos()


    def build(self):
        return ft.Column([ft.Text("", size=20, weight='bold'), 
        ft.ElevatedButton("Atualizar", on_click=self.addnovo_dados ), self.todos_dados])
                                                                    #exibir todos os dados

    #criar app
def main3 (page):
    page.update()
    #criar pagina de login
    tela = admin3()
    page.title = "Login"
    page.scroll = "always"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(tela)
    page.update()
