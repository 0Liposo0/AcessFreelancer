import flet as ft
from models import *
import flet.map as map
from datetime import datetime
from datetime import datetime


def create_page_login(page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

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
#Página de Login    


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


    perfil = ft.Column(
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[
        ft.Container(
            width=200,
            height=200,
            alignment=ft.alignment.center,
            content=ft.Image(  # Mova a imagem para o content
                src=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/freelancers//{dict_profile["username"]}.jpg",  
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
            border_radius=ft.border_radius.all(100),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
        )
    ]
)

    #....................................................................
    #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas

    total_deliverys = sp.get_deliverys_data_total(username=dict_profile["username"])  
    data_total_deliverys = total_deliverys.json()
    
    total_polygons = 0  # Todos os poligonos que o usuario fez
    total_errors = 0  # Todos os erros que o usuario cometeu
    total_delays = 0  # Todos os atrasos que o usuario cometeu
    number_total_deliverys = 0  # Todos as entregas que o usuario fez

    for row in data_total_deliverys:  #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas

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

    #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas
    #....................................................................

    #....................................................................
    #Filtrando entregas baseado no projeto atual

    current_deliverys = sp.get_user_deliverys_data(subproject=dict_profile["current_project"], username=dict_profile["username"]) 
    data_current_deliverys = current_deliverys.json()
    
    dicio_current_deliverys = {}
    subproject_polygons = 0   # Todos os poligonos feitos no subprojeto   
    number_current_deliverys = 0  # Todos as entregas feitas no subprojeto

    date_cash = "07/03/2025"

    temp_list = [] 

    if dict_profile["current_project"] != ".":
        for row in data_current_deliverys:   #Filtrando entregas baseado no projeto atual

            date = row["date"]
            name_subproject = row["name_subproject"]
            polygons = row["polygons"]
            photos = row["photos"]
            errors = row["errors"]
            discount = row["discount"]
            delay = row["delay"]

            date_delivery_dt = datetime.strptime(date, "%d/%m/%Y")

            linha = ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=date, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=name_subproject, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=polygons, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=photos, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=errors, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=discount, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=delay, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                        ])

            temp_list.append((date_delivery_dt, linha))

            number_current_deliverys += 1
            subproject_polygons += int(polygons)

    # Ordena a lista pela data (mais recente primeiro)
    temp_list.sort(reverse=True, key=lambda x: x[0])

    # Cria uma lista ordenada para ser usada no Flet
    dicio_current_deliverys = [linha for _, linha in temp_list]

    #Filtrando entregas baseado no projeto atual
    #....................................................................


    #....................................................................
    # Processo de calculo financeiro

    cash_total_polygons = 0   
    cash_total_errors = 0
    cash_total_photos = 0
    cash_number_total_deliverys = 0
    delivery_07 = [0, 0]
    delivery_14 = [0, 0]
    delivery_21 = [0, 0]
    delivery_28 = [0, 0]

    if dict_profile["current_project"] != ".":
        for row in data_current_deliverys:

                date = row["date"]
                polygons = row["polygons"]
                errors = row["errors"]
                discount = row["discount"]
                delay = row["delay"]
                photos = row["photos"]

                data_obj = datetime.strptime(date, "%d/%m/%Y")

                if data_obj.month == 2 and data_obj.year == 2025:

                    cash_total_polygons += int(polygons)
                    cash_total_errors += int(errors)
                    cash_total_photos += int(photos)
                    cash_number_total_deliverys += 1


                    def add_polygons(delivery, polygons):
                        delivery[0] = polygons

                    def add_photos(delivery, photos):
                        delivery[1] = photos

                    dicio1 = {
                        7: lambda: add_polygons(delivery_07, int(polygons)),
                        14: lambda: add_polygons(delivery_14, int(polygons)),
                        21: lambda: add_polygons(delivery_21, int(polygons)),
                        28: lambda: add_polygons(delivery_28, int(polygons)),
                    }
                    dicio2 = {
                        7: lambda: add_photos(delivery_07, int(photos)),
                        14: lambda: add_photos(delivery_14, int(photos)),
                        21: lambda: add_photos(delivery_21, int(photos)),
                        28: lambda: add_photos(delivery_28, int(photos)),
                    }

                    call_function1 = dicio1.get(data_obj.day, lambda: None)()
                    call_function2 = dicio2.get(data_obj.day, lambda: None)()

    # Processo de calculo financeiro
    #....................................................................


    #....................................................................
    # Atualizando dados do usuario

    user2 = sp.get_user_data(users=dict_profile["username"])   
    data2 = user2.json()
    row2 = data2[0]
    row2["weekly_deliveries"] = number_total_deliverys
    row2["polygons_made"] = total_polygons
    row2["polygons_wrong"] = total_errors
    row2["delays"] = total_delays

    # Atualizando dados do usuario
    #....................................................................

    #....................................................................
    # Atualizando dados do subprojeto atual

    if dict_profile["current_project"] != ".":
        subproject3 = sp.get_subproject_data(subproject=dict_profile["current_project"]) 
        data3 = subproject3.json()
        row3 = data3[0]
        row3["lots_done"] = subproject_polygons
        percent = (subproject_polygons * 100) / (int(row3["predicted_lots"]))
        row3["percent"] = f"{percent:.2f} %"
        current_average = 0
        if number_current_deliverys != 0:
            current_average = subproject_polygons / number_current_deliverys

        row3["current_average"] = f"{current_average:.2f}"

    # Atualizando dados do subprojeto atual
    #....................................................................

    #....................................................................
    # Atualizando dados financeiros

    total_cash_polygons = float((delivery_07[0]+delivery_14[0]+delivery_21[0]+delivery_28[0]) * 0.50)
    total_cash_photos = float((delivery_07[1]+delivery_14[1]+delivery_21[1]+delivery_28[1]) * 0.20)
    total_cash = f"{(total_cash_polygons + total_cash_photos):.2f}"
    total_cash_polygons_made = int((delivery_07[0]+delivery_14[0]+delivery_21[0]+delivery_28[0]))
    total_cash_photos_made = int((delivery_07[1]+delivery_14[1]+delivery_21[1]+delivery_28[1]))

    # Atualizando dados financeiros
    #....................................................................

    #....................................................................
    # Texto de verificação de entrega

    text_date_file = []
    test = ft.Text(value="")
    text_date_file.append(test)

    def change_text_date(text_date_file):

        date_file = datetime.now().day

        dias = {
        i: 7 if i > 28 or i <= 7 else 
        14 if i > 7 and i <= 14 else 
        21 if i > 14 and i <= 21 else 
        28 
        for i in range(1, 32)
        }

        day_date_file = f"{dias[date_file]}/{datetime.now().strftime("%m")}/{datetime.now().year}"

        request_date_file = sp.check_file(date=day_date_file, username=dict_profile["username"])

        if len(request_date_file.json()) > 0:
            text_date_file[0].value = f"Entrega de {day_date_file} realizada"
            text_date_file[0].color = ft.colors.GREEN
        else:
            text_date_file[0].value = f"Entrega de {day_date_file} não realizada"
            text_date_file[0].color = ft.colors.RED
            
        page.update()

    change_text_date(text_date_file)    

    # Texto de verificação de entrega
    #....................................................................

    #....................................................................
    # Criação de tabelas

    # Tabela do Usuario
    table1 = geo_objects.view_user_data(row2)
    form1 = forms.create_forms_post(table1, "Informções", "Freelancer", ft.MainAxisAlignment.START)

    # Tabela do subprojeto
    table2 = ft.Container()
    if dict_profile["current_project"] != ".":
        table2 = geo_objects.view_user_data2(row3)
    form2 = ft.Container()
    if dict_profile["current_project"] != ".":
        form2 = forms.create_forms_post(table2, "Informações", "Projeto", ft.MainAxisAlignment.START)

    # Tabela do Financeiro
    table3 = geo_objects.view_user_data3(total_cash_polygons_made, total_cash_photos_made, total_cash)
    form3 = forms.create_forms_post(table3, "Pagamento", date_cash, ft.MainAxisAlignment.START)

    
    # Tabela das entregas
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

    # Tabela da ortofoto
    url_imagem1 = sp.get_storage()
    ortofoto = web_images.create_web_image(src=url_imagem1)
    container_ortofoto = ft.Container(content=(ortofoto), border_radius=20)

    # Criação de tabelas
    #....................................................................

    #....................................................................
    # Inserção de arquivo

    def send_file(file_path, name_file):

        container = page.overlay[1]
        
        response = sp.add_file_storage(file_path, name_file)

        if response.status_code == 200 or response.status_code == 201:
            id = str(sp.get_file_id())

            response2 = sp.post_to_files(
                                        id=id,   
                                        date=container.controls[0].content.controls[3].value,
                                        username=dict_profile["username"],
                                        subproject=dict_profile["current_project"],
                                        type=container.controls[0].content.controls[5].value,
                                        amount=container.controls[0].content.controls[7].value,
                                        url=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/files//{name_file}"
                                        )

            if response2.status_code == 200 or response2.status_code == 201:
                snack_bar = ft.SnackBar(
                content=ft.Text(value="Arquivo enviado", color=ft.Colors.BLACK),
                duration=2000,
                bgcolor=ft.Colors.GREEN,
                data="bar",
                )
                page.overlay.append(snack_bar)
                snack_bar.open = True
                change_text_date(text_date_file)
                overlay_copy = list(page.overlay)
                for item in overlay_copy:
                    if item.data == "fp" or item.data == "bar":
                            pass
                    else:
                        page.overlay.remove(item)
                page.update()
            else:
                snack_bar = ft.SnackBar(
                content=ft.Text(value="Falha ao enviar arquivo", color=ft.Colors.BLACK),
                duration=2000,
                bgcolor=ft.Colors.RED,
                data="bar",
                )
                page.overlay.append(snack_bar)
                snack_bar.open = True
                overlay_copy = list(page.overlay)
                for item in overlay_copy:
                    if item.data == "fp" or item.data == "bar":
                            pass
                    else:
                        page.overlay.remove(item)
                page.update()


    def on_image_selected(e: ft.FilePickerResultEvent):

            if not e.files or len(e.files) == 0:
                return
            
            file_selected = []
            file_selected.append(e.files[0])
            name = e.files[0].name

            def get_uploaded_file_bytes():

                file_path = f"uploads/{name}"    

                with open(file_path, "rb") as file:
                    file_content = file.read()

                file_selected.clear()
                file_selected.append(file_content)


            if e.page.web:
                #  Gerar a URL temporária
                temp_url = e.page.get_upload_url(file_selected[0].name, 3600)

                #  Criar objeto para upload
                file_upload = ft.FilePickerUploadFile(file_selected[0].name, temp_url)

                #  Realiza o upload
                fp.upload([file_upload])

                #  Chama a função para baixar os bytes do arquivo após o upload
                get_uploaded_file_bytes()
            
            
            data = (datetime.now().strftime("%d/%m/%Y")).replace("/", "")
            name_file = f'{dict_profile["username"]}_{data}.dwg'
            
            btn_send = buttons.create_button(on_click=lambda e: send_file(file_selected[0], name_file),
                                      text="Enviar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5
                        )
            
            def close():
                overlay_copy = list(page.overlay)
                for item in overlay_copy:
                    if item.data == "fp":
                            pass
                    else:
                        page.overlay.remove(item)
                page.update()

            btn_exit = buttons.create_button(on_click=lambda e: close(),
                                      text="Sair",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5
                        )

            container = ft.Row(
                controls=[ ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value=f"{name}", color=ft.Colors.BLACK),
                                        ft.Text(value="", color=ft.Colors.BLACK),
                                        ft.Text(value="Data da entrega:", color=ft.Colors.BLACK),
                                        ft.Dropdown(
                                            options=[
                                                ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                                ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                                ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                                ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                            ],
                                            text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                            bgcolor=ft.Colors.WHITE,
                                        ),
                                        ft.Text(value="Tipo de entrega:", color=ft.Colors.BLACK),
                                        ft.Dropdown(
                                            options=[
                                                ft.dropdown.Option("Poligonos"),
                                                ft.dropdown.Option("Fotos"),
                                            ],
                                            text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                            bgcolor=ft.Colors.WHITE,
                                        ),
                                        ft.Text(value="Quantidade:", color=ft.Colors.BLACK),
                                        ft.TextField(
                                            bgcolor=ft.Colors.WHITE,
                                            text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                            border_radius=0,
                                        ),
                                        btn_send,
                                        btn_exit, 
                                    ],
                                ),
                                bgcolor=ft.Colors.GREY,
                                border_radius=20,
                                alignment=ft.alignment.center,
                                width=300,
                                height=500,
                                padding=10,
                                col=6,   
                            )
                        ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            

            page.overlay.append(container)
            page.update()


    fp = ft.FilePicker(on_result=on_image_selected, data="fp")
    page.overlay.append(fp)

    def open_gallery(e): 
        fp.pick_files(              
            allow_multiple=False,
        )

    # Inserção de arquivo
    #....................................................................

    btn_send = buttons.create_button(on_click=open_gallery,
                                      text="Enviar arquivo",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
    
    btn_exit = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page)),
                                      text="Sair",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5,)


    container1 = ft.Container(content=ft.Column(controls=[perfil, ft.Text(value=dict_profile["name"], color=ft.Colors.WHITE), btn_send, btn_exit],
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
    container_form3 = ft.Container(content=ft.Column(controls=[text_date_file[0], form3],
                                                     alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    spacing=30,
                                                    ),
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
# Pagina de Usuario


def create_page_initial_adm(page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    page.bgcolor = ft.Colors.GREY_200

    sp = SupaBase(page)
    buttons = Buttons(page)
    loading = LoadingPages(page)

    
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
    btn_new_free = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_new_freelancer(page)),
                                        text= "Cadastrar Freelancer",
                                        color=ft.Colors.GREY,
                                        col=12,
                                        padding=5,)    
    btn_new_sub_proj = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_new_delivery(page)),
                                         text= "Cadastrar Entrega",
                                        color=ft.Colors.GREY,
                                        col=12,
                                        padding=5,)
    btn_new_delivery = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_payment(page, month="Fevereiro")),
                                         text= "Relatório Financeiro",
                                        color=ft.Colors.GREY,
                                        col=12,
                                        padding=5,)
    btn_new_pro = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_new_project(page)),
                                            text= "Cadastrar Projeto",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    btn_see_file = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_files(page)),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_deliverys(page)),
                                            text= "Ver Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    drawer = ft.NavigationDrawer(


        controls=[
            ft.Divider(thickness=1),
            btn_see_file,

            ft.Divider(thickness=1),
            btn_see_deliverys,
            
            ft.Divider(thickness=1),
            btn_new_pro,

            ft.Divider(thickness=1),
            btn_new_sub_proj,

            ft.Divider(thickness=1),
            btn_new_free,

            ft.Divider(thickness=1),
            btn_new_delivery,

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


    request_all_subprojects = sp.get_all_subprojects()
    request_all_subprojects_json = request_all_subprojects.json()
    dicio_all_subprojects = {}

    for row in request_all_subprojects_json:

        name_subproject = row["name_subproject"]
        predicted_lots = row["predicted_lots"]
        lots_done = row["lots_done"]
        deliverys = row["deliverys"]
        recommended_medium = row["recommended_medium"]  
        percent = row["percent"]
        ortofoto = row["ortofoto"]
        project = row["project"]
        final_delivery = row["final_delivery"]
        current_average = row["current_average"]

        dicio_all_subprojects[name_subproject] = {
                                                "name_subproject": name_subproject,
                                                "predicted_lots": predicted_lots,
                                                "lots_done": lots_done,
                                                "deliverys": deliverys,
                                                "recommended_medium": recommended_medium,
                                                "percent": percent, "ortofoto": ortofoto,
                                                "project": project,
                                                "final_delivery": final_delivery,
                                                "current_average": current_average
                                                }


    request_all_deliverys = sp.get_all_deliverys()
    request_all_deliverys_json = request_all_deliverys.json()
    dicio_all_deliverys = {}

    for row in request_all_deliverys_json:
        
        id = row["id"]
        username = row["username"]
        date = row["date"]
        name_subproject = row["name_subproject"]
        project = row["project"]
        polygons = row["polygons"]
        photos = row["photos"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]
        warning = row["warning"]
        file = row["file"]

        dicio_all_deliverys[id] = {
                                    "id": id,
                                    "username": username,
                                    "date": date,
                                    "name_subproject": name_subproject,
                                    "project": project,
                                    "polygons": polygons,
                                    "photos": photos,
                                    "errors": errors,
                                    "discount": discount,
                                    "delay": delay,
                                    "warning": warning,
                                    "file": file
                                    }


    freelancer_data = []

    request_user = sp.get_all_user_data()
    data_users = request_user.json()


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
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),    
                    ])

            freelancer_data.append(linha)

            continue


        subproject = dicio_all_subprojects[current_subproject]
        
        total_deliverys_subproject = subproject["deliverys"]
        recommended_medium_subproject = subproject["recommended_medium"]

        polygons_made = 0
        delay_made  = 0
        current_deliverys_made = 0

        data_current_deliverys = []

        for item in dicio_all_deliverys.items():
            
            if item[1]["name_subproject"] == current_subproject:
                data_current_deliverys.append(item[1])

       

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
                        ft.DataCell(ft.Text(value=f"{int(polygons_made)} / {polygons_recommended} / {missing_lots}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, size=20)),
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

            data_current_deliverys2 = []

            for item2 in dicio_all_deliverys.items():
                
                if item2[1]["name_subproject"] == item:
                    data_current_deliverys2.append(item2[1])


            if len(data_current_deliverys2) == 0:
                polygons2 = 0
            else:
                for item3 in data_current_deliverys2:
                    polygons2 = item3["polygons"]
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
        bgcolor=ft.colors.WHITE,
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
# Página de Administrador


def verificar(username, password, page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

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
# Model de verificação de entrada - IF ADM DO/ IF USER DO;


def create_page_project(page):

    loading = LoadingPages(page=page)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    base = SupaBase(page=None)
    get_base = base.get_projects_data()
    get_json = get_base.json()

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))
    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))



    history_list = ft.Column(
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
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Visualizar", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Editar", text_align=ft.TextAlign.CENTER)),

                    ],
                    rows=[],  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,  
    )



    for city in get_json: 
        name_project = city["name_project"]

        def create_on_click(name):
            return lambda e: loading.new_loading_page(page=page,
                                                    call_layout= lambda:creat_page_subproject(page=page, project=name),
                                                    )
        
        def call_edit(name):
            return lambda e: loading.new_loading_page(page=page,
                                                    call_layout= lambda:create_page_project_token(page=page, project=name),
                                                    )


        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=f"{name_project}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.IconButton(icon=ft.Icons.SEARCH, on_click=create_on_click(name_project))),
                            ft.DataCell(ft.IconButton(icon=ft.Icons.EDIT, on_click=call_edit(name_project))),
                        ]
                )
        )
        
        


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
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,  # Removendo espaçamento entre os elementos da coluna
        ),
        bgcolor=ft.colors.WHITE,
        padding=10,  # Padding mínimo para o container
        border_radius=10,
        expand=True,
        alignment=ft.alignment.center,
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
# Pagina Lateral de Projetos


def create_page_project_token(page, project):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    loading = LoadingPages(page=page)
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )
    base = SupaBase(page=page)
    print (project)
    get_base_Project = base.get_one_project_data(project)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    print(get_info2)
    

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: creat_page_subproject(page=page, project=project))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))
    
    def editar_dados(data_list):
        

        supa_list = [
        data_list[0].value, data_list[1].value, data_list[2].value, data_list[3].value, data_list[4].value, data_list[5].value
        ]


        if any(field == "" or field is None for field in supa_list):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.edit_projects_data(supa_list)
            snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()), ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back())],
    )

    data_list =[
    ft.TextField(label="Nome do projeto", value=get_info2["name_project"], width=300),
    ft.TextField(label="Nome", value=get_info2["current_subprojects"], width=300),
    ft.TextField(label="Lotes Previstos", value=get_info2["final_delivery"], width=300),
    ft.TextField(label="Lotes Feitos", value=get_info2["predicted_lots"], width=300),
    ft.TextField(label="Entregas", value=get_info2["lots_done"], width=300),
    ft.TextField(label="Média Recomendada", value=get_info2["percent"], width=300),
    ]


   
    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(data_list))

    

    projects_token = ft.Container(
    content=ft.Column(
        controls=data_list,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza os itens na horizontal
        scroll=ft.ScrollMode.AUTO,  # Adiciona scroll se necessário
    ),
    padding=20,
    border=ft.border.all(2, ft.colors.BLUE),
    border_radius=10,
    bgcolor=ft.colors.WHITE,
    width=min(800, page.width * 0.9),  # Largura máxima de 800px ou 90% da tela
    height=min(900, page.height * 0.8),  # Altura máxima de 900px ou 80% da tela
    alignment=ft.alignment.center,  # Centraliza o conteúdo dentro do container
    margin=10,  # Margem externa
)

    

    # Layout responsivo com as duas fichas lado a lado
    layout = ft.ResponsiveRow(
    [
        ft.Column(
            [
                ft.Container(
                    projects_token,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    botao_edit,
                    alignment=ft.alignment.center
                )
            ],
            col={"sm": 12, "md": 6},
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=20,
    expand=True
)


    return layout
# Pagina de Ficha Editavel de Projetos


def creat_page_subproject(page, project):
    
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )
    
    loading = LoadingPages(page=page)
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
            return lambda e: loading.new_loading_page(
                page=page,
                call_layout=lambda: create_ficha_supro(page=page, subproject=subproject, project=project),
            )

        history_list.controls.append(
            ft.ListTile(title=ft.Text(f"{name_subproject}"), on_click=create_on_click(name_subproject))
        )

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),
            ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back()),
        ],
    )

   

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Subprojetos de Cidades", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o campo de pesquisa
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),  # Espaçamento
                history_list,
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
        ),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        col=6,
        alignment=ft.alignment.center,
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            main_container
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    return layout
# Pagina de Subprojetos - Continuação de Projetos


def create_ficha_supro(page, subproject, project):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    loading = LoadingPages(page=page)
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )
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




    
    def editar_dados(data_list):
        
        name = data_list[0].value
        username = data_list[1].value

        current_project = data_list[2].value
        total_deliverys = data_list[3].value

        weekly_deliveries = data_list[4].value
        polygons_made = data_list[5].value

        polygons_wrong = data_list[6].value
        warnings = data_list[7].value

        delays = data_list[8].value
        password = data_list[9].value

        permission = data_list[10].value
    
        supa_list = [
        name, username, current_project, total_deliverys, weekly_deliveries, polygons_made, polygons_wrong, warnings, delays, password, permission
        ]

        print(password)
        print(supa_list[9])

        if any(field == "" or field is None for field in supa_list):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.edit_user_data(supa_list)
            snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    
        
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

    
    data_list = [
        nome, usuario, projeto_atual, entrega_total, entrega_semanal, poligonos_feitos, poligonos_errados, advertencias, atrasos, senha, permissao
    ]

    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(data_list))

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
            botao_edit,
            
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


    return layout
# Pagina de Fichas Criacionais de Projetos


def create_page_new_freelancer(page):

    loading = LoadingPages(page=page)
    
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),],
    )

    # Campos do formulário
    campos = {
        "nome": ft.TextField(label="Nome", hint_text="Digite o nome", bgcolor=ft.Colors.WHITE),
        "Usuario": ft.TextField(label="Usuario", hint_text="Digite o Usuario",bgcolor=ft.Colors.WHITE),
        "pix": ft.TextField(label="PIX", hint_text="Digite o chave PIX",bgcolor=ft.Colors.WHITE),
        "email": ft.TextField(label="Email", hint_text="Digite o email",bgcolor=ft.Colors.WHITE),
    }



    # Função para enviar os dados (simulação)
    def enviar_dados(e):
        
        name_data = campos["nome"].value
        user_data = campos["Usuario"].value
        pix_data = campos["pix"].value
        email_data = campos["email"].value

        list_field = [name_data, user_data, pix_data, email_data]  

        if any(field == "" or field is None for field in list_field):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.create_user_data(name=name_data, username=user_data, pix=pix_data, email=email_data)
            snack_bar = ft.SnackBar(content=ft.Text("Dados enviados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()


    


    # Botão para enviar os dados
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_dados)
    
    
    # Layout do formulário de cadastro
    formulario_cadastro = ft.Column(
        [ft.Text("Cadastro de Dados", size=24, weight=ft.FontWeight.BOLD)] + list(campos.values()) + [botao_enviar],

        spacing=20,
        expand=True,

    )

    # Layout principal da página
    layout_principal = ft.ResponsiveRow(
        [
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},  # Define o tamanho do container em diferentes breakpoints
                controls=[
                    formulario_cadastro,
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
                spacing=20,
                scroll=ft.ScrollMode.AUTO,  # Habilita o scroll dentro da coluna
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o ResponsiveRow na página
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza verticalmente o ResponsiveRow
        
    )

    # Adiciona o layout principal à página
    return layout_principal
# Pagina de Fichas Criacionais de Freelancers


def create_page_new_delivery(page):

    base = SupaBase(page=page)
    sp = SupaBase(page)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    loading = LoadingPages(page=page)

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),],
    )

    # Definindo um tamanho fixo para todos os TextFields
    field_width = 300

    cadastrar = []
    users = (sp.get_all_user_data()).json()
    for item in users:
        cadastrar.append(ft.dropdown.Option(item["username"]))
    
    dropdown1 = ft.Dropdown(
        options=cadastrar,
        label="User",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        width=300,
        )
    
    current_project = []
    sub_project = (sp.get_all_subprojects()).json()
    for item in sub_project:
        current_project.append(ft.dropdown.Option(item["name_subproject"]))

    dropdown2 = ft.Dropdown(
        options=current_project,
        label="SubProjeto Atual",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        width=300,
        )
    
    project = []
    get_project = (sp.get_all_project_data()).json()
    for item in get_project:
        project.append(ft.dropdown.Option(item["name_project"]))
    
    dropdown3 = ft.Dropdown(
        options=project,
        label="Projeto",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        width=300,
        )

    content = {
                "id": ft.TextField(label="ID", hint_text="Digite o ID", bgcolor=ft.Colors.WHITE, width=field_width),
                "username": dropdown1,
                "date": ft.TextField(label="Data", hint_text="Digite a Data", bgcolor=ft.Colors.WHITE, width=field_width),
                "name_subproject": dropdown2,
                "project": dropdown3,
                "polygons": ft.TextField(label="Poligonos", hint_text="Digite o Poligonos", bgcolor=ft.Colors.WHITE, width=field_width),
                "errors": ft.TextField(label="Erros", hint_text="Digite o Erros", bgcolor=ft.Colors.WHITE, width=field_width),
                "discount": ft.TextField(label="Desconto", hint_text="Digite o Desconto", bgcolor=ft.Colors.WHITE, width=field_width),
                "warnings": ft.TextField(label="Advertencias", hint_text="Digite o Advertencias", bgcolor=ft.Colors.WHITE, width=field_width),
                "delay": ft.TextField(label="Atraso", hint_text="Digite o Atraso", bgcolor=ft.Colors.WHITE, width=field_width),
                "file": ft.TextField(label="Arquivos", hint_text="Digite o Arquivos", bgcolor=ft.Colors.WHITE, width=field_width),
                "photos": ft.TextField(label="Fotos", hint_text="Digite o Fotos", bgcolor=ft.Colors.WHITE, width=field_width),
    }

    

    list_content = [content["id"], content["username"], content["date"], content["name_subproject"], 
                    content["project"], content["polygons"], content["errors"], content["discount"], 
                    content["warnings"], content["delay"], content["file"], content["photos"]]

    def send_to_data(e):
        if any(field.value == "" or field.value is None for field in list_content):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.post_to_deliverys_data(content["id"].value, content["username"].value, content["date"].value, content["name_subproject"].value,
                                      content["project"].value, content["polygons"].value, content["errors"].value, content["discount"].value,
                                        content["warnings"].value, content["delay"].value, content["file"].value, content["photos"].value),
            snack_bar = ft.SnackBar(content=ft.Text("Dados enviados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    btn_send = ft.ElevatedButton("Enviar", on_click=send_to_data)        
    layout = ft.ResponsiveRow(
        [
            ft.Column(
                [*list_content, btn_send],
                col={"sm": 12, "md": 8, "lg": 6},
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        vertical_alignment=ft.CrossAxisAlignment.CENTER, 
    )

    return layout
# Pagina de Fichas Criacionais de Entregas


def create_page_payment(page, month):

    textthemes = TextTheme()
    buttons = Buttons(page)
    sp = SupaBase(page)
    texttheme1 = textthemes.create_text_theme1()
    loading = LoadingPages(page)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),],
    )

    request_all_deliverys = sp.get_all_deliverys()
    request_all_deliverys_json = request_all_deliverys.json()
    dicio_all_deliverys = {}

    for row in request_all_deliverys_json:
        
        id = row["id"]
        username = row["username"]
        date = row["date"]
        name_subproject = row["name_subproject"]
        project = row["project"]
        polygons = row["polygons"]
        photos = row["photos"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]
        warning = row["warning"]
        file = row["file"]

        dicio_all_deliverys[id] = {
                                    "id": id,
                                    "username": username,
                                    "date": date,
                                    "name_subproject": name_subproject,
                                    "project": project,
                                    "polygons": polygons,
                                    "photos": photos,
                                    "errors": errors,
                                    "discount": discount,
                                    "delay": delay,
                                    "warning": warning,
                                    "file": file
                                    }


    dropdown1 = ft.Dropdown(
        options=[
            ft.dropdown.Option("Janeiro"),
            ft.dropdown.Option("Fevereiro"),
            ft.dropdown.Option("Março"),
            ft.dropdown.Option("Abril"),
            ft.dropdown.Option("Maio"),
            ft.dropdown.Option("Junho"),
            ft.dropdown.Option("Julho"),
            ft.dropdown.Option("Agosto"),
            ft.dropdown.Option("Setembro"),
            ft.dropdown.Option("Outubro"),
            ft.dropdown.Option("Novembro"),
            ft.dropdown.Option("Dezembro"),
        ],
        value=month,
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        on_change= lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_payment(page, month=dropdown1.value)),
        col=6)

    dropdown2 = ft.Dropdown(options=[
        ft.dropdown.Option("2025"),
    ],
    value="2025",
    text_style=ft.TextStyle(color=ft.Colors.BLACK),
    bgcolor=ft.Colors.WHITE,
    col=6)

    meses_pt = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
    }

    mes = meses_pt[dropdown1.value]

    selected_data = datetime(int(dropdown2.value), mes, 1)

    data_list = []

    get_all_user_data = sp.get_all_user_data()
    data_all_users = get_all_user_data.json()

    for row1 in data_all_users:

        name = row1["name"]
        username = row1["username"]
        payment = row1["payment"]

        data_total_deliverys = []

        for item in dicio_all_deliverys.items():
            
            if item[1]["username"] == username:
                data_total_deliverys.append(item[1])

        total_polygons = 0
        total_errors = 0
        total_photos = 0
        number_total_deliverys = 0
        delivery_07 = [0, 0]
        delivery_14 = [0, 0]
        delivery_21 = [0, 0]
        delivery_28 = [0, 0]

        for row in data_total_deliverys:

            date = row["date"]
            polygons = row["polygons"]
            errors = row["errors"]
            discount = row["discount"]
            delay = row["delay"]
            photos = row["photos"]

            data_obj = datetime.strptime(date, "%d/%m/%Y")

            if data_obj.month == selected_data.month and data_obj.year == selected_data.year:

                total_polygons += int(polygons)
                total_errors += int(errors)
                total_photos += int(photos)
                number_total_deliverys += 1


                def add_polygons(delivery, polygons):
                    delivery[0] = polygons

                def add_photos(delivery, photos):
                    delivery[1] = photos

                dicio1 = {
                    7: lambda: add_polygons(delivery_07, int(polygons)),
                    14: lambda: add_polygons(delivery_14, int(polygons)),
                    21: lambda: add_polygons(delivery_21, int(polygons)),
                    28: lambda: add_polygons(delivery_28, int(polygons)),
                }
                dicio2 = {
                    7: lambda: add_photos(delivery_07, int(photos)),
                    14: lambda: add_photos(delivery_14, int(photos)),
                    21: lambda: add_photos(delivery_21, int(photos)),
                    28: lambda: add_photos(delivery_28, int(photos)),
                }

                call_function1 = dicio1.get(data_obj.day, lambda: None)()
                call_function2 = dicio2.get(data_obj.day, lambda: None)()

 
        total = float((delivery_07[0]+delivery_14[0]+delivery_21[0]+delivery_28[0]) * 0.50) + (float((delivery_07[1]+delivery_14[1]+delivery_21[1]+delivery_28[1]) * 0.20))
        total_format = format(total, ".2f")
        

        if number_total_deliverys > 0:

            linha = ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=name, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=payment, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{delivery_07[0]} / {delivery_07[1]}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{delivery_14[0]} / {delivery_14[1]}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{delivery_21[0]} / {delivery_21[1]}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{delivery_28[0]} / {delivery_28[1]}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"R$ {total_format}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                        ])        

            data_list.append(linha)

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
                        ft.DataColumn(ft.Text(value="Nome", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Pix", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 07", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 14", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 21", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 28", text_align=ft.TextAlign.CENTER)),  
                        ft.DataColumn(ft.Text(value="Total", text_align=ft.TextAlign.CENTER)),  
                    ],
                    rows=data_list,  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=300,  
        expand=True,  
    )


 
    container_form2 = ft.Container(content=ft.Column([dropdown1, dropdown2, form4]),
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=20,
                                    padding=10,
                                    height=((page.height) / 1.3),
                                    col={"xs" : 12, "lg" : 8},
                                    )
    

    container2 = ft.Container(content=ft.ResponsiveRow(controls=[container_form2],
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
        controls=[container2],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
# Pagina de Status Financeiros


def create_page_new_project(page):
    base = SupaBase(page=page)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    loading = LoadingPages(page=page)

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),],
    )

    
    content = {
                "Projeto": ft.TextField(label="Projeto", hint_text="Digite o Projeto", bgcolor=ft.Colors.WHITE, expand= False, width=300),
                "Projeto Atual": ft.TextField(label="Projeto Atual", hint_text="Digite o Nome", bgcolor=ft.Colors.WHITE, expand= False, width=300),
                "Entrega Final": ft.TextField(label="Entrega Final", hint_text="Digite a data", bgcolor=ft.Colors.WHITE, expand= False, width=300),
                "Lotes Previstos": ft.TextField(label="Lotes Previstos", hint_text="Digite a Quantidade", bgcolor=ft.Colors.WHITE, expand= False, width=300),
                "Lotes Feitos": ft.TextField(label="Lotes Feitos", hint_text="Digite a Quantidade", bgcolor=ft.Colors.WHITE, expand= False, width=300),
                "Porcentagem": ft.TextField(label="Porcentagem", hint_text="Digite a Porcentagem", bgcolor=ft.Colors.WHITE, expand= False, width=300),
    }




    list_content = [content["Projeto"], content["Projeto Atual"], content["Entrega Final"], content["Lotes Previstos"],
                    content["Lotes Feitos"], content["Porcentagem"]]


    def send_to_data(e):
        
      
    
        if any(field.value == "" or field.value is None for field in list_content):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.get_new_project_data(content["Projeto"].value, content["Projeto Atual"].value, content["Entrega Final"].value, content["Lotes Previstos"].value,
                                      content["Lotes Feitos"].value, content["Porcentagem"].value),
            snack_bar = ft.SnackBar(content=ft.Text("Dados enviados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

 
    btn_send = ft.ElevatedButton("Enviar", on_click=send_to_data)        
    layout = ft.ResponsiveRow(
        [
            ft.Column(
                [*list_content, btn_send],
                col={"sm": 12, "md": 8, "lg": 6},
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        vertical_alignment=ft.CrossAxisAlignment.CENTER, 
    )

    return layout
# Pagina de Fichas Criacionais de Projetos


def create_page_see_deliverys(page):
    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    get_base = base.get_all_deliverys()
    get_json = get_base.json()

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # Lista para exibir as entregas
    history_list = ft.ListView(
        controls=[],
        expand=True,
        spacing=0,  # Removendo espaçamento entre os itens da lista
    )

    # Preenche a lista com os dados das entregas
    for delev in get_json:
        delivery = {
            "id": delev["id"],
            "username": delev["username"],
            "date": delev["date"],
            "name_subproject": delev["name_subproject"],
            "project": delev["project"],
            "polygons": delev["polygons"],
            "errors": delev["errors"],
            "discount": delev["discount"],
            "warning": delev["warning"],
            "delay": delev["delay"],
            "file": delev["file"],
            "photos": delev["photos"],
        }

        # Adiciona um ListTile para cada entrega
        history_list.controls.append(
            ft.ListTile(
                subtitle=ft.Text(
                    f"{delivery['username']} | "
                    f"{delivery['date']} | "
                    f"{delivery['polygons']} | "
                    f"{delivery['photos']}",
                    color=ft.colors.BLACK,
                    size=16,
                ),
                on_click=lambda e, delivery=delivery: loading.new_loading_page(
                    page=page,
                    call_layout=lambda: create_page_delivery_details(page=page, delivery=delivery)
                ),
            )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),
            ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back()),
        ],
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Entregas", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                history_list,  # Adiciona a lista de entregas
            ],
            expand=True,
            spacing=0,
        ),
        bgcolor=ft.colors.WHITE,
        padding=10,
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
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return layout
# Pagina De Visualização de Entregas


def create_page_delivery_details(page, delivery):
    loading = LoadingPages(page=page)
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )
    # Definir o tema global para garantir que o texto seja preto por padrão
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_deliverys(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Detalhes da Entrega", color=ft.colors.BLACK),  # Texto preto
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),
            ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back()),
        ],
    )

    def editar_dados(data_list):
        
        
        username = data_list[0].value

        date = data_list[1].value
        name_subproject = data_list[2].value

        project = data_list[3].value
        polygons = data_list[4].value

        errors = data_list[5].value
        warnings = data_list[6].value
        
        discount = data_list[7].value
        delays = data_list[8].value
        file = data_list[9].value

        photo = data_list[10].value
    
        supa_list = [
        username, date, name_subproject, project, polygons, errors, discount,
          warnings, delays, file, photo
        ]

        if any(field == "" or field is None for field in supa_list):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.edit_delivery_data(supa_list)
            snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()


    # Campos para exibir os detalhes da entrega
    details_layout = ft.Column(
    controls=[
        ft.Text("Detalhes da Entrega", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),  # Título        
        ft.TextField(label="Usuário", value=f"{delivery['username']}", width=300, color=ft.colors.BLACK),  # usuario_field
        ft.TextField(label="Data", value=f"{delivery['date']}", width=300, color=ft.colors.BLACK),  # data_field
        ft.TextField(label="Subprojeto", value=f"{delivery['name_subproject']}", width=300, color=ft.colors.BLACK),  # subprojeto_field
        ft.TextField(label="Projeto", value=f"{delivery['project']}", width=300, color=ft.colors.BLACK),  # projeto_field
        ft.TextField(label="Polígonos", value=f"{delivery['polygons']}", width=300, color=ft.colors.BLACK),  # poligonos_field
        ft.TextField(label="Erros", value=f"{delivery['errors']}", width=300, color=ft.colors.BLACK),  # erros_field
        ft.TextField(label="Desconto", value=f"{delivery['discount']}", width=300, color=ft.colors.BLACK),  # desconto_field
        ft.TextField(label="Advertências", value=f"{delivery['warning']}", width=300, color=ft.colors.BLACK),  # advertencias_field
        ft.TextField(label="Atrasos", value=f"{delivery['delay']}", width=300, color=ft.colors.BLACK),  # atrasos_field
        ft.TextField(label="Arquivo", value=f"{delivery['file']}", width=300, color=ft.colors.BLACK),  # arquivo_field
        ft.TextField(label="Fotos", value=f"{delivery['photos']}", width=300, color=ft.colors.BLACK),  # fotos_field
    ],
    spacing=10,
    scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
)

# Lista com os TextFields
    data_list = [   
    ft.TextField(label="Usuário", value=f"{delivery['username']}", width=300, color=ft.colors.BLACK),  # usuario_field
    ft.TextField(label="Data", value=f"{delivery['date']}", width=300, color=ft.colors.BLACK),  # data_field
    ft.TextField(label="Subprojeto", value=f"{delivery['name_subproject']}", width=300, color=ft.colors.BLACK),  # subprojeto_field
    ft.TextField(label="Projeto", value=f"{delivery['project']}", width=300, color=ft.colors.BLACK),  # projeto_field
    ft.TextField(label="Polígonos", value=f"{delivery['polygons']}", width=300, color=ft.colors.BLACK),  # poligonos_field
    ft.TextField(label="Erros", value=f"{delivery['errors']}", width=300, color=ft.colors.BLACK),  # erros_field
    ft.TextField(label="Desconto", value=f"{delivery['discount']}", width=300, color=ft.colors.BLACK),  # desconto_field
    ft.TextField(label="Advertências", value=f"{delivery['warning']}", width=300, color=ft.colors.BLACK),  # advertencias_field
    ft.TextField(label="Atrasos", value=f"{delivery['delay']}", width=300, color=ft.colors.BLACK),  # atrasos_field
    ft.TextField(label="Arquivo", value=f"{delivery['file']}", width=300, color=ft.colors.BLACK),  # arquivo_field
    ft.TextField(label="Fotos", value=f"{delivery['photos']}", width=300, color=ft.colors.BLACK),  # fotos_field
]
    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(data_list))
    # Container principal
    main_container = ft.Container(
        content=details_layout,
        padding=20,
        border=ft.border.all(2, ft.colors.BLUE),
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        width=800 if page.width > 800 else page.width * 0.9,  # Largura responsiva
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},
                controls=[main_container, botao_edit],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return layout
# Pagina De Visualização de Todas as Informações de Entregas


def create_page_files(page):
    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    get_base = base.get_all_files()
    get_json = get_base.json()

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # Lista para exibir as entregas
    history_list = ft.ListView(
        controls=[],
        expand=True,
        spacing=0,  # Removendo espaçamento entre os itens da lista
    )

    # Preenche a lista com os dados das entregas
    for delev in get_json:
        files = {
            "id": delev["id"],
            "date": delev["date"],
            "username": delev["username"],
            "subproject": delev["subproject"],
            "type": delev["type"],
            "amount": delev["amount"],
            "url": delev["url"],
        }

        # Adiciona um ListTile para cada entrega
        history_list.controls.append(
            ft.ListTile(
                subtitle=ft.Text(
                    f"{files['username']} | "
                    f"{files['date']} | "
                    f"{files['subproject']} | "
                    f"{files['amount']}",
                    color=ft.colors.BLACK,
                    size=16,
                ),
                on_click=lambda e, files=files: loading.new_loading_page(
                    page=page,
                    call_layout=lambda: create_page_files_details(page=page, files=files)
                ),
            )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Soluções e Engenharia"),
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),
            ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back()),
        ],
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Arquivos", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                history_list,  # Adiciona a lista de entregas
            ],
            expand=True,
            spacing=0,
        ),
        bgcolor=ft.colors.WHITE,
        padding=10,
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
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return layout
# Pagina de Visualização de Arquivos


def create_page_files_details(page, files):
    loading = LoadingPages(page=page)
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )
    # Definir o tema global para garantir que o texto seja preto por padrão
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=ft.colors.BLACK,  # Define a cor do texto como preto
        ),
    )

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_files(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Detalhes da Entrega", color=ft.colors.BLACK),  # Texto preto
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: go_home()),
            ft.IconButton(ft.icons.KEYBOARD_RETURN, on_click=lambda e: go_back()),
        ],
    )

  


    # Campos para exibir os detalhes da entrega
    details_layout = ft.Column(
    controls=[
        ft.Text("Detalhes da Entrega", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),  # Título        
        ft.TextField(label="Usuário", value=f"{files['username']}", width=300, color=ft.colors.BLACK),  # usuario_field
        ft.TextField(label="Data", value=f"{files['date']}", width=300, color=ft.colors.BLACK),  # data_field
        ft.TextField(label="Subprojeto", value=f"{files['subproject']}", width=300, color=ft.colors.BLACK),  # subprojeto_field
        ft.TextField(label="type", value=f"{files['type']}", width=300, color=ft.colors.BLACK),  # erros_field
        ft.TextField(label="amount", value=f"{files['amount']}", width=300, color=ft.colors.BLACK),  # desconto_field
        ft.TextField(label="url", value=f"{files['url']}", width=300, color=ft.colors.BLACK),  # advertencias_field
    ],
    spacing=10,
    scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
)

# Lista com os TextFields
    data_list = [   
    ft.TextField(label="Usuário", value=f"{files['username']}", width=300, color=ft.colors.BLACK),  # usuario_field
    ft.TextField(label="Data", value=f"{files['date']}", width=300, color=ft.colors.BLACK),  # data_field
    ft.TextField(label="Subprojeto", value=f"{files['subproject']}", width=300, color=ft.colors.BLACK),  # subprojeto_field
    ft.TextField(label="type", value=f"{files['type']}", width=300, color=ft.colors.BLACK),
    ft.TextField(label="amount", value=f"{files['amount']}", width=300, color=ft.colors.BLACK),
    ft.TextField(label="url", value=f"{files['url']}", width=300, color=ft.colors.BLACK),  # advertencias_field
]
    
    # Container principal
    main_container = ft.Container(
        content=details_layout,
        padding=20,
        border=ft.border.all(2, ft.colors.BLUE),
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        width=800 if page.width > 800 else page.width * 0.9,  # Largura responsiva
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},
                controls=[main_container],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return layout
# Pagina De Visualização de Todas as Informações de Arquivos




























































































































