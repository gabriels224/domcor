from flet import *

class teladm(Container):
    
    def __init__(self, page: Page):
        super().__init__()
        page.title = "Adm"
        self.alignment = alignment.center
        self.expand = True
        self.botao_entrar = ElevatedButton("Entrar")
        self.usuario3 = Container(
                        content=Text(
                            value='Adm3',
                            color='#4e73df',
                            size=15
                            ),
                            on_click=lambda _: self.page.go('/admin3')
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
                            src='assets/icons/bb.png'
                        ),
                    ]),
                            Container(height=0),
                            Text(
                                value='Página de adm para vizualização',
                                size=12,
                                color='#858796',
                                text_align='center'
                            ),
                            Container(height=0),
                            
                            Container(
                                content=Text(
                                    value='Adm1',
                                    color='#4e73df',
                                    size=15
                                    ),
                                    on_click=lambda _: self.page.go('/admin1')
                            ),
                            Container(
                                content=Text(
                                    value='Adm2',
                                    color='#4e73df',
                                    size=15
                                    ),
                                    on_click=lambda _: self.page.go('/admin2')
                            ),
                            self.usuario3
                        ]
                    )
                )
            ]
            )
        
    
