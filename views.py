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
        bgcolor= ft.Colors.WHITE,
        text_style= ft.TextStyle(color=ft.Colors.BLACK),
        border_radius= 0,
        
    )    
         #Login//Password
    password = ft.TextField(
        label= "Code",
        bgcolor= ft.Colors.WHITE,
        text_style= ft.TextStyle(color=ft.Colors.BLACK),
        border_radius= 0,
        password= True, 
        can_reveal_password= True,
    )
         #Login//Enter
    Send = ft.ElevatedButton(text="Enter",
        bgcolor= ft.Colors.GREEN_100,
        color= ft.Colors.GREEN,
        on_click=lambda e: verificar(login.value, password.value, page)
    )
    logo = ft.Image(
        src="https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/images//acess.jpg",
        repeat=ft.ImageRepeat.NO_REPEAT,
        data=0,
        height=200,
    )
    area = ft.Container(
        bgcolor= ft.Colors.WHITE,
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
            dwg = row["dwg"]

            date_delivery_dt = datetime.strptime(date, "%d/%m/%Y")


            def create_on_click(dwg):
                return lambda e: page.launch_url(dwg)

            btn_dwg = buttons.create_button(on_click=create_on_click(dwg),
                                      text="Baixar",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,)

            linha = ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=date, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=name_subproject, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=polygons, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=photos, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=errors, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=discount, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=delay, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(btn_dwg),
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
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    cash_month = (datetime.now().month) - 1
    cash_year = datetime.now().year
    if current_day > 7:
        current_month += 1
        cash_month = (datetime.now().month)
        if current_month == 12:
            current_year += 1
            current_month = 1
        if cash_month == 0:
            cash_month == 12
            cash_year -= 1
   
    date_cash = f"07/{current_month:02d}/{current_year}"


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

                if data_obj.month == cash_month and data_obj.year == cash_year:

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
    test = ft.Text(value="", size=20)
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

        month = datetime.now().month
        year = datetime.now().year
        if date_file > 28:
            month += 1
            if month == 13:
                month = 1
                year += 1

        day_date_file = f"{dias[date_file]}/{month:02d}/{year:02d}"

        request_date_file = sp.check_file(date=day_date_file, username=dict_profile["username"])

        if len(request_date_file.json()) > 0:
            text_date_file[0].value = f"Entrega de {day_date_file} realizada"
            text_date_file[0].color = ft.Colors.GREEN
        else:
            text_date_file[0].value = f"Entrega de {day_date_file} não realizada"
            text_date_file[0].color = ft.Colors.RED
            
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
                        ft.DataColumn(ft.Text(value="Data", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Poligonos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Fotos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Erros", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Desconto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Atraso", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="DWG", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
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
    container_ortofoto = ft.Container(content=(ortofoto), border_radius=20, height=((page.height) / 2),)

    # Criação de tabelas
    #....................................................................

    #....................................................................
    # Inserção de arquivo

    def send_file(file_path, name_file):

        container = None
        overlay_copy = list(page.overlay)
        for item in overlay_copy:
                if item.data == "fp" or item.data == "bar":
                    pass
                else:
                    container = item

        field_container = [
            container.controls[0].content.controls[3].value,
            container.controls[0].content.controls[5].value,
            container.controls[0].content.controls[7].value,
        ]
        if any(field == "" or field is None for field in field_container):
            snack_bar = ft.SnackBar(
                content=ft.Text("Preencha todos os campos!"),
                bgcolor=ft.Colors.RED,
                duration=2000,
                data="bar",
                )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:

            snack_bar = ft.SnackBar(
                    content=ft.Text(
                        value=f"Enviando arquivo", color=ft.Colors.BLACK
                        ),
                    duration=10000,
                    bgcolor=ft.Colors.AMBER,
                    data="bar",
                )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            date = container.controls[0].content.controls[3].value

            check = (sp.check_file(
                date=date,
                username=dict_profile["username"]
            )).json()

            if len(check) > 0:
                for item in overlay_copy:
                    if item.data != "bar":
                        pass
                    else:
                        page.overlay.remove(item)
                snack_bar = ft.SnackBar(
                    content=ft.Text(
                        value=f"Entrega de {date} já realizada, arquivo não enviado", color=ft.Colors.BLACK
                        ),
                    duration=4000,
                    bgcolor=ft.Colors.AMBER,
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
                return
            
            response = sp.add_file_storage(file_path, name_file, row3["type"])

            if response.status_code == 200 or response.status_code == 201:

                id = str(sp.get_file_id())

                response2 = sp.post_to_files(
                                            id=id,   
                                            date=container.controls[0].content.controls[3].value,
                                            username=dict_profile["username"],
                                            subproject=dict_profile["current_project"],
                                            type=row3["type"],
                                            amount=container.controls[0].content.controls[7].value,
                                            url=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/files//{name_file}"
                                            )

                if response2.status_code == 200 or response2.status_code == 201:

                    for item in overlay_copy:
                        if item.data != "bar":
                            pass
                        else:
                            page.overlay.remove(item)

                    snack_bar = ft.SnackBar(
                    content=ft.Text(value="Arquivo enviado", color=ft.Colors.BLACK),
                    duration=4000,
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

                    for item in overlay_copy:
                        if item.data != "bar":
                            pass
                        else:
                            page.overlay.remove(item)

                    print(f" \n Erro ao enviar arquivo: {response2.status_code} - {response2.text} \n")
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

    file_selected = []
    file_name = []

    def on_file_selected():

        data = (datetime.now().strftime("%d/%m/%Y")).replace("/", "")
        extension = "dwg"
        if row3["type"] == "fotos":
            extension = "xlsx"
        name_file = f'{dict_profile["username"]}_{data}.{extension}'
        
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
        
        next_month = datetime.now().month + 1
        year = datetime.now().year
        if next_month == 13:
            next_month = 1
            year += 1


        container = ft.Row(
            controls=[ ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(value=f"{file_name[0]}", color=ft.Colors.BLACK),
                                    ft.Text(value="", color=ft.Colors.BLACK),
                                    ft.Text(value="Data da entrega:", color=ft.Colors.BLACK),
                                    ft.Dropdown(
                                        options=[
                                            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}"),
                                            ft.dropdown.Option(f"07/{next_month:02d}/{year:02d}"),
                                        ],
                                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                        bgcolor=ft.Colors.WHITE,
                                    ),
                                    ft.Text(value="Tipo de entrega:", color=ft.Colors.BLACK),
                                    ft.Dropdown(
                                        value=row3["type"],
                                        label=row3["type"],
                                        label_style=ft.TextStyle(color=ft.Colors.BLACK),
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

    def get_uploaded_file_bytes(e: ft.FilePickerUploadEvent):

        file_path = f"uploads/{file_name[0]}"    

        with open(file_path, "rb") as file:
            file_content = file.read()

        file_selected.clear()
        file_selected.append(file_content)

        on_file_selected()
 
    def on_image_selected(e: ft.FilePickerResultEvent):

            if not e.files or len(e.files) == 0:
                return
            
            file_selected.clear()
            file_selected.append(e.files[0])
            file_name.clear()
            file_name.append(e.files[0].name)


            if e.page.web:
                #  Gerar a URL temporária
                temp_url = e.page.get_upload_url(file_selected[0].name, 3600)

                #  Criar objeto para upload
                file_upload = ft.FilePickerUploadFile(file_selected[0].name, temp_url)

                #  Realiza o upload
                fp.upload([file_upload])

            else:
                on_file_selected()
 
    fp = ft.FilePicker(on_result=on_image_selected, on_upload=get_uploaded_file_bytes, data="fp")
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
    
    btn_dwg = buttons.create_button(on_click=lambda e: page.launch_url(row3["dwg"]),
                                      text="Baixar DWG",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )
    
    btn_ecw = buttons.create_button(on_click=lambda e: page.launch_url(row3["ecw"]),
                                      text="Baixar Ortofoto",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )
    
    btn_planner1= buttons.create_button(on_click=lambda e: page.launch_url(row3["planner1"]),
                                      text="Baixar Planilha 1",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )
    
    btn_planner2= buttons.create_button(on_click=lambda e: page.launch_url(row3["planner2"]),
                                      text="Baixar Planilha 2",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )

    if dict_profile["current_project"] != ".":
        if row3["type"] == "poligonos":
            btn_planner1.visible = False
            btn_planner2.visible = False
        else:
            btn_dwg.visible = False
            btn_ecw.visible = False
    else:
        btn_planner1.visible = False
        btn_planner2.visible = False
        btn_dwg.visible = False
        btn_ecw.visible = False


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
                                    padding=30,
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
    

    container_ortofoto2 = ft.Container(
                                    content=ft.Column(
                                        controls=[container_ortofoto, btn_dwg, btn_ecw, btn_planner1, btn_planner2],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=15,
                                        scroll=ft.ScrollMode.AUTO,
                                        ),
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
    btn_see_file = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_files(page)),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_deliverys(page)),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    btn_see_subprojects = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_list_subproject(page)),
                                            text= "Subprojetos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_freelancers(page)),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=5,)
    
    drawer = ft.NavigationDrawer(


        controls=[
            
            ft.Divider(thickness=1),
            btn_projeto,

            ft.Divider(thickness=1),
            btn_see_subprojects,

            ft.Divider(thickness=1),
            btn_see_freelancers,

            ft.Divider(thickness=1),
            btn_see_file,

            ft.Divider(thickness=1),
            btn_see_deliverys,
            
            ft.Divider(thickness=1),
            btn_exit,
            ]
            )
        
    
    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda:create_page_initial_adm(page=page))

    page.drawer = drawer

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(drawer), icon_color=ft.Colors.BLACK)],
        
        
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
                        ft.DataCell(ft.Text(value=first_name, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=".", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),    
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
                        ft.DataCell(ft.Text(value=first_name, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=current_subproject, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{int(polygons_made)} / {polygons_recommended} / {missing_lots}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{current_deliverys_made} / {total_deliverys_subproject} / {recommended_medium_subproject}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),    
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
                        ft.DataColumn(ft.Text(value="Nome", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
                        #ft.DataColumn(ft.Text(value="Média", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=10)),  
                        ft.DataColumn(ft.Text(value="Poligonos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
                        #ft.DataColumn(ft.Text(value="Faltantes", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=10)),  
                        ft.DataColumn(ft.Text(value="Entregas", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
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
                        ft.DataCell(ft.Text(value=name_project, theme_style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{project_polygons} / {predicted_lots} ... {int(percent_project)}%", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{len(list_current_subprojects)}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),
                        ft.DataCell(ft.Text(value=f"{final_delivery}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),    
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
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
                        ft.DataColumn(ft.Text(value="Lotes", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),   
                        ft.DataColumn(ft.Text(value="N°", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),   
                        ft.DataColumn(ft.Text(value="Entrega", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, size=20)),  
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
        bgcolor=ft.Colors.WHITE,
        padding=30,
        alignment=ft.alignment.top_center,
        expand=True,
        height=container_height,
        border_radius=20,
        col={"xs" : 12, "lg" : 6},
    )

    container2 = ft.Container(
        content=form5,
        bgcolor=ft.Colors.WHITE,
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
                        ft.DataColumn(ft.Text(value="Projeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Visualizar", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Editar", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),

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
                                                    call_layout= lambda:create_page_subproject(page=page, project=name),
                                                    )
        
        def call_edit(name):
            return lambda e: loading.new_loading_page(page=page,
                                                    call_layout= lambda:create_page_project_token(page=page, project=name),
                                                    )


        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=f"{name_project}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                on_click=create_on_click(name_project),
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.EDIT,
                                on_click=call_edit(name_project),
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                )),
                        ]
                )
        )
        
        


        # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
        
        
    )

    def filtrar_usuarios(e):
        texto = e.control.value.lower().strip()
        
        for item in history_list.controls[0].content.rows:
            item.visible = texto in item.cells[0].content.value.lower() if texto else True

        history_list.update()

    # Campo de pesquisa
    search_field = ft.TextField(
        label="Pesquisar",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        hint_text="Digite para pesquisar...",
        border_color=ft.Colors.BLUE_800,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        width=350,
        on_change=filtrar_usuarios,
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column( 
            [
                ft.Row(
                controls=[
                    ft.Text("Projetos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: loading.new_loading_page(
                            page=page,
                            call_layout=lambda: create_page_new_project(page=page),
                            ),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                search_field,
                history_list,
                # Lista colada ao campo de pesquisa
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,  # Removendo espaçamento entre os elementos da coluna
        ),
        bgcolor=ft.Colors.WHITE,
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

    loading = LoadingPages(page=page)
    base = SupaBase(page=page)
    get_base_Project = base.get_one_project_data(project)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))
    
    def editar_dados(view_project):
        
        data_project = view_project

        data_project["name_project"] = view_project["name_project"].value
        data_project["current_subprojects"] = view_project["current_subprojects"].value
        data_project["final_delivery"] = view_project["final_delivery"].value
        data_project["predicted_lots"] = view_project["predicted_lots"].value

        
        if any(field == "" or field is None for field in data_project.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            sp.edit_projects_data(data_project)
            snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )

    view_project ={
        "name_project": ft.TextField(label="Nome do projeto", value=get_info2["name_project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "current_subprojects": ft.TextField(label="Nome", value=get_info2["current_subprojects"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "final_delivery": ft.TextField(label="Lotes Previstos", value=get_info2["final_delivery"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "predicted_lots": ft.TextField(label="Lotes Feitos", value=get_info2["predicted_lots"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
    }


   
    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(view_project))

    

    projects_token = ft.Container(
    content=ft.Column(
        controls=view_project.values(),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza os itens na horizontal
        scroll=ft.ScrollMode.AUTO,  # Adiciona scroll se necessário
    ),
    padding=20,
    border=ft.border.all(2, ft.Colors.BLUE),
    border_radius=10,
    bgcolor=ft.Colors.WHITE,
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
def create_page_new_project(page):

    loading = LoadingPages(page=page)
    sp = SupaBase(page)

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    containers_list = []

    def create_container():
        
        return ft.Container(
                    content=ft.Column(
                        controls=[],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                    bgcolor=ft.Colors.WHITE,
                    padding=10,
                    border_radius=10,
                    expand=True,
                    alignment=ft.alignment.center,
                )
    
    def remove_container(container, parent_container):
        if container in containers_list:
            containers_list.remove(container)  
            parent_container.content.controls.remove(container)  
            parent_container.update()  

    def add_container(parent_container):

        
        new_container = ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        on_click=lambda e: remove_container(new_container, parent_container),
                                        bgcolor=ft.Colors.RED,
                                        icon_color=ft.Colors.WHITE,
                                    ),
                                    ft.TextField(label="Subprojeto", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="name_subproject"),
                                    ft.Dropdown(
                                        options=[
                                            ft.dropdown.Option("poligonos"),
                                            ft.dropdown.Option("fotos"),
                                        ],
                                        label="Tipo",
                                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                        bgcolor=ft.Colors.WHITE,
                                        width=300,
                                        data="type",
                                    ),
                                    ft.TextField(label="Lotes Previstos", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="predicted_lots"),
                                    ft.TextField(label="Média", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="recommended_medium"),
                                    ft.TextField(label="Entrega", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="final_delivery"),
                                ],
                                spacing=20,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=ft.Colors.GREY_400,
                            padding=10,
                            border_radius=10,
                            alignment=ft.alignment.center,
                        )
        
        # Adiciona o novo container à lista e à interface
        containers_list.append(new_container)
        parent_container.content.controls.append(new_container)
        parent_container.update()


    content = {
                "Projeto": ft.TextField(label="Projeto", hint_text="Digite o Projeto", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),

                "Subprojetos": ft.Row(
                                controls=[
                                    ft.Text("Adicionar Subprojetos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                                    ft.IconButton(
                                        icon=ft.Icons.ADD,
                                        on_click=lambda e: add_container(content["Container_Subprojetos"]),
                                        bgcolor=ft.Colors.GREEN,
                                        icon_color=ft.Colors.WHITE,
                                    )
                                ],  
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20,
                                ),

                "Container_Subprojetos": create_container(),

                "Entrega_Final": ft.TextField(label="Entrega Final", hint_text="Digite a data", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),

                "Lotes_Previstos": ft.TextField(label="Lotes Previstos", hint_text="Digite a Quantidade", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
    }


    def send_data():

        string_name = f""
        dicio_data_subprojects = {}
        for subproject in content["Container_Subprojetos"].content.controls:
            
            def create_dicio(name_subproject, type, predicted_lots, recommended_medium, final_delivery):
                new_dicio = {}
                new_dicio["name_subproject"] = name_subproject
                new_dicio["type"] = type
                new_dicio["predicted_lots"] = predicted_lots
                new_dicio["recommended_medium"] = recommended_medium
                new_dicio["final_delivery"] = final_delivery
                new_dicio["lots_done"] = "0"
                new_dicio["ortofoto"] = "."
                new_dicio["deliverys"] = "1"
                new_dicio["percent"] = "0"
                new_dicio["project"] = content["Projeto"].value
                new_dicio["current_average"] = "0"
                new_dicio["dwg"] = "."
                new_dicio["planner1"] = "."
                new_dicio["planner2"] = "."

                return new_dicio

            string_name += f"{subproject.content.controls[1].value},"

            dicio_data_subprojects[subproject.content.controls[1].value] = create_dicio(
                                                            subproject.content.controls[1].value,
                                                            subproject.content.controls[2].value,
                                                            subproject.content.controls[3].value,
                                                            subproject.content.controls[4].value,
                                                            subproject.content.controls[5].value,
                                                            )
        
        string_sbprojects = string_name[:-1]

        response = sp.post_project_data(
            content["Projeto"].value,
            string_sbprojects,
            content["Entrega_Final"].value,
            content["Lotes_Previstos"].value,
            )
        
        if response.status_code == 201:

            list_codes = []
            for item in dicio_data_subprojects.items():
                response2 = sp.post_subproject_data(item[1])
                list_codes.append(response2.status_code)

            check = all(item == 201 for item in list_codes)

            if check:
                loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))
                snack_bar = ft.SnackBar(content=ft.Text("Projeto criado com sucesso"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text("Erro ao criar subprojetos"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

        else:
            snack_bar = ft.SnackBar(content=ft.Text("Erro ao criar projeto"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    def check_field(e):
        
        def show_snackbar(page, message):
            """Exibe uma mensagem de erro usando SnackBar."""
            snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor=ft.colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

        fields_projects = [content["Projeto"], content["Entrega_Final"], content["Lotes_Previstos"]]


        if any(not field.value for field in fields_projects):
            show_snackbar(page, "Preencha todos os campos!")
            return


        for subproject in content["Container_Subprojetos"].content.controls:
            empty_fields = [
                field for field in subproject.content.controls
                if getattr(field, "data", None) != None and not field.value
            ]

            if empty_fields:
                show_snackbar(page, "Preencha todos os campos dos subprojetos!")
                return
            
        send_data()

 
    btn_send = ft.ElevatedButton("Enviar", on_click=check_field) 

    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Adicionar Projeto", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                *[item for item in content.values()],
                btn_send
            ],
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.WHITE,
        padding=10,
        border_radius=10,
        expand=True,
        alignment=ft.alignment.center,
    )


    layout = ft.ResponsiveRow(
        [
            ft.Column(
                [main_container],
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




def create_page_subproject(page, project):
    
    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    get_base = base.get_all_subproject_data(project)
    get_json = get_base.json()

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
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Editar", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Excluir", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
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
        name_subproject = city["name_subproject"]
        data = city
        
        def delete_subproject(name_subproject):

            base = SupaBase(page=None)
            data = ((base.get_one_project_data(project)).json())[0]
            string_subprojects = (data["current_subprojects"]).split(",")
            for item in string_subprojects:
                if item == name_subproject:
                    string_subprojects.remove(item)

            response1 = base.delete_storage(local="dwg", object=f"{name_subproject}.dwg", type="image/vnd.dwg")
            response2 = base.delete_storage(local="planner1", object=f"{name_subproject}.xlsx", type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response3 = base.delete_storage(local="planner2", object=f"{name_subproject}.xlsx", type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response4 = base.delete_subproject(subproject=name_subproject)
            if response4.status_code in [200, 204]:
                response5 = base.edit_projects_data(
                    data_project={
                        "name_project": project,
                        "current_subprojects": ",".join(string_subprojects)
                            }
                        )
                if response5.status_code in [200, 204]:
                    if len(string_subprojects) == 0:
                        response6 = base.delete_project(project)
                        if response6.status_code in [200, 204]:
                            loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))
                            snack_bar = ft.SnackBar(content=ft.Text("Subprojeto e Projeto Excluidos"), bgcolor=ft.Colors.GREEN)
                            page.overlay.append(snack_bar)
                            snack_bar.open = True
                            page.update()
                        else:
                            loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))
                            snack_bar = ft.SnackBar(content=ft.Text("Falha ao excluir projeto"), bgcolor=ft.Colors.RED)
                            page.overlay.append(snack_bar)
                            snack_bar.open = True
                            page.update()
                    else:
                        loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page, project=project))
                        snack_bar = ft.SnackBar(content=ft.Text("Subprojeto Excluido"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text("Falha ao excluir Subprojeto"), bgcolor=ft.Colors.AMBER)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
           

        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{name_subproject}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.EDIT,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, subproject_data=data: loading.new_loading_page(
                                        page=page,
                                        call_layout=lambda: create_page_subproject_token(page=page, subproject=subproject_data, back_project=project)
                                    ),
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.DELETE,
                                bgcolor=ft.Colors.RED,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, name_subproject=name_subproject: delete_subproject(name_subproject=name_subproject),
                                )),
            ])
        )


    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

   

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                controls=[
                     ft.Text("Subprojetos de Cidades", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: loading.new_loading_page(
                            page=page,
                            call_layout=lambda: create_page_new_subproject(page=page, project=project),
                            ),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o campo de pesquisa
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),  # Espaçamento
                history_list,
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
        ),
        bgcolor=ft.Colors.WHITE,
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

def create_page_list_subproject(page):#ESTOU MEXENDO NESSE AQUI

    loading = LoadingPages(page=page)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    base = SupaBase(page=None)
    get_base = base.get_all_subprojects()
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
                        ft.DataColumn(ft.Text(value="Subprojetos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Lotes_Previstos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)), 
                        ft.DataColumn(ft.Text(value="Entregas", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Media_Recomendada", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Porcentagem", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Entrega_Final", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Editar", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),

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
        name_subproject = city["name_subproject"] 
        predicted_lots = city["predicted_lots"] 
        deliverys = city["deliverys"] 
        recommended_medium = city["recommended_medium"] 
        project = city["project"]  
        final_delivery = city["final_delivery"] 

        
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=f"{name_subproject}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{predicted_lots}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{deliverys}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{recommended_medium}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{project}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(value=f"{final_delivery}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.EDIT,
                                on_click=lambda e, subproject=city: loading.new_loading_page(
                                    page=page,
                                    call_layout=lambda: create_page_subproject_token(page=page, subproject=subproject
                                        
                                    )
                                    ),
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                ))
                                        
                           
                        ]
                )
        )
        
        
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
            
    )

    def filtrar_usuarios(e):
        texto = e.control.value.lower().strip()
        
        for item in history_list.controls[0].content.rows:
            item.visible = texto in item.cells[0].content.value.lower() if texto else True

        history_list.update()

    # Campo de pesquisa
    search_field = ft.TextField(
        label="Pesquisar",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        hint_text="Digite para pesquisar...",
        border_color=ft.Colors.BLUE_800,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        width=350,
        on_change=filtrar_usuarios,
    )


    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Subprojetos", size=35, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                search_field,
                ft.Container(
                    content=history_list,
                    expand=True,
                    padding=ft.padding.only(bottom=20)
                )
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        bgcolor=ft.Colors.WHITE,
        padding=20,
        margin=0,
        border_radius=5,
        expand=True
    )

    # Layout da página
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout
# Pagina com conteudos de Subprojetos
def create_page_subproject_token(page, subproject, back_project=None):
# Pagina de Ficha edital de subprojeto

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    sp = SupaBase(page)

    get_info2 = subproject


    def go_back():
        if back_project != None:
            loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page , project=back_project))
        else:
            loading.new_loading_page(page=page, call_layout=lambda: create_page_list_subproject(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))
    
    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]

    file_config = {
            "dwg": ["dwg", "dwg"],
            "planner1": ["xlsx", "planner1"],
            "planner2": ["xlsx", "planner2"],
        }

    def editar_dados(view_subproject):
        
        data_subproject = view_subproject
        print("")
        print(view_subproject["name_subproject"].value)
        print(view_subproject["predicted_lots"].value)
        print(view_subproject["lots_done"].value)
        print(view_subproject["deliverys"].value)
        print(view_subproject["recommended_medium"].value)
        print(view_subproject["percent"].value)
        print(view_subproject["ortofoto"].value)
        print("")

        data_subproject["name_subproject"] = view_subproject["name_subproject"].value
        data_subproject["predicted_lots"] = view_subproject["predicted_lots"].value
        data_subproject["lots_done"] = view_subproject["lots_done"].value
        data_subproject["deliverys"] = view_subproject["deliverys"].value
        data_subproject["recommended_medium"] = view_subproject["recommended_medium"].value
        data_subproject["percent"] = view_subproject["percent"].value
        data_subproject["ortofoto"] = view_subproject["ortofoto"].value
        data_subproject["project"] = view_subproject["project"].value
        data_subproject["final_delivery"] = view_subproject["final_delivery"].value
        data_subproject["current_average"] = view_subproject["current_average"].value
        data_subproject["type"] = view_subproject["type"].value
        data_subproject["dwg"] = view_subproject["dwg"].value
        data_subproject["planner1"] = view_subproject["planner1"].value
        data_subproject["planner2"] = view_subproject["planner2"].value

        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            if add_file[0] == True:
                local = file_config[file_type[0]][1]
                ext = file_config[file_type[0]][0]
                response1 = sp.add_subproject_storage(file_selected[0], file_name[0], ext, local)

                if response1.status_code == 200 or response1.status_code == 201:

                    data_subproject[local] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/{local}//{file_name[0]}"
                    response2 = sp.edit_subproject_data(data_subproject)

                    if response2.status_code in [200, 204]:
                        loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page, project=data_subproject["project"]))
                        snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
            else:
                response2 = sp.edit_subproject_data(data_subproject)

                if response2.status_code in [200, 204]:
                    loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page, project=data_subproject["project"]))
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )

    view_subproject = {

        "name_subproject":ft.TextField(label="Nome do Subprojeto", value=get_info2["name_subproject"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "predicted_lots":ft.TextField(label="Lotes Previstos", value=get_info2["predicted_lots"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "lots_done":ft.TextField(label="Lotes Feitos", value=get_info2["lots_done"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "deliverys":ft.TextField(label="Entregas", value=get_info2["deliverys"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "recommended_medium":ft.TextField(label="Média Recomendada", value=get_info2["recommended_medium"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "percent":ft.TextField(label="Porcentagem", value=get_info2["percent"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "ortofoto":ft.TextField(label="Ortofoto", value=get_info2["ortofoto"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "project":ft.TextField(label="Projeto", value=get_info2["project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "final_delivery":ft.TextField(label="Entrega Final", value=get_info2["final_delivery"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "current_average":ft.TextField(label="Média Atual", value=get_info2["current_average"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "type":ft.TextField(label="Tipo", value=get_info2["type"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "dwg":ft.TextField(label="DWG", value=get_info2["dwg"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "planner1":ft.TextField(label="Planilha 1", value=get_info2["planner1"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "planner2":ft.TextField(label="Planilha 2", value=get_info2["planner2"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
    }


    def on_file_selected():

        data = (datetime.now().strftime("%d/%m/%Y")).replace("/", "")

        name_file = f'{view_subproject["name_subproject"].value}.{file_config[file_type[0]][0]}'
        file_name.clear()
        file_name.append(name_file)

        view_subproject[file_config[file_type[0]][1]].value = file_old_name[0]

        add_file[0] = True

        page.update()

    def get_uploaded_file_bytes(e: ft.FilePickerUploadEvent):

        file_path = f"uploads/{file_old_name[0]}"    

        with open(file_path, "rb") as file:
            file_content = file.read()

        file_selected.clear()
        file_selected.append(file_content)

        on_file_selected()

    def on_image_selected(e: ft.FilePickerResultEvent):

            if not e.files or len(e.files) == 0:
                return
            
            file_selected.clear()
            file_selected.append(e.files[0])
            file_old_name.clear()
            file_old_name.append(e.files[0].name)



            if e.page.web:
                #  Gerar a URL temporária
                temp_url = e.page.get_upload_url(file_selected[0].name, 3600)

                #  Criar objeto para upload
                file_upload = ft.FilePickerUploadFile(file_selected[0].name, temp_url)

                #  Realiza o upload
                fp.upload([file_upload])

            else:
                on_file_selected()

    fp = ft.FilePicker(on_result=on_image_selected, on_upload=get_uploaded_file_bytes, data="fp")
    page.overlay.append(fp)

    def open_gallery(e, type): 
        fp.pick_files(              
            allow_multiple=False,
        )

        file_type.clear()
        file_type.append(type)

    btn_edit = buttons.create_button(on_click=lambda e: editar_dados(view_subproject),
                                      text="Editar Dados",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
    
    btn_dwg = buttons.create_button(on_click=lambda e: open_gallery(e, type="dwg"),
                                      text="Upload DWG",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,)
    
    btn_planner1 = buttons.create_button(on_click=lambda e: open_gallery(e, type="planner1"),
                                      text="Upload Planilha 1",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,)
    
    btn_planner2 = buttons.create_button(on_click=lambda e: open_gallery(e, type="planner2"),
                                      text="Upload Planilha 2",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,)

    

    projects_token = ft.Container(
        content=ft.Column(
            controls=[
                *(view_subproject.values()),
                btn_dwg,
                btn_planner1,
                btn_planner2
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,  # Permite que a Column expanda com o conteúdo
        ),
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(1000, page.width * 0.9),  # Largura responsiva
        # REMOVIDA a altura fixa - agora se ajusta ao conteúdo
        alignment=ft.alignment.top_center,  # Alinhamento no topo para melhor distribuição
        margin=10,
        expand=True  # Permite que o Container expanda verticalmente
    )

    # Layout responsivo
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 6},
                controls=[
                    projects_token,
                    btn_edit,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START,  # Alinha no topo
                spacing=20,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,  # Alinha no topo
        spacing=20,
        expand=True
    )

    return layout

def create_page_new_subproject(page, project):

    sp = SupaBase(page=page)
    loading = LoadingPages(page=page)

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    def send_to_data(view_subproject):

        data_subproject = view_subproject
        
        data_subproject["name_subproject"] = view_subproject["name_subproject"].value
        data_subproject["predicted_lots"] = view_subproject["predicted_lots"].value
        data_subproject["recommended_medium"] = view_subproject["recommended_medium"].value
        data_subproject["final_delivery"] = view_subproject["final_delivery"].value
        data_subproject["type"] = view_subproject["type"].value
        data_subproject["project"] = project
        data_subproject["lots_done"] = "0"
        data_subproject["ortofoto"] = "."
        data_subproject["deliverys"] = "1"
        data_subproject["percent"] = "0"
        data_subproject["project"] = project
        data_subproject["current_average"] = "0"
        data_subproject["dwg"] = "."
        data_subproject["planner1"] = "."
        data_subproject["planner2"] = "."

        sp = SupaBase(page=page)
        data = ((sp.get_one_project_data(project)).json())[0]
        string_subprojects = (data["current_subprojects"]).split(",")

        string_subprojects.append(data_subproject["name_subproject"])

        if any(field== "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            response1 = sp.post_subproject_data(data_subproject)
            if response1.status_code == 201: 
                response2 = sp.edit_projects_data(
                    data_project={
                        "name_project": project,
                        "current_subprojects": ",".join(string_subprojects)
                    }
                )
                if response2.status_code in [200, 204]:
                    loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page, project=project))
                    snack_bar = ft.SnackBar(content=ft.Text("Subrpojeto criado"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()

    view_subproject = {
                "name_subproject": ft.TextField(label="Subprojeto", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="name_subproject"),
                "predicted_lots": ft.TextField(label="Lotes Previstos", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="predicted_lots"),
                "recommended_medium": ft.TextField(label="Média", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="recommended_medium"),
                "type":ft.Dropdown(
                                    options=[
                                        ft.dropdown.Option("poligonos"),
                                        ft.dropdown.Option("fotos"),
                                    ],
                                    label="Tipo",
                                    text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                    bgcolor=ft.Colors.WHITE,
                                    width=300,
                                    data="type",
                                ),
                "final_delivery": ft.TextField(label="Entrega", bgcolor=ft.Colors.WHITE, expand= False, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), data="final_delivery"),
    }


    btn_send = ft.ElevatedButton("Enviar", on_click=lambda e: send_to_data(view_subproject))  

    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Adicionar Subprojeto", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                *[item for item in view_subproject.values()],
                btn_send
            ],
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.WHITE,
        padding=10,
        border_radius=10,
        expand=True,
        alignment=ft.alignment.center,
    )

    layout = ft.ResponsiveRow(
        [
            ft.Column(
                [main_container],
                col={"sm": 12, "md": 8, "lg": 6},
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        vertical_alignment=ft.CrossAxisAlignment.CENTER, 
    )

    return layout



def create_page_new_freelancer(page):

    loading = LoadingPages(page=page)
    
    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))
    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_freelancers(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    # Campos do formulário
    campos = {
        "nome": ft.TextField(label="Nome", hint_text="Digite o nome", bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "Usuario": ft.TextField(label="Usuario", hint_text="Digite o Usuario",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "pix": ft.TextField(label="PIX", hint_text="Digite o chave PIX",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "email": ft.TextField(label="Email", hint_text="Digite o email",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
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
    
    # Layout principal da página
    layout_principal = ft.ResponsiveRow(
        [
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},  # Define o tamanho do container em diferentes breakpoints
                controls=list(campos.values()) + [botao_enviar],
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

    loading = LoadingPages(page=page)

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_deliverys(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
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
                "id": ft.TextField(label="ID", hint_text="Digite o ID", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "username": dropdown1,
                "date": ft.TextField(label="Data", hint_text="Digite a Data", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "name_subproject": dropdown2,
                "project": dropdown3,
                "polygons": ft.TextField(label="Poligonos", hint_text="Digite o Poligonos", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "errors": ft.TextField(label="Erros", hint_text="Digite o Erros", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "discount": ft.TextField(label="Desconto", hint_text="Digite o Desconto", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "warnings": ft.TextField(label="Advertencias", hint_text="Digite o Advertencias", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "delay": ft.TextField(label="Atraso", hint_text="Digite o Atraso", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "file": ft.TextField(label="Arquivos", hint_text="Digite o Arquivos", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
                "photos": ft.TextField(label="Fotos", hint_text="Digite o Fotos", bgcolor=ft.Colors.WHITE, width=field_width, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
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

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
        ],
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
def create_page_see_freelancers(page):

    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    get_base = base.get_all_user_data()
    get_json = get_base.json()

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # Lista para exibir as entregas
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
                        ft.DataColumn(ft.Text(value="Usuario", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Permissão", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Projeto Atual", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Ficha", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
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

    # Preenche a lista com os dados das entregas
    for delev in get_json:
        
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['permission']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['current_project']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, username=delev['username']: loading.new_loading_page(
                                        page=page,
                                        call_layout=lambda: create_page_freelancer_token(page=page, username=username)
                                    ),
                                )),
                            
                        ]
                )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    def filtrar_usuarios(e):
        texto = e.control.value.lower().strip()
        
        for item in history_list.controls[0].content.rows:
            item.visible = texto in item.cells[0].content.value.lower() if texto else True

        history_list.update()

    # Campo de pesquisa
    search_field = ft.TextField(
        label="Pesquisar",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        hint_text="Digite para pesquisar...",
        border_color=ft.Colors.BLUE_800,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        width=350,
        on_change=filtrar_usuarios,
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                controls=[
                    ft.Text("Freelancers", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: loading.new_loading_page(
                            page=page,
                            call_layout=lambda: create_page_new_freelancer(page=page),
                            ),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                search_field,
                history_list,  # Adiciona a lista de entregas
            ],
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.WHITE,
        padding=10,
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
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return layout

def create_page_freelancer_token(page, username):

    loading = LoadingPages(page=page)
    base = SupaBase(page=page)
    get_base_Project = base.get_user_data(username)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_freelancers(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))
    
    def editar_dados(view_project):
        
        data_project = view_project

        data_project["name"] = view_project["name"].value
        data_project["current_project"] = view_project["current_project"].value
        data_project["username"] = view_project["username"].value
        data_project["password"] = view_project["password"].value
        data_project["email"] = view_project["email"].value
        data_project["permission"] = view_project["permission"].value
        data_project["payment"] = view_project["payment"].value
        data_project["weekly_deliveries"] = "0"
        data_project["total_deliverys"] = "0"
        data_project["polygons_made"] = "0"
        data_project["delays"] = "0"
        data_project["warnings"] = "0"
        data_project["polygons_wrong"] = "0"

        
        if any(field == "" or field is None for field in data_project.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            response = sp.edit_user_data(data_project)
            if response.status_code in [200, 204]:
                loading.new_loading_page(page=page, call_layout=lambda: create_page_see_freelancers(page=page))
                snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )

    view_project ={
        "name": ft.TextField(label="Nome do Freelancer", value=get_info2["name"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "current_project": ft.TextField(label="Projeto Atual", value=get_info2["current_project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "username": ft.TextField(label="Nome de Usuario", value=get_info2["username"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "password": ft.TextField(label="Senha", value=get_info2["password"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "email": ft.TextField(label="Email", value=get_info2["email"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "permission": ft.TextField(label="Senha", value=get_info2["permission"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "payment": ft.TextField(label="Pix", value=get_info2["payment"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
    }

    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(view_project))

    projects_token = ft.Container(
    content=ft.Column(
        controls=view_project.values(),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza os itens na horizontal
        scroll=ft.ScrollMode.AUTO,  # Adiciona scroll se necessário
    ),
    padding=20,
    border=ft.border.all(2, ft.Colors.BLUE),
    border_radius=10,
    bgcolor=ft.Colors.WHITE,
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



def create_page_see_deliverys(page):

    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    get_base = base.get_all_deliverys()
    get_json = get_base.json()

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # Lista para exibir as entregas
    history_list = ft.Column(
        controls=[
            ft.Container(
                padding=0,  
                expand=True,  
                theme=texttheme1,
                clip_behavior=ft.ClipBehavior.NONE,  
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=40,  
                    expand=True,
                    expand_loose=True,
                    columns=[
                        ft.DataColumn(ft.Text(value="Usuario", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Data", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
                        ft.DataColumn(ft.Text(value="Poligonos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
                        ft.DataColumn(ft.Text(value="Fotos", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
                        ft.DataColumn(ft.Text(value="", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
                    ],
                    rows=[],
                    clip_behavior=ft.ClipBehavior.NONE  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,  
    )

    # Preenche a lista com os dados das entregas
    for delev in get_json:
        
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['date']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['name_subproject']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['polygons']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['photos']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                expand=True,
                                on_click=lambda e, delivery=delev: loading.new_loading_page(
                                        page=page,
                                        call_layout=lambda: create_page_delivery_details(page=page, delivery=delivery)
                                    ),
                                )),
                            
                        ]
                )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    filtros_ativos = {
    "dia": None,
    "mes": None,
    "ano": None,
    "usuario": None,
    "subprojeto": None
    }

    # Função para filtrar a tabela
    def aplicar_filtros():
        for item in history_list.controls[0].content.rows:
            dia = ((item.cells[1].content.value).split("/"))[0]  
            mes = ((item.cells[1].content.value).split("/"))[1]  
            ano = ((item.cells[1].content.value).split("/"))[2]  
            usuario = item.cells[0].content.value  
            subproject = item.cells[2].content.value  

            # Verifica se o item atende a TODOS os filtros ativos
            item.visible = (
                (filtros_ativos["dia"] is None or filtros_ativos["dia"] == dia) and
                (filtros_ativos["mes"] is None or filtros_ativos["mes"] == mes) and
                (filtros_ativos["ano"] is None or filtros_ativos["ano"] == ano) and
                (filtros_ativos["subprojeto"] is None or filtros_ativos["subprojeto"] == subproject) and
                (filtros_ativos["usuario"] is None or filtros_ativos["usuario"] == usuario)
            )

        history_list.update()  # Atualiza a UI

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()



    subprojects = (base.get_all_subprojects()).json()
    name_subprojects = [ft.dropdown.Option("Nulo")]
    for item in subprojects:
        name_subprojects.append(ft.dropdown.Option(item["name_subproject"]))

    users = (base.get_all_user_data()).json()
    name_users = [ft.dropdown.Option("Nulo")]
    for item in users:
        name_users.append(ft.dropdown.Option(item["username"]))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Dia",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("07"),
                    ft.dropdown.Option("14"),
                    ft.dropdown.Option("21"),
                    ft.dropdown.Option("28"),
                ],
                on_change=lambda e: on_dropdown_change(e, "dia"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Mês",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("01"),
                    ft.dropdown.Option("02"),
                    ft.dropdown.Option("03"),
                    ft.dropdown.Option("04"),
                    ft.dropdown.Option("05"),
                    ft.dropdown.Option("06"),
                    ft.dropdown.Option("07"),
                    ft.dropdown.Option("08"),
                    ft.dropdown.Option("09"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("11"),
                    ft.dropdown.Option("12"),  
                ],
                on_change=lambda e: on_dropdown_change(e, "mes"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Ano",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("2025"),
                    ft.dropdown.Option("2026"),
                ],
                on_change=lambda e: on_dropdown_change(e, "ano"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Usuário",
                expand=True,
                options=name_users,
                on_change= lambda e: on_dropdown_change(e, "usuario"),
                enable_filter=True,
                editable=True,
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                label="Subprojeto",
                expand=True,
                options=name_subprojects,
                on_change=lambda e: on_dropdown_change(e, "subprojeto"),
                enable_filter=True,
                editable=True,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                controls=[
                    ft.Text("Entregas", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: loading.new_loading_page(
                            page=page,
                            call_layout=lambda: create_page_new_delivery(page=page),
                            ),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                list_dropdown,
                history_list,  # Adiciona a lista de entregas
            ],
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.WHITE,
        padding=10,
        border_radius=10,
        expand=True,
        clip_behavior=ft.ClipBehavior.NONE,
        alignment=ft.alignment.center,
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

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_deliverys(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
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
        ft.TextField(label="Usuário", value=f"{delivery['username']}", width=300, color=ft.Colors.BLACK), 
        ft.TextField(label="Data", value=f"{delivery['date']}", width=300, color=ft.Colors.BLACK), 
        ft.TextField(label="Subprojeto", value=f"{delivery['name_subproject']}", width=300, color=ft.Colors.BLACK), 
        ft.TextField(label="Projeto", value=f"{delivery['project']}", width=300, color=ft.Colors.BLACK),  
        ft.TextField(label="Polígonos", value=f"{delivery['polygons']}", width=300, color=ft.Colors.BLACK), 
        ft.TextField(label="Erros", value=f"{delivery['errors']}", width=300, color=ft.Colors.BLACK),  
        ft.TextField(label="Desconto", value=f"{delivery['discount']}", width=300, color=ft.Colors.BLACK),  
        ft.TextField(label="Advertências", value=f"{delivery['warning']}", width=300, color=ft.Colors.BLACK),  
        ft.TextField(label="Atrasos", value=f"{delivery['delay']}", width=300, color=ft.Colors.BLACK), 
        ft.TextField(label="Arquivo", value=f"{delivery['file']}", width=300, color=ft.Colors.BLACK),  
        ft.TextField(label="Fotos", value=f"{delivery['photos']}", width=300, color=ft.Colors.BLACK),  
    ],
    spacing=10,
    scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
)

# Lista com os TextFields
    data_list = [   
    ft.TextField(label="Usuário", value=f"{delivery['username']}", width=300, color=ft.Colors.BLACK),  # usuario_field
    ft.TextField(label="Data", value=f"{delivery['date']}", width=300, color=ft.Colors.BLACK),  # data_field
    ft.TextField(label="Subprojeto", value=f"{delivery['name_subproject']}", width=300, color=ft.Colors.BLACK),  # subprojeto_field
    ft.TextField(label="Projeto", value=f"{delivery['project']}", width=300, color=ft.Colors.BLACK),  # projeto_field
    ft.TextField(label="Polígonos", value=f"{delivery['polygons']}", width=300, color=ft.Colors.BLACK),  # poligonos_field
    ft.TextField(label="Erros", value=f"{delivery['errors']}", width=300, color=ft.Colors.BLACK),  # erros_field
    ft.TextField(label="Desconto", value=f"{delivery['discount']}", width=300, color=ft.Colors.BLACK),  # desconto_field
    ft.TextField(label="Advertências", value=f"{delivery['warning']}", width=300, color=ft.Colors.BLACK),  # advertencias_field
    ft.TextField(label="Atrasos", value=f"{delivery['delay']}", width=300, color=ft.Colors.BLACK),  # atrasos_field
    ft.TextField(label="Arquivo", value=f"{delivery['file']}", width=300, color=ft.Colors.BLACK),  # arquivo_field
    ft.TextField(label="Fotos", value=f"{delivery['photos']}", width=300, color=ft.Colors.BLACK),  # fotos_field
]
    botao_edit = ft.ElevatedButton("Editar", on_click=lambda e: editar_dados(data_list))
    # Container principal
    main_container = ft.Container(
        content=details_layout,
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
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
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

    get_base = base.get_all_files()
    get_json = get_base.json()


    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # Lista para exibir as entregas
    history_list = ft.Column(
        controls=[
            ft.Container(
                padding=0,  
                expand=True,  
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=40,  
                    expand=True,  
                    columns=[
                        ft.DataColumn(ft.Text(value="Usuario", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Data", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Tipo", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="Quantidade", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
                        ft.DataColumn(ft.Text(value="", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
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

    # Preenche a lista com os dados das entregas
    for delev in get_json:

        
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['date']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['subproject']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['type']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.Text(
                                value=f"{delev['amount']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, files=delev: loading.new_loading_page(
                                        page=page,
                                        call_layout=lambda: create_page_files_details(page=page, files=files)
                                    ),
                                )),
                            
                        ]
                )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )


    filtros_ativos = {
    "dia": None,
    "mes": None,
    "ano": None,
    "usuario": None,
    "subprojeto": None
    }

    # Função para filtrar a tabela
    def aplicar_filtros():
        for item in history_list.controls[0].content.rows:
            dia = ((item.cells[1].content.value).split("/"))[0]  
            mes = ((item.cells[1].content.value).split("/"))[1]  
            ano = ((item.cells[1].content.value).split("/"))[2]  
            usuario = item.cells[0].content.value  
            subproject = item.cells[2].content.value  

            # Verifica se o item atende a TODOS os filtros ativos
            item.visible = (
                (filtros_ativos["dia"] is None or filtros_ativos["dia"] == dia) and
                (filtros_ativos["mes"] is None or filtros_ativos["mes"] == mes) and
                (filtros_ativos["ano"] is None or filtros_ativos["ano"] == ano) and
                (filtros_ativos["subprojeto"] is None or filtros_ativos["subprojeto"] == subproject) and
                (filtros_ativos["usuario"] is None or filtros_ativos["usuario"] == usuario)
            )

        history_list.update()  # Atualiza a UI

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()



    subprojects = (base.get_all_subprojects()).json()
    name_subprojects = [ft.dropdown.Option("Nulo")]
    for item in subprojects:
        name_subprojects.append(ft.dropdown.Option(item["name_subproject"]))

    users = (base.get_all_user_data()).json()
    name_users = [ft.dropdown.Option("Nulo")]
    for item in users:
        name_users.append(ft.dropdown.Option(item["username"]))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Dia",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("07"),
                    ft.dropdown.Option("14"),
                    ft.dropdown.Option("21"),
                    ft.dropdown.Option("28"),
                ],
                on_change=lambda e: on_dropdown_change(e, "dia"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Mês",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("01"),
                    ft.dropdown.Option("02"),
                    ft.dropdown.Option("03"),
                    ft.dropdown.Option("04"),
                    ft.dropdown.Option("05"),
                    ft.dropdown.Option("06"),
                    ft.dropdown.Option("07"),
                    ft.dropdown.Option("08"),
                    ft.dropdown.Option("09"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("11"),
                    ft.dropdown.Option("12"),  
                ],
                on_change=lambda e: on_dropdown_change(e, "mes"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Ano",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo"),
                    ft.dropdown.Option("2025"),
                    ft.dropdown.Option("2026"),
                ],
                on_change=lambda e: on_dropdown_change(e, "ano"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Usuário",
                expand=True,
                options=name_users,
                on_change= lambda e: on_dropdown_change(e, "usuario"),
                enable_filter=True,
                editable=True,
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                label="Subprojeto",
                expand=True,
                options=name_subprojects,
                on_change=lambda e: on_dropdown_change(e, "subprojeto"),
                enable_filter=True,
                editable=True,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Arquivos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                list_dropdown,
                history_list,  
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        bgcolor=ft.Colors.WHITE,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
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

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_files(page=page))

    def go_home():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_initial_adm(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda e: go_home(), icon_color=ft.Colors.BLACK),
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

  


    # Campos para exibir os detalhes da entrega
    details_layout = ft.Column(
    controls=[
        ft.Text("Detalhes da Entrega", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),  # Título        
        ft.TextField(label="Usuário", value=f"{files['username']}", width=300, color=ft.Colors.BLACK),  # usuario_field
        ft.TextField(label="Data", value=f"{files['date']}", width=300, color=ft.Colors.BLACK),  # data_field
        ft.TextField(label="Subprojeto", value=f"{files['subproject']}", width=300, color=ft.Colors.BLACK),  # subprojeto_field
        ft.TextField(label="type", value=f"{files['type']}", width=300, color=ft.Colors.BLACK),  # erros_field
        ft.TextField(label="amount", value=f"{files['amount']}", width=300, color=ft.Colors.BLACK),  # desconto_field
        ft.TextField(label="url", value=f"{files['url']}", width=300, color=ft.Colors.BLACK),  # advertencias_field
    ],
    spacing=10,
    scroll=ft.ScrollMode.AUTO,  # Habilita o scroll
)

# Lista com os TextFields
    data_list = [   
    ft.TextField(label="Usuário", value=f"{files['username']}", width=300, color=ft.Colors.BLACK),  # usuario_field
    ft.TextField(label="Data", value=f"{files['date']}", width=300, color=ft.Colors.BLACK),  # data_field
    ft.TextField(label="Subprojeto", value=f"{files['subproject']}", width=300, color=ft.Colors.BLACK),  # subprojeto_field
    ft.TextField(label="type", value=f"{files['type']}", width=300, color=ft.Colors.BLACK),
    ft.TextField(label="amount", value=f"{files['amount']}", width=300, color=ft.Colors.BLACK),
    ft.TextField(label="url", value=f"{files['url']}", width=300, color=ft.Colors.BLACK),  # advertencias_field
]
    
    # Container principal
    main_container = ft.Container(
        content=details_layout,
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
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




























































































































