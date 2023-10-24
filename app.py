from flet import *
from pages.dashboard import Dashboard
from pages.forgotpassword import Forgotpass
from pages.signup import Signup
from pages.login import login
from pages_usuario.usuario1 import App1
from pages_usuario.usuario2 import App2
from pages_usuario.usuario3 import App3
from pages.escolheruser import escolheruser
from pages.telainicial import telaini
from pages_adm.admin import admin1, admin2, admin3
from pages_adm.teladm import teladm



class Main (UserControl):

    def __init__(self, page: Page,):
        super().__init__()
        self.page = page
        self.init_helper()
        

    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/admin1')
        self.page.update()

    def on_route_change(self, route):
        new_page = {
            "/login":login,
            "/signup": Signup,
            "/me":Dashboard,
            "/forgot":Forgotpass,
            "/usuario1": App1,
            "/usuario2": App2,
            "/usuario3": App3,
            "/escolheruser": escolheruser,
            "/telaini": telaini,
            "/admin1": admin1,
            "/admin2": admin2,
            "/admin3": admin3,
            "/teladm": teladm


        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )

    
app( target=Main, assets_dir='assets')

    