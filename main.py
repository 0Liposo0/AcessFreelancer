import flet as ft
from views import *
from models import *

def main(page: ft.Page):
    page.title = 'Acesso Freelancer(admin)'
    page.expand = True  
    page.bgcolor = ft.Colors.AMBER
    page.scroll = "auto"
    page.padding=20 
 
    loading = LoadingPages(page)
    loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page))


if __name__ == "__main__":
    ft.app(target=main, upload_dir="uploads", assets_dir="assets")




