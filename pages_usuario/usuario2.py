import flet as ft
import sqlite3
import datetime as dt
#conectando ao banco de dados
conexao = sqlite3.connect("dbDatabase2.db", check_same_thread=False)
cur = conexao.cursor()

class App2(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        page.title = "Dom Cort's"
        self.alignment = ft.alignment.center
        self.expand = True
        self.error_border = ft.border.all(width=1, color='red')
        self.todos_dados = ft.Column(auto_scroll=True)
        self.login = ft.TextField(label="Nome", 
                                  width=300, 
                                  text_size='bold', 
                                  border_radius=30,
                                )
        
        self.profissional = ft.Text("Profissional 2")
        
        self.dia = ft.Dropdown(
                    width=60,                   
                    border_radius=30,
                    options=[
            ft.dropdown.Option("01"),ft.dropdown.Option("02"),ft.dropdown.Option("03"),ft.dropdown.Option("04"),
            ft.dropdown.Option("05"),ft.dropdown.Option("06"),ft.dropdown.Option("07"),ft.dropdown.Option("08"),
            ft.dropdown.Option("09"),ft.dropdown.Option("10"),ft.dropdown.Option("11"),ft.dropdown.Option("12"),
            ft.dropdown.Option("13"),ft.dropdown.Option("14"),ft.dropdown.Option("15"),ft.dropdown.Option("16"),
            ft.dropdown.Option("17"),ft.dropdown.Option("18"),ft.dropdown.Option("19"),ft.dropdown.Option("20"),
            ft.dropdown.Option("21"),ft.dropdown.Option("22"),ft.dropdown.Option("23"),ft.dropdown.Option("24"),
            ft.dropdown.Option("25"),ft.dropdown.Option("26"),ft.dropdown.Option("27"),ft.dropdown.Option("28"),
            ft.dropdown.Option("29"),ft.dropdown.Option("30"),ft.dropdown.Option("31"),
        ],
        border="underline",
    )

        self.hora = ft.Dropdown(
                    width=60,
                    border_radius=30,
                    options=[
            ft.dropdown.Option("09"),ft.dropdown.Option("10"),ft.dropdown.Option("11"),ft.dropdown.Option("12"),
            ft.dropdown.Option("13"),ft.dropdown.Option("14"),ft.dropdown.Option("15"),ft.dropdown.Option("16"),
            ft.dropdown.Option("17"),ft.dropdown.Option("18")
        ], border="underline"
    )
        
        self.minuto = ft.Dropdown(
                    width=60,
                    border_radius=30,
                    options=[
            ft.dropdown.Option("00"),ft.dropdown.Option("10"),ft.dropdown.Option("20"),ft.dropdown.Option("30"),
            ft.dropdown.Option("40"),ft.dropdown.Option("50")
        ], border="underline"
    )
        self.ano = dt.datetime.now().year
        
        self.whatsapp = ft.TextField(label="WhatsApp", 
                                     width=300, 
                                     text_size='bold', 
                                     border_radius=30, 
                                     hint_text="Enter text here",
                                     )
        
        self.mes = ft.Dropdown(
                    width=60,                   
                    border_radius=30,
                    options=[
            ft.dropdown.Option("01"),ft.dropdown.Option("02"),ft.dropdown.Option("03"),ft.dropdown.Option("04"),
            ft.dropdown.Option("05"),ft.dropdown.Option("06"),ft.dropdown.Option("07"),ft.dropdown.Option("08"),
            ft.dropdown.Option("09"),ft.dropdown.Option("10"),ft.dropdown.Option("11"),ft.dropdown.Option("12"),
        ],
        border="underline",
    )

        #criar um dado dentro do banco de dados
    def addnovo_dados (self, e):
        if not self.login.value:
            self.login.error_text = "Insira seu nome"
            self.page.update()
        else:
            if not self.dia.value:
                self.dia.error_text = ""
                self.page.update()
            if not self.hora.value:
                self.hora.error_text = ""
                self.page.update()
            else:
                if not self.whatsapp.value:
                    self.whatsapp.error_textr = "Insira sua senha"
                    self.page.update()
                else:
                    self.page.snack_bar = ft.SnackBar(
                        ft.Text(
                            "Horário Marcado"))
                    self.page.snack_bar.open = True
                    self.page.update()
                    cur.execute("INSERT INTO Database (nome, data, horario, whatsapp, profissional) VALUES (?,?,?,?,?)", 
                        [self.login.value, 
                            (f"{self.ano}-{self.mes.value}-{self.dia.value}"), 
                           (f"{self.hora.value}:{self.minuto.value}"),
                            self.whatsapp.value,
                            self.profissional.value,
                        ])
                    conexao.commit()       
                    self.todos_dados.controls.clear()
                    self.page.update()
                self.page.update()
            self.page.update()
        self.page.update()


    def build(self):
        return ft.Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                            width=500,
                            padding=20,
                            bgcolor='white',
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        value="Vinicius",
                                        size=25,
                                        color='black',
                                        text_align="center"
                                    )])),
                                    ft.Stack(
                                        width=125,
                                        controls=[
                                ft.Image(
                                    src='assets/icons/bb.png', 
                                    border_radius=30,
                                )                           
                            ]),
                self.login, 
                ft.Row(alignment='center',
                        controls=[ft.Column(
                                    horizontal_alignment='center',
                                    controls=[ft.Text("Dia:"), 
                                              self.dia,
                                              ],
                                            ), 
                                ft.Column(
                                    horizontal_alignment='center',
                                    controls=[ft.Text("Mês:"), 
                                              self.mes,
                                              ],
                                            ),
                                ft.Column(
                                    horizontal_alignment='center',
                                    controls=[ft.Text("Hora:"), 
                                              self.hora,
                                              ],
                                            ),
                                ft.Column(
                                    horizontal_alignment='center',
                                    controls=[ft.Text(""), 
                                              self.minuto,
                                              ],
                                            ),
                                ],
                            ),

                 self.whatsapp,

                ft.Container(height=0),

                ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor='black',
                    width=200,
                    height=40,
                    border_radius=30,
                    content=ft.Text(
                                value='Marcar',
                                color='white'
                                    ), 
                    on_click=self.addnovo_dados), 

                ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor='black',
                    width=200,
                    height=40,
                    border_radius=30,
                    content=ft.Row(
                                alignment='center',
                                controls=[ft.Icon(ft.icons.ARROW_BACK, 
                                color=ft.colors.RED_900,),
                                        ],
                                    ),
                    on_click=lambda _: self.page.go('/escolheruser')),
                                                                        ]) #self.todos_dados
                                                                        #exibir todos os dados
