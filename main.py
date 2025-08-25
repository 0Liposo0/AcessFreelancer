import flet as ft
from views import *
from models import *



def main(page: ft.Page):
    page.title = 'Acesso Freelancer(admin)'
    page.expand = True  
    page.scroll = "auto"
    page.padding=20 
    page.bgcolor = ft.Colors.INDIGO_600
    loading = LoadingPages(page)

    def route_change(e: ft.RouteChangeEvent):
        url = {
            "/": lambda: loading.new_loading_page(page=page, call_layout=lambda: create_page_login(page)),
            "/freelancers": lambda: loading.new_loading_page(page, lambda: create_page_see_freelancers(page)),
        }

        if page.route in url:
            url[page.route]()   
        else:
            url["/"]()     
    
    page.on_route_change = route_change

    route_change(ft.RouteChangeEvent(page.route))


if __name__ == "__main__":
    ft.app(target=main, upload_dir="uploads", assets_dir="assets", view=ft.WEB_BROWSER)




    