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
    btn_see_lisps = buttons.create_button(on_click=lambda e: go_url("/lisps"),
                                            text= "Lisps",
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
        btn_see_lisps,
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

def update_pagination_bar(pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True):

        total_pages = (len(visible_rows) + items_per_page - 1) // items_per_page

        visible_pages = 4
        many_pages = True

        if total_pages < visible_pages:
            many_pages = False
            visible_pages = total_pages 

        pagination_bar.controls.clear()

        if many_pages:
            pagination_bar.controls.append(
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=ft.Colors.INDIGO_600,
                    disabled=current_page[0] == 1,
                    visible=current_page[0] != 1,
                    on_click=lambda e: load_page((current_page[0] - 1), pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                )
            )

        # Números
        initial_number = current_page[0]
        last_number = current_page[0] + visible_pages

        def color_button(page):
            if page == current_page[0]:
                color = ft.Colors.AMBER
            else:
                color = ft.Colors.INDIGO_600
            
            return color

        for page in range(initial_number, last_number):
            pagination_bar.controls.append(
                ft.ElevatedButton(
                    text=str(page),
                    bgcolor = color_button(page),
                    color = ft.Colors.WHITE,
                    on_click=lambda e, p=page: load_page(p, pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                )
            )

        # Limitar a ultima página
        if current_page[0] + visible_pages > total_pages:
            pagination_bar.controls.clear()
            initial_page = 1
            final = total_pages + 1

            if many_pages:
                initial_page = total_pages - visible_pages
                final = total_pages + 1
                pagination_bar.controls.append(
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        icon_color=ft.Colors.INDIGO_600,
                        on_click=lambda e: load_page((current_page[0] - 1), pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                    )
                )


            for page in range(initial_page, final):
                pagination_bar.controls.append(
                    ft.ElevatedButton(
                        text=str(page),
                        bgcolor = color_button(page),
                        color = ft.Colors.WHITE,
                        on_click=lambda e, p=page: load_page(p, pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                    )
                )
            

        if many_pages:
            # Botão "Próximo"
            pagination_bar.controls.append(
                ft.IconButton(
                    icon=ft.Icons.ARROW_FORWARD,
                    icon_color=ft.Colors.INDIGO_600,
                    disabled=current_page[0] == total_pages,
                    visible=current_page[0] != total_pages,
                    on_click=lambda e: load_page((current_page[0] + 1), pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                )
            )

        if current_page[0] <= total_pages - visible_pages and many_pages:
            pagination_bar.controls.insert(-1,
                ft.ElevatedButton(
                        text=str(f"{total_pages}"),
                        bgcolor = color_button(current_page[0] + 1),
                        color = ft.Colors.WHITE,
                        on_click=lambda e, p=page: load_page(total_pages, pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                    )
            ) 

        if current_page[0] != 1 and many_pages:
            pagination_bar.controls.insert(1,
                ft.ElevatedButton(
                        text=str("1"),
                        bgcolor = color_button(current_page[0] + 1),
                        color = ft.Colors.WHITE,
                        on_click=lambda e, p=page: load_page(1, pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True)
                    )
            )

        # Atualiza label "Total de registros"
        lbl_total.value = f"{len(table.rows)} itens de {len(visible_rows)}"
        if initial:
            lbl_total.update()
            pagination_bar.update()

def load_page(page, pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=True):

        current_page[0] = page

        start = (page * items_per_page) - items_per_page
        end = start + items_per_page

        visible_rows.clear()
        for item in all_rows:
            if item.visible:
                visible_rows.append(item)
    
        table.rows = visible_rows[start:end]
        if initial:
            table.update()
        update_pagination_bar(pagination_bar, current_page, visible_rows, items_per_page, lbl_total, table, all_rows, initial=initial)

def add_rows(
        page,
        all_rows,
        get_json,
        dicio_projects,
        list_filtros,
        type,
        headers,
        field_map,
        subproject_key="subproject",
    ):
        def go_download(d):
            if d.get("dwg"):
                page.launch_url(d["dwg"])
            else: 
                page.launch_url(d["lisp"])

        def go_token(d):
            profile = page.client_storage.get("profile") or {}

            payload = {**d, "dwg": d.get("dwg") or ""}

            type_map = {
                "model": {
                    "key": "model",
                    "filter": "models_filter",
                    "route": "/models/token",
                },
                "delivery": {
                    "key": "delivery",
                    "filter": "deliveries_filter",
                    "route": "/deliveries/token",
                },
                "file": {
                    "key": "file",
                    "filter": "files_filter",
                    "route": "/files/token",
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
                },
            }

            cfg = type_map[type]

            if type != "model":
                
                profile.update({
                    cfg["key"]: payload,
                    cfg["filter"]: list_filtros,
                })

            else:
                profile.update({
                    cfg["key"]: payload,
                    "logs": payload,
                    cfg["filter"]: list_filtros,
                })


            page.client_storage.set("profile", profile)
            page.go(cfg["route"])

        def text_cell(value, d, data=None):
            return ft.DataCell(
                ft.Text(
                    value=str(value),
                    theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BLACK,
                    expand=True,
                    data=data,
                ),
                on_long_press=lambda e, d=d: go_token(d),
            )

        def icon_cell(icon, color, action, d):
            return ft.DataCell(
                ft.IconButton(
                    icon=icon,
                    bgcolor=color,
                    icon_color=ft.Colors.WHITE,
                    expand=True,
                    on_click=lambda e, d=d: action(d),
                ),
                on_long_press=lambda e, d=d: action(d),
            )

        for d in get_json:

            # Project seguro (quando existir dicio_projects)
            if dicio_projects:
                project = next(
                    (
                        k for k, v in dicio_projects.items()
                        if any(d.get(subproject_key, "").startswith(i) for i in v)
                    ),
                    None,
                )
            else:
                project = None

            polygons = int(d.get("polygons", 0))
            numbers = int(d.get("numbers", 0))
            percent = int(numbers / (polygons / 100)) if polygons else 0

            cells = []

            empty_headers = headers.count("")

            for h in headers:

                if h == "%":
                    cells.append(text_cell(f"{percent}%", d))

                elif h == "":
                    # Caso exista apenas UM header vazio
                    if empty_headers == 1:
                        cells.append(
                            icon_cell(ft.Icons.DOWNLOAD, ft.Colors.AMBER, go_download, d)
                        )

                    # Caso existam DOIS ou mais headers vazios
                    else:
                        filled_cells = len([c for c in cells if isinstance(c, ft.DataCell)])

                        if filled_cells == len(headers) - 2:
                            cells.append(
                                icon_cell(ft.Icons.DOWNLOAD, ft.Colors.AMBER, go_download, d)
                            )
                        else:
                            cells.append(
                                icon_cell(ft.Icons.SEARCH, ft.Colors.BLUE, go_token, d)
                            )

                else:
                    key = field_map.get(h)
                    value = d.get(key, "") if key else ""
                    cells.append(
                        text_cell(
                            value,
                            d,
                            project if h == "Subprojeto" else None
                        )
                    )

            all_rows.append(ft.DataRow(cells=cells))

def build_list_dropdown(
        on_dropdown_change,
        filtros_config,
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

def build_filtro_tabela(
    all_rows,
    filtros_ativos,
    list_filtros,
    load_page,
    pagination_bar,
    current_page,
    visible_rows,
    items_per_page,
    lbl_total,
    table,
    update
    ):

        def aplicar_filtros(update=update):

            def safe_cell_value(cells, idx, default=None):
                    try:
                        cell = cells[idx]
                        return getattr(cell.content, "value", default)
                    except Exception:
                        return default


            def safe_cell_data(cells, idx, default=None):
                try:
                    return getattr(cells[idx].content, "data", default)
                except Exception:
                    return default

            for item in all_rows:

                cells = item.cells

                # Segurança para data
                date_value = safe_cell_value(cells, 1)
                if isinstance(date_value, str) and "/" in date_value:
                    dia, mes, ano = date_value.split("/")
                else:
                    dia = mes = ano = None

                dados_linha = {
                    "dia": dia,
                    "mes": mes,
                    "ano": ano,
                    "usuario": safe_cell_value(cells, 0),
                    "projeto": safe_cell_data(cells, 2),
                    "subprojeto": safe_cell_value(cells, 2),
                    "status": safe_cell_value(cells, 5),
                    "name": safe_cell_value(cells, 0),
                    "type": safe_cell_value(cells, 1),
                }

                # aplica apenas filtros existentes no dict
                item.visible = all(
                    valor is None or
                    (
                        dados_linha.get(chave) is not None and
                        (
                            dados_linha[chave].startswith(valor)
                            if isinstance(valor, str) and chave == "subprojeto"
                            else dados_linha[chave] == valor
                        )
                    )
                    for chave, valor in filtros_ativos.items()
                )

            load_page(
                1,
                pagination_bar,
                current_page,
                visible_rows,
                items_per_page,
                lbl_total,
                table,
                all_rows,
                initial=update,
            )

            list_filtros[0] = filtros_ativos

        return aplicar_filtros


