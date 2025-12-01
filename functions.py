from models import *
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def get_menu(ft, page):

    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")

    def go_url(url):
        profile = page.client_storage.get("profile")
        profile.update({
            "deliveries_filter": [None],
            "models_filter": [None],
            "freelancers_filter": [None],
            "files_filter": [None],
        })
        page.client_storage.set("profile", profile)
        page.go(url)

    btn_exit = buttons.create_button(on_click=lambda e: page.go("/"),
                                      text="Logout",
                                      color=ft.Colors.RED,
                                      col=12,
                                      padding=10,)
    btn_projeto = buttons.create_button(on_click=lambda e: page.go("/projects"),
                                      text= "Projetos",
                                      color=ft.Colors.INDIGO_600,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_logs = buttons.create_button(on_click=lambda e: go_url("/logs"),
                                            text= "Logs",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.INDIGO_600,
                                      col=12,
                                      padding=10,)


    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    
    btn_dashboard = buttons.create_button(on_click=lambda e: page.go("/dashboard"),
                                      text= "Dashboard",
                                      color=ft.Colors.INDIGO_600,
                                      col=12,
                                      padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_dashboard,
        btn_projeto,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_see_logs,
        btn_exit,
        ],
    bgcolor=ft.Colors.WHITE,
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_dashboard) 
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.remove(btn_see_logs)
        drawer.controls.insert(0, btn_profile)
        drawer.controls.insert(1, btn_projeto_user)

    return drawer

def get_app_bar(ft, page):

    return ft.AppBar(
        leading_width=40,
        center_title=True,
        bgcolor=ft.Colors.WHITE,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

def return_line_chart(ft, data, title):


    def get_min_y_and_max_y(data):
        data_points = data[0][0].data_points
        if not data_points:
            return [0, 0]

        min_y = min(point.y for point in data_points)
        max_y = max(point.y for point in data_points)

        return [min_y, max_y]
    
    
    def build_left_axis_from_data(tips, divisions=3):
        min_y, max_y = get_min_y_and_max_y(tips)

        min_y = 0
        step = int((max_y - min_y) / divisions)
        step = int(round(step / 10) * 10)

        labels = []
        for i in range(1, divisions + 1):
            value = int(min_y + i * step)

            labels.append(
                ft.ChartAxisLabel(
                    value=value,
                    label=ft.Text(
                        str(value),
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                )
            )

        return ft.ChartAxis(labels=labels, labels_size=40, labels_interval=step)

    def get_last_7_weekdays(x_map):
     
        dias = []
        hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))

        nomes = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

        for i in range(7, -1, -1):
            dia = hoje - timedelta(days=i)
            data_str = dia.strftime("%d/%m/%Y")

            novo_x = x_map[data_str]  # usa novo X (1 a 8)
            nome_semana = nomes[dia.weekday()]

            dias.append(ft.ChartAxisLabel(
                value=novo_x,
                label=ft.Text(nome_semana, color=ft.Colors.BLACK)
            ))


        return dias
        
    weekdays = get_last_7_weekdays(data[1])

    chart = ft.LineChart (
        data_series=data[0],
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE))
        ),
        left_axis= build_left_axis_from_data(data, divisions=3),
        bottom_axis = ft.ChartAxis(
            labels=weekdays,
            labels_size=32,
            title=ft.Text(str(title),color=ft.Colors.BLACK),
            title_size = 50
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY),
        min_y=get_min_y_and_max_y(data)[0],
        max_y=((get_min_y_and_max_y(data)[1]) * 1.1),
        min_x=0,
        max_x=9,
        expand=True,
    )


    return chart