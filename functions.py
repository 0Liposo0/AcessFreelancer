from models import *
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time


def get_menu(ft, page):

    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")

    def go_url(url):
        profile = page.client_storage.get("profile")
        profile.update({
            "deliveries_filter": [None],
            "models_filter": [None],
            "ortos_filter": [None],
            "lisps_filter": [None],
            "ibge_filter": [None],
            "logs_filter": [None],
            "freelancers_filter": [None],
            "files_filter": [None],
            "planners_filter": [None],
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
                                            text= "Usuários",
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
    btn_see_lisps = buttons.create_button(on_click=lambda e: go_url("/lisps"),
                                            text= "Lisps",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_ibge = buttons.create_button(on_click=lambda e: go_url("/ibge"),
                                            text= "IBGE",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_orto = buttons.create_button(on_click=lambda e: go_url("/ortofotos"),
                                            text= "Ortofotos",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_see_planners = buttons.create_button(on_click=lambda e: go_url("/planners"),
                                            text= "Planilhas",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.INDIGO_600,
                                            col=12,
                                            padding=10,)
    
    btn_user = buttons.create_button(on_click=lambda e: page.go("/user"),
                                      text= "Início",
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
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_see_orto,
        btn_see_planners,
        btn_see_lisps,
        btn_see_ibge,
        btn_see_logs,
        btn_exit,
        ],
    bgcolor=ft.Colors.WHITE,
    )
    
    if dict_profile["permission"] != "adm":
        if dict_profile["permission"] == "user":
            drawer.controls.remove(btn_dashboard) 
            drawer.controls.remove(btn_projeto) 
            drawer.controls.remove(btn_see_freelancers) 
            drawer.controls.remove(btn_see_logs)
            drawer.controls.remove(btn_see_ibge)
            drawer.controls.remove(btn_see_file)
            drawer.controls.remove(btn_see_deliverys)
            drawer.controls.remove(btn_see_models)
            drawer.controls.remove(btn_see_planners)
            drawer.controls.insert(0, btn_user)
        elif dict_profile["permission"] == "ldr":
            drawer.controls.remove(btn_dashboard) 
            drawer.controls.remove(btn_projeto) 
            drawer.controls.remove(btn_see_freelancers) 
            drawer.controls.remove(btn_see_logs)
            drawer.controls.remove(btn_see_ibge)
            drawer.controls.insert(0, btn_profile)
            drawer.controls.insert(1, btn_projeto_user)
        else:
            drawer.controls.remove(btn_dashboard) 
            drawer.controls.remove(btn_projeto) 
            drawer.controls.remove(btn_see_freelancers) 
            drawer.controls.remove(btn_see_logs)
            drawer.controls.remove(btn_see_ibge)
            drawer.controls.insert(0, btn_profile)



    return drawer

def get_app_bar(ft, page):

    return ft.AppBar(
        leading_width=40,
        center_title=True,
        bgcolor=ft.Colors.WHITE,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

def return_line_chart(ft, data, title, type):


    def get_min_y_and_max_y(data):
        data_points = data[0][0].data_points
        if not data_points:
            return [0, 0]

        min_y = min(point.y for point in data_points)
        max_y = max(point.y for point in data_points)

        if min_y < 0:
            min_y = 0

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

    def get_last_7_weekdays(x_map, type):
        dias = []

        hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))

        nomes = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

        # RANGE DE DIAS
        dias_range = 7 if type == "week" else 31

        for i in range(dias_range, -1, -1):
            dia = hoje - timedelta(days=i)
            data_str = dia.strftime("%d/%m/%Y")

            if data_str not in x_map:
                continue

            novo_x = x_map[data_str]

            # --- DIFERENÇA ENTRE WEEK E MONTH ---
            if type == "week":
                label_text = nomes[dia.weekday()]       # Seg, Ter, ...
            else:  # month
                label_text = str(dia.day)              # 1, 2, 3, ... 31

            dias.append(
                ft.ChartAxisLabel(
                    value=novo_x,
                    label=ft.Text(label_text, color=ft.Colors.BLACK)
                )
            )

        return dias
        
    weekdays = get_last_7_weekdays(data[1], type)

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
        max_x=len(data[0][0].data_points) + 1,
        expand=True,
    )


    return chart

def return_table(list):

    data_column = []

    for item in list:
        data_column.append(ft.DataColumn(ft.Text(value=item, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)))


    return ft.DataTable(
                data_row_max_height=50,
                column_spacing=40,
                expand=True,
                expand_loose=True,
                columns=data_column,
                rows=[]
            )

def return_container_table(table, pagination_bar, lbl_total):

    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()


    return ft.Column(
                controls=[
                    ft.Container(
                        padding=0,  
                        expand=True,  
                        theme=texttheme1,
                        clip_behavior=ft.ClipBehavior.NONE,  
                        content=table,
                    ),
                    ft.Row(
                        controls=[lbl_total],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    pagination_bar,  # Barra com números
                ],
                scroll=ft.ScrollMode.AUTO,  
                alignment=ft.MainAxisAlignment.CENTER,  
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,  
            )

def update_pagination_bar(
    pagination_bar,
    current_page,
    total_pages,
    load_page_callback,
    initial=False
):

    pagination_bar.controls.clear()

    if total_pages <= 1:
        if not initial:
            pagination_bar.update()
        return

    max_visible = 5  # máximo de botões numéricos visíveis

    # Define janela deslizante
    start_page = max(1, current_page[0] - 2)
    end_page = start_page + max_visible - 1

    if end_page > total_pages:
        end_page = total_pages
        start_page = max(1, end_page - max_visible + 1)

    # Botão voltar
    if current_page[0] > 1:
        pagination_bar.controls.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.INDIGO_600,
                on_click=lambda e: load_page_callback(current_page[0] - 1)
            )
        )

    # Sempre mostrar botão 1 se estiver fora da janela
    if start_page > 1:
        pagination_bar.controls.append(
            ft.ElevatedButton(
                text="1",
                bgcolor=ft.Colors.INDIGO_600,
                color=ft.Colors.WHITE,
                on_click=lambda e: load_page_callback(1)
            )
        )

        if start_page > 2:
            pagination_bar.controls.append(
                ft.Text("...")
            )

    # Botões centrais
    for p in range(start_page, end_page + 1):
        pagination_bar.controls.append(
            ft.ElevatedButton(
                text=str(p),
                bgcolor=ft.Colors.AMBER if p == current_page[0] else ft.Colors.INDIGO_600,
                color=ft.Colors.WHITE,
                on_click=lambda e, page=p: load_page_callback(page)
            )
        )

    # Sempre mostrar última página se estiver fora da janela
    if end_page < total_pages:
        if end_page < total_pages - 1:
            pagination_bar.controls.append(
                ft.Text("...")
            )

        pagination_bar.controls.append(
            ft.ElevatedButton(
                text=str(total_pages),
                bgcolor=ft.Colors.INDIGO_600,
                color=ft.Colors.WHITE,
                on_click=lambda e: load_page_callback(total_pages)
            )
        )

    # Botão avançar
    if current_page[0] < total_pages:
        pagination_bar.controls.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_FORWARD,
                icon_color=ft.Colors.INDIGO_600,
                on_click=lambda e: load_page_callback(current_page[0] + 1)
            )
        )

    if not initial:
        pagination_bar.update()

def load_page(
    page_number,
    pagination_bar,
    current_page,
    items_per_page,
    lbl_total,
    table,
    filtered_data,
    headers,
    field_map,
    page,
    planner,
    list_filtros = None,
    page_type = None,
    initial=False,
):

    current_page[0] = page_number

    total_items = len(filtered_data)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    start = (page_number - 1) * items_per_page
    end = start + items_per_page

    page_slice = filtered_data[start:end]

    table.rows.clear()

    for d in page_slice:
        row = build_row(
            d=d,
            headers=headers,
            field_map=field_map,
            page=page,
            planner=planner,
            list_filtros=list_filtros,
            table=table,
            page_type=page_type,
            
        )
        table.rows.append(row)
    
    
    lbl_total.value = f"{len(page_slice)} itens de {total_items}"

    if not initial:
        page.update()

    update_pagination_bar(
        pagination_bar=pagination_bar,
        current_page=current_page,
        total_pages=total_pages,
        load_page_callback=lambda p: load_page(
            p,
            pagination_bar,
            current_page,
            items_per_page,
            lbl_total,
            table,
            filtered_data,
            headers,
            field_map,
            page,
            planner,
            list_filtros=list_filtros,
            page_type=page_type,
            initial=False,
        ),
        initial=initial
    )

def prepare_data(get_json, headers, field_map):



    prepared = []

    for d in get_json:

        row_data = {}

        for header in headers:
            if header == "":
                continue

            field = field_map.get(header)
            row_data[field] = d.get(field)

        # garantir que check também venha
        row_data["check"] = d.get("check", "no")
        row_data["editor"] = d.get("editor")

        prepared.append(row_data)



    return prepared


def build_list_dropdown(
        on_dropdown_change,
        filtros_config,
        initial=False
    ):
        def dd(label, key, options, *, width=None, filter=False):
            return ft.Dropdown(
                label=label,
                expand=True,
                width=width,
                options=options,
                filled=True,
                editable=filter,
                enable_filter=filter,
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                on_change=lambda e: on_dropdown_change(e, key),
            )

        def opts(values):
            result = []

            for v in values:
                if isinstance(v, ft.dropdown.Option):
                    # Já é uma Option → usa direto
                    result.append(v)
                else:
                    # Assume string ou valor simples
                    result.append(
                        ft.dropdown.Option(
                            key=str(v),
                            content=ft.Text(str(v), color=ft.Colors.BLACK)
                        )
                    )

            return result

        controls = []

        for f in filtros_config:
            options = f["options"]
            if isinstance(options, list):
                options = opts(options)

            controls.append(
                dd(
                    label=f["label"],
                    key=f["key"],
                    options=options,
                    width=f.get("width"),
                    filter=f.get("filter", False),
                )
            )

        return ft.Row(
            controls=controls,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

def build_row(
    d,
    headers,
    field_map,
    page,
    planner,
    list_filtros=None,
    table=None,
    page_type=None

):

    sp = SupaBase(page)
    username = page.client_storage.get("profile")["username"]

    check = str(d.get("check", "no"))
    row_color = ft.Colors.GREEN if check == "yes" else ft.Colors.WHITE

    def text_cell(value):
        return ft.DataCell(
            ft.Text(
                value=str(value) if value is not None else "",
                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLACK,
                expand=True,
            )
        )

    def toggle_check(e):

        current = str(d.get("check", "no"))
        new_value = "yes" if current == "no" else "no"

    
        if new_value == "yes":
            editor_value = username
        else:
            editor_value = None

        data = {
            "codigo": row.cells[0].content.value,
            "editor": editor_value,
            "check": new_value
        }

        response = sp.edit_planner_data(data, planner=planner)

        if response.status_code in [200, 204]:

            d["check"] = new_value

            d["editor"] = editor_value

            # Atualiza dados locais
            row.cells[10].content.value = editor_value if editor_value else ""

            row.color = {
                ft.ControlState.DEFAULT:
                    ft.Colors.GREEN if new_value == "yes" else ft.Colors.WHITE
            }

            btn = row.cells[-1].content
            btn.bgcolor = ft.Colors.GREEN if new_value == "yes" else ft.Colors.GREY

            # Atualiza SOMENTE a linha
            row.update()

            snack_bar = ft.SnackBar(
                content=ft.Text("Dados atualizados com sucesso"),
                bgcolor=ft.Colors.GREEN
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

        else:

            snack_bar = ft.SnackBar(
                content=ft.Text("Não foi possivel atualizar"),
                bgcolor=ft.Colors.RED
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    cells = []

    row = ft.DataRow(
        cells=cells,
        color={ft.ControlState.DEFAULT: row_color},
    )

    empty_count = 0

    def go_download(d, file):
                   
        page.launch_url(d[file])


    def go_token(d, type, filter, route, log):
        
        profile = page.client_storage.get("profile") 

        if log:
            profile.update({
                f"{type}": d,
                "logs": d,
                f"{filter}": list_filtros,
            })
        else:
            profile.update({
                f"{type}": d,
                f"{filter}": list_filtros,
            })


        page.client_storage.set("profile", profile)

        page.go(route)

    type_map = {
                "model": {
                    "key": "model",
                    "filter": "models_filter",
                    "route": "/models/token",
                    "file": "dwg",
                },
                "delivery": {
                    "key": "delivery",
                    "filter": "deliveries_filter",
                    "route": "/deliveries/token",
                    "file": "dwg",
                },
                "file": {
                    "key": "file",
                    "filter": "files_filter",
                    "route": "/files/token",
                    "file": "url",
                },
                "freelancer": {
                    "key": "freelancer",
                    "filter": "freelancers_filter",
                    "route": "/freelancers/token",
                },
                "log": {
                    "key": "logs",
                    "filter": "logs_filter",
                    "route": "/logs/token",
                },
                "lisp": {
                    "key": "lisp",
                    "filter": "lisps_filter",
                    "route": "/lisps/token",
                    "file": "lisp",
                },
                "city": {
                    "key": "city",
                    "filter": "city_filter",
                    "route": "/city/token",
                },
            }

    for h in headers:

        if h == "":
            empty_count += 1

            if page_type in ["model", "delivery", "file"]:

                # Primeiro botão vazio = DOWNLOAD
                if empty_count == 1:
                    cells.append(
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DOWNLOAD,
                                icon_color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.AMBER,
                                on_click=lambda e,
                                                d=d,
                                                file=type_map[page_type]["file"]: go_download(d, file),
                            )
                        )
                    )

                # Segundo botão vazio = SEARCH
                elif empty_count == 2:
                    cells.append(
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                icon_color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE,
                                on_click=lambda e,
                                                d=d,
                                                type=type_map[page_type]["key"],
                                                filter=type_map[page_type]["filter"],
                                                route=type_map[page_type]["route"],
                                                log=True: go_token(d, type, filter, route, log),
                            )
                        )
                    )

            elif page_type in ["lisp"]:
                cells.append(
                    ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DOWNLOAD,
                                icon_color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.AMBER,
                                on_click=lambda e,
                                                d=d,
                                                file=type_map[page_type]["file"]: go_download(d, file),
                            )
                        )
                )

            elif page_type in ["freelancer"]:
                cells.append(
                            ft.DataCell(
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Container(
                                            width=40,
                                            height=40,
                                            alignment=ft.alignment.center,
                                            content=ft.Image(  # Mova a imagem para o content
                                                src=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/freelancers//{d.get("username", "")}.jpg",  
                                                fit=ft.ImageFit.COVER,
                                                expand=True,
                                            ),
                                            border=ft.Border(
                                                left=ft.BorderSide(2, ft.Colors.BLACK),  
                                                top=ft.BorderSide(2, ft.Colors.BLACK),    
                                                right=ft.BorderSide(2, ft.Colors.BLACK), 
                                                bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                                            ),
                                            bgcolor=ft.Colors.BLACK,
                                            border_radius=ft.border_radius.all(20),
                                            clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                        )
                                    ]
                                )
                            )
                        )

            else:
                cells.append(
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.Icons.CHECK,
                            bgcolor=ft.Colors.GREEN if check == "yes" else ft.Colors.GREY,
                            icon_color=ft.Colors.WHITE,
                            expand=True,
                            on_click=toggle_check,
                        )
                    )
                )

        elif h == "Ficha":
            cells.append(
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                icon_color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE,
                                on_click=lambda e,
                                                d=d["username"],
                                                type=type_map[page_type]["key"],
                                                filter=type_map[page_type]["filter"],
                                                route=type_map[page_type]["route"],
                                                log=False: go_token(d, type, filter, route, log),
                            )
                        )
                    )
        else:
            key = field_map.get(h)
            value = d.get(key, "")
            cells.append(text_cell(value))


    return row




