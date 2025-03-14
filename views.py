import flet as ft
from models import *
import flet.map as map
from datetime import datetime
from datetime import datetime


def create_page_login(page):

    container = []

    #Login//Photo
    block = ft.Image(
        src="https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/images//attam.jpeg",
        repeat=ft.ImageRepeat.NO_REPEAT,
        data=0,
        height=100
    )
         #Login//User
    login = ft.TextField(
        label= "User",
        bgcolor= ft.colors.WHITE,
        text_style= ft.TextStyle(color=ft.colors.BLACK),
        border_radius= 0,
        
    )    
         #Login//Password
    password = ft.TextField(
        label= "Code",
        bgcolor= ft.colors.WHITE,
        text_style= ft.TextStyle(color=ft.colors.BLACK),
        border_radius= 0,
        password= True, 
        can_reveal_password= True,
    )
         #Login//Enter
    Send = ft.ElevatedButton(text="Enter",
        bgcolor= ft.colors.GREEN_100,
        color= ft.colors.GREEN,
        on_click=lambda e: verificar(login.value, password.value, page)
    )
    logo = ft.Image(
        src="https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/images//acess.jpg",
        repeat=ft.ImageRepeat.NO_REPEAT,
        data=0,
        height=200,
    )
    area = ft.Container(
        bgcolor= ft.colors.WHITE,
        height= 500,
        width= 500,
        padding= 20,
        border_radius= 30,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=25,
            color=ft.Colors.BLACK,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
        content=(ft.Column(
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            expand= True,
            spacing= 20,
            controls=[block, login, password, Send, logo],
            scroll=ft.ScrollMode.AUTO
                ))

    )

    block2 = ft.Column(
        controls =[area], 
        alignment= ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        expand= True,
        spacing= 20,
       
    )

    container.append(area)

    return ft.ResponsiveRow(
        columns=12,
        controls=[
            block2             
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

def create_page_user(page):

    loading = LoadingPages(page)
    web_images = Web_Image(page)
    forms = Forms(page)
    geo_objects = Objects(page)
    textthemes = TextTheme()
    buttons = Buttons(page)
    sp = SupaBase(page)
    texttheme1 = textthemes.create_text_theme1()
    profile = CurrentProfile() 
    dict_profile = profile.return_current_profile()

    url_imagem1 = web_images.get_image_url(name="perfil")

    perfil = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ft.Container(
                width=200,
                height=200,
                alignment=ft.alignment.center,
                image=ft.Image(
                src=url_imagem1,  
                ),
                bgcolor=ft.Colors.GREY,
                border=ft.Border(
                    left=ft.BorderSide(2, ft.Colors.BLACK),  
                    top=ft.BorderSide(2, ft.Colors.BLACK),    
                    right=ft.BorderSide(2, ft.Colors.BLACK), 
                    bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                ),
                border_radius=ft.border_radius.all(100),
            )
            ]
        )

    #....................................................................

    total_deliverys = sp.get_deliverys_data_total(username=dict_profile["username"])
    data_total_deliverys = total_deliverys.json()
    
    total_polygons = 0
    total_errors = 0
    total_delays = 0
    number_total_deliverys = 0

    for row in data_total_deliverys:

        id = row["id"]
        date = row["date"]
        name_subproject = row["name_subproject"]
        polygons = row["polygons"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]

        number_total_deliverys += 1
        total_polygons += int(polygons)
        total_errors += int(errors)

        if delay == "Sim":
            total_delays += 1

    #....................................................................

    current_deliverys = sp.get_deliverys_data(subproject=dict_profile["current_project"])
    data_current_deliverys = current_deliverys.json()
    
    dicio_current_deliverys = {}
    subproject_polygons = 0
    number_current_deliverys = 0

    date_cash = "07/03/2025"
    last_date = "07/02/2025"
    data_atual = datetime.now()
    data_cash_dt = datetime.strptime(date_cash, "%d/%m/%Y")
    last_date_dt = datetime.strptime(last_date, "%d/%m/%Y")
    data_formatada = data_atual.strftime("%d/%m/%Y")

    cash_polygons = 0
    cash_photos = 0

    temp_list = []

    for row in data_current_deliverys:

        id = row["id"]
        date = row["date"]
        name_subproject = row["name_subproject"]
        polygons = row["polygons"]
        photos = row["photos"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]

        date_delivery_dt = datetime.strptime(date, "%d/%m/%Y")

        linha = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(value=date, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=name_subproject, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=polygons, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=photos, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=errors, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=discount, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text(value=delay, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER)),
                    ])

        if last_date_dt < date_delivery_dt and date_delivery_dt < data_cash_dt:
            cash_polygons += (int(polygons) - int(discount))
            cash_photos += int(photos) 

        temp_list.append((date_delivery_dt, linha))

        number_current_deliverys += 1
        subproject_polygons += int(polygons)

    # Ordena a lista pela data (mais recente primeiro)
    temp_list.sort(reverse=True, key=lambda x: x[0])

    # Cria uma lista ordenada para ser usada no Flet
    dicio_current_deliverys = [linha for _, linha in temp_list]

    #....................................................................

    user2 = sp.get_user_data(username=dict_profile["username"])
    data2 = user2.json()
    row2 = data2[0]
    row2["weekly_deliveries"] = number_total_deliverys
    row2["polygons_made"] = total_polygons
    row2["polygons_wrong"] = total_errors
    row2["delays"] = total_delays


    subproject3 = sp.get_subproject_data(subproject=dict_profile["current_project"])
    data3 = subproject3.json()
    row3 = data3[0]
    row3["lots_done"] = subproject_polygons
    percent = (subproject_polygons * 100) / (int(row3["predicted_lots"]))
    row3["percent"] = f"{percent:.2f} %"
    current_average = subproject_polygons / number_current_deliverys
    row3["current_average"] = f"{current_average:.2f}"

    total_cash_polygons = float(cash_polygons) * 0.50
    total_cash_photos = float(cash_photos) * 0.20
    total_cash = f"{(total_cash_polygons + total_cash_photos):.2f}"

    table1 = geo_objects.view_user_data(row2)
    table2 = geo_objects.view_user_data2(row3)
    table3 = geo_objects.view_user_data3(cash_polygons, cash_photos, total_cash)
    form1 = forms.create_forms_post(table1, "Informções", "Freelancer", ft.MainAxisAlignment.START)
    form2 = forms.create_forms_post(table2, "Informações", "Projeto", ft.MainAxisAlignment.START)

    
    form3 = forms.create_forms_post(table3, "Pagamento", date_cash, ft.MainAxisAlignment.START)


    form4 = ft.Column(
        controls=[
            ft.Container(
                padding=0,  
                expand=True,  
                theme=texttheme1,
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=40,  
                    expand=True,  
                    columns=[
                        ft.DataColumn(ft.Text(value="Data", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Poligonos", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Fotos", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Erros", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Desconto", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Atraso", text_align=ft.TextAlign.CENTER)),  
                    ],
                    rows=dicio_current_deliverys,  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=300,  
        expand=True,  
    )

    url_imagem1 = sp.get_storage()
    ortofoto = web_images.create_web_image(src=url_imagem1)
    container_ortofoto = ft.Container(content=(ortofoto), border_radius=20)

    btn_exit = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page)),
                                      text="Sair",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5,)


    container1 = ft.Container(content=ft.Column(controls=[perfil, ft.Text(value=dict_profile["name"], color=ft.Colors.WHITE), btn_exit],
                                                 alignment=ft.MainAxisAlignment.CENTER,
                                                 horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                              alignment=ft.alignment.center,
                              col=12,
                              )
    


    container_form1 = ft.Container(content=form1,
                                    alignment=ft.alignment.top_center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 4},
                                    )
    container_form2 = ft.Container(content=form2,
                                    alignment=ft.alignment.top_center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 4},
                                    )
    container_form3 = ft.Container(content=form3,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 4},
                                    )
    container2 = ft.Container(content=ft.ResponsiveRow(controls=[container_form1, container_form2, container_form3],
                                                 alignment=ft.MainAxisAlignment.CENTER,
                                                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                 spacing=10,
                                                 ),
                                                 
                              alignment=ft.alignment.center,
                              col=12,
                              )
    

    container_ortofoto2 = ft.Container(content=container_ortofoto,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 4},
                                    )
    container_form4 = ft.Container(content=form4,
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 8},
                                    )
    container3 = ft.Container(content=ft.ResponsiveRow(controls=[container_ortofoto2, container_form4],
                                                 alignment=ft.MainAxisAlignment.CENTER,
                                                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                 spacing=10,
                                                 ),
                                                 
                              alignment=ft.alignment.center,
                              col=12,
                              )

    

    return ft.ResponsiveRow(
        col=12,
        expand=True,
        controls=[container1, container2, container3],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

def create_page_initial_adm(page):

    page.bgcolor = ft.Colors.GREY_500

    sp = SupaBase(page)
    buttons = Buttons(page)
    loading = LoadingPages(page)

    freelancer_data = []

    request_user = sp.get_all_user_data()
    data_users = request_user.json()


    btn_exit = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page)),
                                      text="Logout",
                                      color=ft.Colors.RED,
                                      col=12,
                                      padding=5,)
    btn_projeto = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_project(page)),
                                      text= "Projetos",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=5,)       
                                        
    drawer = ft.NavigationDrawer(


        controls=[

            ft.Divider(thickness=1),
            btn_projeto,
                        
            ft.Divider(thickness=1),
            btn_exit,
            ]
            )
        
    


    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.MENU, on_click=lambda e:page.open(drawer))],
        
        
    )


    for row in data_users:

        permission = row["permission"]
        name_freelancer = row["name"]
        all_names = name_freelancer.split(" ")
        first_name = all_names[0]
        current_subproject = row["current_project"]

        if permission == "adm":
            continue

        if current_subproject == ".":

            linha = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(value=first_name, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        #ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        #ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),    
                    ])

            freelancer_data.append(linha)

            continue


        subproject = sp.get_subproject_data(subproject=current_subproject)
        data_subproject = subproject.json()
        row2 = data_subproject[0]
        total_deliverys_subproject = row2["deliverys"]
        recommended_medium_subproject = row2["recommended_medium"]

        polygons_made = 0
        delay_made  = 0
        current_deliverys_made = 0
        current_deliverys = sp.get_deliverys_data(current_subproject)
        data_current_deliverys = current_deliverys.json()
        if data_current_deliverys == []:
            polygons_made = 1
            current_deliverys_made = 1
        else:
            for row in data_current_deliverys:

                polygons = row["polygons"]
                delay = row["delay"]
                photos = row["photos"]
                polygons_made += int(polygons)
                if delay =="Sim":
                    delay_made += 1
                if int(photos) == 0:
                    current_deliverys_made += 1

        average_deliverys = polygons_made / current_deliverys_made
        polygons_recommended = current_deliverys_made * int(recommended_medium_subproject)
        missing_lots = (current_deliverys_made * int(recommended_medium_subproject)) - polygons_made
        if missing_lots < 0:
            missing_lots = 0


        linha = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(value=first_name, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=current_subproject, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        #ft.DataCell(ft.Text(value=f"{int(average_deliverys)} / {recommended_medium_subproject}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),
                        ft.DataCell(ft.Text(value=f"{int(polygons_made)} / {polygons_recommended} / {missing_lots}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        #ft.DataCell(ft.Text(value=missing_lots, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),
                        ft.DataCell(ft.Text(value=f"{current_deliverys_made} / {total_deliverys_subproject} / {recommended_medium_subproject}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),    
                    ])

        if average_deliverys < int(recommended_medium_subproject):
            linha.cells[2].content.color = ft.Colors.RED


        freelancer_data.append(linha)


    form4 = ft.Column(
        controls=[
            ft.Container(
                padding=0,  
                expand=True,  
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=30,  
                    expand=True,  
                    columns=[
                        ft.DataColumn(ft.Text(value="Nome", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                        #ft.DataColumn(ft.Text(value="Média", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),  
                        ft.DataColumn(ft.Text(value="Poligonos", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                        #ft.DataColumn(ft.Text(value="Faltantes", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=10)),  
                        ft.DataColumn(ft.Text(value="Entregas", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                    ],
                    rows=freelancer_data,  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=300,  
        expand=True,  
    )


    request_projects = sp.get_all_project_data()
    data_projects = request_projects.json()

    projects_data = []

    for row in data_projects:

        name_project = row["name_project"]
        current_subprojects2 = row["current_subprojects"]
        predicted_lots = row["predicted_lots"]
        final_delivery = row["final_delivery"]

        list_current_subprojects = current_subprojects2.split(",")

        project_polygons = 0

        for item in list_current_subprojects:

            request = sp.get_deliverys_data(item)
            json_request = request.json()

            if len(json_request) == 0:
                polygons2 = 0
            else:
                for item2 in json_request:
                    polygons2 = item2["polygons"]
                    project_polygons += int(polygons2)

        percent_project = (int(project_polygons) * 100) / int(predicted_lots)

        linha2 = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(value=name_project, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{project_polygons} / {predicted_lots} ... {int(percent_project)}%", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{len(list_current_subprojects)}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{final_delivery}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),    
                    ])

        projects_data.append(linha2)


    form5 = ft.Column(
        controls=[
            ft.Container(
                padding=0,  
                expand=True,  
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=30,  
                    expand=True,  
                    columns=[
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                        ft.DataColumn(ft.Text(value="Lotes", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),   
                        ft.DataColumn(ft.Text(value="N°", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),   
                        ft.DataColumn(ft.Text(value="Entrega", text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),  
                    ],
                    rows=projects_data,  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=300,  
        expand=True,  
    )

    


    container_height = ((page.height) / 1.3)

    container1 = ft.Container(
        content=form4,
        bgcolor=ft.colors.GREY_200,
        padding=30,
        alignment=ft.alignment.top_center,
        expand=True,
        height=container_height,
        border_radius=20,
        col={"xs" : 12, "lg" : 6},
    )

    container2 = ft.Container(
        content=form5,
        bgcolor=ft.colors.WHITE,
        padding=30,
        alignment=ft.alignment.top_center,
        expand=True,
        height=container_height,
        border_radius=20,
        col={"xs" : 12, "lg" : 6},
    )


    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
           
            container1,
            container2
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
        spacing=20,
    )

    return layout

def verificar(username, password, page):

    loading = LoadingPages(page)
    sp = SupaBase(page)

    response = sp.check_login(username=username, password=password)

    if response.status_code == 200 and len(response.json()) > 0:

        data = response.json()
        row = data[0]
        name = row["name"]
        user_name = row["username"]
        permission = row["permission"]
        current_project = row["current_project"]
        
        profile = CurrentProfile()
        profile.add_name(name)
        profile.add_username(user_name)
        profile.add_permission(permission)
        profile.add_current_project(current_project)

        if permission == "user":

            loading.new_loading_page(page=page,
            call_layout=lambda:create_page_user(page),
            )

        else:

            loading.new_loading_page(page=page,
            call_layout=lambda:create_page_initial_adm(page),
            )
        
    else:
        # Exibe mensagem de erro se as credenciais não forem encontradas
        snack_bar = ft.SnackBar(
            content=ft.Text("Login ou senha incorretos"),
            bgcolor=ft.Colors.RED
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

def create_page_project(page):

    loading = LoadingPages(page=page)

    base = SupaBase(page=None)
    get_base = base.get_projects_data()
    get_json = get_base.json()

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))
    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))

    history_list = ft.ListView(
            controls=[

            ],
            expand=True,
            spacing=0,  # Removendo espaçamento entre os itens da lista
        )

    for city in get_json: 
        name_project = city["name_project"]

        def create_on_click(name):
            return lambda e: loading.new_loading_page(page=page,
                                                    call_layout= lambda:creat_page_subproject(page=page, project=name),
                                                    )

        history_list.controls.append(ft.ListTile(title=ft.Text(f"{name_project}"),
                                                 on_click=create_on_click(name_project)))
        


        # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back())],
        
        
    )

    # Campo de pesquisa
    search_field = ft.TextField(
        label="Pesquisar",
        hint_text="Digite para pesquisar...",
        border_color=ft.colors.BLUE_800,
        filled=True,
        bgcolor=ft.colors.WHITE,
        expand=False,
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column( 
            [
                ft.Text("Projetos", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
                search_field,
                history_list,
                # Lista colada ao campo de pesquisa
            ],
            expand=True,
            spacing=0,  # Removendo espaçamento entre os elementos da coluna
        ),
        bgcolor=ft.colors.WHITE,
        padding=10,  # Padding mínimo para o container
        border_radius=10,
        expand=True,
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},
                controls=[main_container],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o ResponsiveRow na página
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza verticalmente o ResponsiveRow
    )

    return layout

def creat_page_subproject(page, project):
    
    loading= LoadingPages(page=page)

    base = SupaBase(page=None)
    get_base = base.get_all_subproject_data(project)
    get_json = get_base.json()

     
    

    history_list = ft.ListView(
        controls=[],
        expand=True,
        spacing=0,  # Removendo espaçamento entre os itens da lista
    )

    for city in get_json: 
        name_subproject = city["name_subproject"]

        def create_on_click(subproject):
            return lambda e: loading.new_loading_page(page=page,
                                                    call_layout= lambda:create_ficha_supro(page=page, subproject=subproject, project=project),
                                                    )

        history_list.controls.append(ft.ListTile(title=ft.Text(f"{name_subproject}"), on_click=create_on_click(name_subproject)))



    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_project(page=page))
    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
    leading_width=40,
    center_title=True,
    title=ft.Text("Atta'm Soluções e Engenharia"),
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),ft.IconButton(ft.icons.KEYBOARD_RETURN, 
                                                        on_click=lambda e: go_back())],
    )

    # Campo de pesquisa
    search_field = ft.TextField(
    label="Pesquisar",
    hint_text="Digite para pesquisar...",
    border_color=ft.colors.BLUE_800,
    filled=True,
    bgcolor=ft.colors.WHITE,
    expand=True,  # Expande para ocupar o espaço disponível
    )

    # Container principal
    main_container = ft.Container(
    content=ft.Column(
        [
            ft.Text("Subprojetos de Cidades", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Row(
                controls=[search_field],
                expand=True,
            ),
            ft.Divider(height=20, color=ft.colors.TRANSPARENT),  # Espaçamento
            history_list,
        

        ],
        expand=True,
        spacing=10,
    ),
    bgcolor=ft.colors.WHITE,
    padding=20,
    border_radius=10,
    expand=True,
    )

    # Layout da página
    layout = ft.ResponsiveRow(
    columns=12,
    controls=[
        ft.Column(
            col={"sm": 12, "md": 8, "lg": 6},  # Define o tamanho do container em diferentes breakpoints
            controls=[main_container],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
        )
            
    ],
    )


    return layout

def create_ficha_supro(page, subproject, project):

    loading = LoadingPages(page=page)

    base = SupaBase(page=page)

    get_base_Project = base.get_subproject_data(subproject)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    get_base_user = base.get_user_data_SubPro(subproject)
    get_info3 = get_base_user.json()
    get_info4 = get_info3[0]

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: creat_page_subproject(page=page, project=project))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()), ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back())],
    )

    # Campos de entrada editáveis 
    nome_user_field = ft.TextField(label="Nome do Usuário", value=get_info4["username"], width=300)
    name_field = ft.TextField(label="Nome", value=get_info2["name_subproject"], width=300)
    lotes_previstos_field = ft.TextField(label="Lotes Previstos", value=get_info2["predicted_lots"], width=300)
    lotes_feitos_field = ft.TextField(label="Lotes Feitos", value=get_info2["lots_done"], width=300)
    entregas_field = ft.TextField(label="Entregas", value=get_info2["deliverys"], width=300)
    media_recomendada_field = ft.TextField(label="Média Recomendada", value=get_info2["recommended_medium"], width=300)
    porcentagem_field = ft.TextField(label="Porcentagem", value=get_info2["percent"], width=300)
    ortofoto_field = ft.TextField(label="Ortofoto", value=get_info2["ortofoto"], width=300)
    projeto_field = ft.TextField(label="Projeto", value=get_info2["project"], width=300)
    entrega_final_field = ft.TextField(label="Entrega Final", value=get_info2["final_delivery"], width=300)

    # Layout responsivo usando ft.ResponsiveRow
    ficha_subprojeto = ft.Column(
        [
            ft.Text("Ficha Subprojeto", size=24, weight=ft.FontWeight.BOLD),
            nome_user_field,
            name_field,
            lotes_previstos_field,
            lotes_feitos_field,
            entregas_field,
            media_recomendada_field,
            porcentagem_field,
            ortofoto_field,
            projeto_field,
            entrega_final_field,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
    )

    # FREELANCER
    nome = ft.TextField(label="Nome", value=get_info4["name"], width=300)
    usuario = ft.TextField(label="Usuario", value=get_info4["username"], width=300)
    projeto_atual = ft.TextField(label="Projeto_Atual", value=get_info4["current_project"], width=300)
    entrega_total = ft.TextField(label="Entrega_Total", value=get_info4["total_deliverys"], width=300)
    entrega_semanal = ft.TextField(label="Entregas_Semanais", value=get_info4["weekly_deliveries"], width=300)
    poligonos_feitos = ft.TextField(label="Poligonos_Feitos", value=get_info4["polygons_made"], width=300)
    poligonos_errados = ft.TextField(label="Poligonos_Errados", value=get_info4["polygons_wrong"], width=300)
    advertencias = ft.TextField(label="Advertencia", value=get_info4["warnings"], width=300)
    atrasos = ft.TextField(label="Atrasos", value=get_info4["delays"], width=300)
    senha = ft.TextField(label="Senha", value=get_info4["password"], width=300)
    permissao = ft.TextField(label="Permissão", value=get_info4["permission"], width=300)

    # Layout responsivo usando ft.ResponsiveRow
    ficha_cadastral = ft.Column(
        [
            ft.Text("Ficha Cadastral", size=24, weight=ft.FontWeight.BOLD),
            nome,
            usuario,
            projeto_atual,
            entrega_total,
            entrega_semanal,
            poligonos_errados,
            poligonos_feitos,
            advertencias,
            atrasos,
            senha,
            permissao,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
    )

    # Container em volta das fichas
    ficha_subprojeto_container = ft.Container(
        content=ficha_subprojeto,
        padding=20,  # Espaçamento interno
        border=ft.border.all(2, ft.colors.BLUE),  # Borda azul
        border_radius=10,  # Bordas arredondadas
        bgcolor=ft.colors.WHITE,  # Cor de fundo do container
        width=800 if page.width > 800 else page.width * 0.9, # Largura responsiva
        height=900,
    )

    ficha_cadastral_container = ft.Container(
        content=ficha_cadastral,
        padding=20,  # Espaçamento interno
        border=ft.border.all(2, ft.colors.BLUE),  # Borda azul
        border_radius=10,  # Bordas arredondadas
        bgcolor=ft.colors.WHITE,  # Cor de fundo do container
        width=800 if page.width > 800 else page.width * 0.9,  # Largura responsiva
        height=900, 
    )

    # Layout responsivo com as duas fichas lado a lado
    layout = ft.ResponsiveRow(
        [
            ft.Column([ficha_subprojeto_container], col={"sm": 13, "md": 6,}), 
            ft.Column([ficha_cadastral_container], col={"sm": 12, "md": 6}),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

# Adiciona o layout à página
    return layout


















































































































































































