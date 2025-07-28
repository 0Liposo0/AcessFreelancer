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
    
    loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page))

    #page.session.set("profile", {
    #        "username": "attam_admin",
    #        "name": "Attam",
    #        "permission": "adm",
    #        "current_project": ".",
    #    })
    
    #loading.new_loading_page(page=page, call_layout=lambda:create_page_see_freelancers(page))


if __name__ == "__main__":
    ft.app(target=main, upload_dir="uploads", assets_dir="assets")




    