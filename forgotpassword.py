from flet import *
from utils.validacao import validar

class Forgotpass(Container):
    def __init__(self, page: Page):
        super().__init__()
        page.title = "Alterar Senha"
        self.expand = True
        self.validar = validar(),
        self.error_border = border.all(width=1, color='red')
        self.alignment = alignment.center
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
                        size=14, color='black'
                    )
                    ),
                    border=border.all(width=1, color='#bdcdf4'),
                    border_radius=30

            )

        self.telafogot1 = Container(
            Container(
                Column(
                    alignment='center',
                    horizontal_alignment='center',
                        controls=[
                             Container(
                    width=500,
                    border_radius=30,
                    padding=40,
                    bgcolor='black',
                    content=Column(
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value="Esqueceu sua senha?",
                                size=20,
                                color='white',
                                text_align='center'
                            ),
                             Stack(width=175,
                        controls=[
                        Image(
                            src='assets/barbe.jpg'
                        ),
                    ]),
                            Text(
                                value='Para recuperar sua senha, insira seu email e aguarde!',
                                size=16,
                                color='#858796',
                                text_align='center'
                            ),
                            ])),
                       self.email_box,
                        Container(height=0),
                   Container(
                        alignment=alignment.center,
                        bgcolor=colors.WHITE70,
                        width=175,
                        height=40,
                        border_radius=30,
                        content=Text(
                            value='Alterar senha',
                            color=colors.BLACK87),
                            on_click=self.reset_password, 
                        ),
                        Container(height=10),
                        Container(
                                content=Text(
                                    value='Criar Conta',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/signup')
                            ),
                            Container(
                                content=Text(
                                    value='Já tem uma Conta?',
                                    color='#4e73df',
                                    size=12
                                    ),
                                    on_click=lambda _: self.page.go('/login')
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
            controls=[self.telafogot1,
                        ]
                    )


    def reset_password(self, e):
        if not self.validar.validar_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
