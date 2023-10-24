from flet import *
from utils.validacao import validar
from sevirce.auth import login_usuario, store_token, rekove_token

class login(Container):
    
    def __init__(self, page: Page):
        super().__init__()
        page.title = "Login"
        self.alignment = alignment.center
        self.expand = True
        self.validar = validar()
        self.error_border = border.all(width=1, color='red')
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                    hint_style=TextStyle(
                        size=12, color='#858796'
                    ),
                    width=300,
                    hint_text='Entrar email...',
                    cursor_color='#858796',
                    text_style=TextStyle(
                        size=14, color='white'
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
                        size=14, color='white'
                    ),
                    password=True
                    ),
                    border=border.all(width=1, color='#bdcdf4'),
                    border_radius=30
            )
        
        self.telalogin1 = Container(
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
                                value="Dom Cort's",
                                size=16,
                                color='white',
                                text_align="center")])),
                    Stack(width=175,
                        controls=[
                        Image(
                            src='assets/barbe.jpg'
                        ),
                    ]),
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
                            value='Login',
                            color=colors.BLACK87),
                            on_click=self.login1, 
                        ),
                        Container(
                                content=Text(
                                    value='Esqueceu a senha?',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/forgot')
                            ),
                            Container(
                                content=Text(
                                    value='Criar Login',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/signup')
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
            controls=[self.telalogin1,
                        ]
                    )
                
            
            

    def login1(self, e):
        if not self.validar.validar_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
        if not self.validar.validar_senha(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()
        else:
            email = self.email_box.content.value
            password = self.password_box.content.value

            self.page.splash = ProgressBar()
            self.page.update()

            token = login_usuario(email, password)
            self.page.splash = None
            self.page.update()

            if token:
                store_token(token)
                self.page.go('/escolheruser')
            else:
                self.page.snack_bar = SnackBar(
                    Text(
                        "Credencial Invalida"
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()








