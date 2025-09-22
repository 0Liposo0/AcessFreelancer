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

    url = {
            "/": lambda: loading.new_loading_page(page=page, call_layout=lambda: create_page_login(page)),
            "/freelancers": lambda: loading.new_loading_page(page, lambda: create_page_see_freelancers(page)),
            "/projects": lambda: loading.new_loading_page(page=page, call_layout=lambda:create_page_project(page)),
            "/files": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_files(page)),
            "/files/token": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_files_details(page)),
            "/deliveries": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_see_deliverys(page)),
            "/deliveries/token": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_delivery_details(page)),
            "/deliveries/insert": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_new_delivery(page)),
            "/logs": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_see_logs(page)),
            "/models": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_see_models(page)),
            "/models/token": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_models_details(page)),
            "/models/insert": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_new_model(page)),
            "/payment": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_payment(page)),
            "/freelancers/token": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_freelancer_token(page)),
            "/project/user": lambda : loading.new_loading_page(page=page, call_layout=lambda:create_page_project_token_user(page)),
        }

    def route_change(e: ft.RouteChangeEvent):
        page.on_keyboard_event = None

        if page.route in url:
            url[page.route]()   
        else:
            url["/"]()     
    
    page.on_route_change = route_change

    profile = page.client_storage.get("profile")
    if profile:
        url[page.route]()
    else:
        page.go("/") 


if __name__ == "__main__":
    ft.app(target=main, upload_dir="uploads", assets_dir="assets", view=ft.WEB_BROWSER)




    