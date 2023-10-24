from flet import *
from utils.colors import *
from utils.validacao import validar
from sevirce.auth import Criar_usuario, store_token, rekove_token



class Signup(Container):
    
    def __init__(self, page: Page):
        super().__init__()
        page.title = "Cadastro de Login"
        self.alignment = alignment.center
        self.expand = True
        self.validar = validar()
        self.error_border = border.all(width=1, color='red')
        self.nome_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                    hint_style=TextStyle(
                        size=12, color='#858796'
                    ),
                    width=300,
                    hint_text='Digite seu nome completo',
                    cursor_color='#858796',
                    text_style=TextStyle(
                        size=14, color='black'
                    )
                    ),
                    border=border.all(width=1, color='#bdcdf4'),
                    border_radius=30
            )
        
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                    hint_style=TextStyle(
                        size=12, color='#858796'
                    ),
                    width=300,
                    hint_text='Insira seu emaill',
                    cursor_color='#858796',
                    text_style=TextStyle(
                        size=14, color='black'
                    )
                    ),
                    border=border.all(width=1, color='#bdcdf4'),
                    border_radius=30
        )
        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                    hint_style=TextStyle(
                        size=12, color='#858796'
                    ),
                    width=300,
                    hint_text='Entrar senha...',
                    cursor_color='#858796',
                    text_style=TextStyle(
                        size=14, color='black'
                    ),
                    password=True
                    ),
                    border=border.all(width=1, color='#bdcdf4'),
                    border_radius=30

            )
       

        self.telasignup = Container(
            Container(
                Column(
                    alignment='center',
                    horizontal_alignment='center',
                        controls=[
                            Container(

                    padding=20,
                    border_radius=30,
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value="Criar Conta",
                                size=16,
                                color='white',
                                text_align="center")])),
                            Stack(
                                 width=150,
                                 controls=[
                             Image(
                            src='assets/barbe.jpg'
                        ), 
                    ]),
                    self.nome_box,
                       self.email_box, 
                        self.password_box,
                        Container(height=0),
                   Container(
                        alignment=alignment.center,
                        bgcolor=colors.WHITE70,
                        width=175,
                        height=40,
                        border_radius=30,
                        content=Text(
                            value='Criar Sua Conta',
                            color=colors.BLACK87),
                            on_click=self.signup, 
                        ),
                        Container(
                                content=Text(
                                    value='Você já tem uma conta',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/login')
                            ),
                            Container(
                                content=Text(
                                    value='Esqueceu a senha?',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/forgot')
                            ),
                ])
            ),
            border_radius=30,
            width=350,
            height=700,
            bgcolor='black'
        )
        
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                      self.telasignup
                        ]
                    )


    def signup(self, e):
        if not self.validar.nome_correto(self.nome_box.content.value):
            self.nome_box.border = self.error_border
            self.nome_box.update()
        if not self.validar.validar_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
        if not self.validar.validar_senha(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()
        else:
            nome = self.nome_box.content.value
            email = self.email_box.content.value
            password = self.password_box.content.value

            self.page.splash = ProgressBar()
            self.page.update()

            token = Criar_usuario(nome, email, password)
            self.page.splash = None
            self.page.update()

            if token:
                rekove_token(token)
                self.page.go('/login')
            else:
                self.page.snack_bar = SnackBar(
                    Text(
                        "Credencial Invalida"
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()








