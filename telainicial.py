from flet import *


class telaini(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.teladesign = Container(
            Container(
                Column(
                    alignment='center',
                        horizontal_alignment='center',
                        controls=[
                    Stack(width=175,
                        controls=[
                        Image(
                            src='assets/barbe.jpg'
                        ),
                    ]),
                    Container(height=0),
                    Column(controls=[
                   Container(
                        alignment=alignment.center,
                        bgcolor=colors.WHITE70,
                        width=200,
                        height=40,
                        border_radius=30,
                        content=Text(
                            value='Login',
                            color=colors.BLACK87),
                            on_click11=lambda _: self.page.go('/login'), 
                        )]),
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
                  self.teladesign
                            ])