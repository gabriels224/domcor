from flet import *
from utils.colors import *
from utils.validacao import validar
from sevirce.auth import login_usuario, store_token

class escolheruser(Container):
    
    def __init__(self, page: Page):
        super().__init__()
        page.title = "Escolher"
        self.alignment = alignment.center
        self.expand = True
        self.validar = validar()
        self.botao_entrar = ElevatedButton("Entrar")
        self.usuario3 = Container(
                        content=Text(
                            value='Usuario 3',
                            color='#4e73df',
                            size=15
                            ),
                            on_click=lambda _: self.page.go('/usuario3')
                    )
        self.botao_sair = Container(
                alignment=alignment.center,
                bgcolor='black',
                width=50,
                height=40,
                border_radius=30,
                content=Row(
                    alignment='center',
                    controls=[Icon(icons.ARROW_BACK, color=colors.RED_900),]),
                    on_click=lambda _: self.page.go('/login'))
         
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=350,
                    height=700,
                    padding=40,
                    border_radius=30,
                    bgcolor='black',
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Container(width=550,
                                content=Row(
                                controls=[self.botao_sair])),
                            Text(
                                value="Bem Vindo",
                                size=20,
                                color='white',
                                text_align="center"
                            ),
                             Stack(width=175,
                        controls=[
                        Image(
                            src='assets/barbe.jpg'
                        ),
                    ]),
                            Container(height=0),
                            Text(
                                value='Escolha um dos nossos profissionais para dar continuidade.',
                                size=12,
                                color='#858796',
                                text_align='center'
                            ),
                            Container(height=0),
                            
                            Container(
                                content=Text(
                                    value='Vinicius',
                                    color='#4e73df',
                                    size=15
                                    ),
                                    on_click=lambda _: self.page.go('/usuario1')
                            ),
                            Container(
                                content=Text(
                                    value='Usuario 2',
                                    color='#4e73df',
                                    size=15
                                    ),
                                    on_click=lambda _: self.page.go('/usuario2')
                            ),
                            self.usuario3
                        ]
                    )
                )
            ]
            )
        
    
