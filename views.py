import flet as ft
from models import *
import flet.map as map
from datetime import datetime, timedelta



def create_page_login(page):

    page.client_storage.clear()
    
    container = []
    page.appbar = None
    if page.drawer:
        page.drawer = None

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

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Enter":
            verificar(login.value, password.value, page)
            
    page.on_keyboard_event = on_keyboard

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
    dict_profile = page.client_storage.get("profile")

    
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
    
    dicio_total_deliverys = {}
    total_polygons = 0  # Todos os poligonos que o usuario fez
    total_errors = 0  # Todos os erros que o usuario cometeu
    total_delays = 0  # Todos os atrasos que o usuario cometeu
    number_total_deliverys = 0  # Todos as entregas que o usuario fez

    temp_list1 = []

    for row in data_total_deliverys:  #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas

        date = row["date"]
        name_subproject = row["name_subproject"]
        polygons = row["polygons"]
        errors = row["errors"]
        discount = row["discount"]
        photos = row["photos"]
        delay = row["delay"]
        dwg = row["dwg"]

        date_delivery_dt1 = datetime.strptime(date, "%d/%m/%Y")

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
        
        temp_list1.append((date_delivery_dt1, linha))

        number_total_deliverys += 1
        total_polygons += int(polygons)
        total_errors += int(errors)

        if delay == "Sim":
            total_delays += 1


     # Ordena a lista pela data (mais recente primeiro)
    temp_list1.sort(reverse=True, key=lambda x: x[0])

    # Cria uma lista ordenada para ser usada no Flet
    dicio_total_deliverys = [linha for _, linha in temp_list1] 



    #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas
    #....................................................................

    #....................................................................
    #Filtrando entregas baseado no projeto atual

    current_deliverys = sp.get_user_deliverys_data(subproject=dict_profile["current_project"]) 
    data_current_deliverys = current_deliverys.json()
    
    subproject_polygons = 0   # Todos os poligonos feitos no subprojeto   
    number_current_deliverys = 0  # Todos as entregas feitas no subprojeto

    if dict_profile["current_project"] not in [".", "", None]:
        for row in data_current_deliverys:   #Filtrando entregas baseado no projeto atual

            polygons = row["polygons"]
            photos = row["photos"]

            number_current_deliverys += 1
            subproject_polygons += int(polygons)


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

    if dict_profile["current_project"] not in [".", "", None]:
        for row in data_total_deliverys:

                date = row["date"]
                polygons = row["polygons"]
                errors = row["errors"]
                discount = row["discount"]
                delay = row["delay"]
                photos = row["photos"]
                username = row["username"]

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
                else:
                    pass
                
                    

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

    if dict_profile["current_project"] not in [".", "", None]:
        subproject3 = sp.get_subproject_data(subproject=dict_profile["current_project"]) 
        data3 = subproject3.json()
        row3 = data3[0]
        row3["lots_done"] = subproject_polygons
        percent = (subproject_polygons * 100) / (int(row3["predicted_lots"]))
        row3["percent"] = f"{percent:.2f} %"


    # Atualizando dados do subprojeto atual
    #....................................................................

    #....................................................................
    # Atualizando dados financeiros

    total_cash_polygons = float((delivery_07[0]+delivery_14[0]+delivery_21[0]+delivery_28[0]) * 0.60)
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

    text_date_file_before = []
    test2 = ft.Text(value="", size=20)
    text_date_file_before.append(test2)

    def change_text_date(text_date_file, week):

        date = {
            "now": {
                "now":datetime.now(),
                "day":datetime.now().day,
                "month":datetime.now().month,
                "year":datetime.now().year
            },
            "before": {
                "now":datetime.now() - timedelta(days=7),
                "day":(datetime.now() - timedelta(days=7)).day,
                "month":(datetime.now() - timedelta(days=7)).month,
                "year":(datetime.now() - timedelta(days=7)).year
            },
        }


        date_file = date[week]["day"]

        dias = {
        i: 7 if i > 28 or i <= 7 else 
        14 if i > 7 and i <= 14 else 
        21 if i > 14 and i <= 21 else 
        28 
        for i in range(1, 32)
        }

        month = date[week]["month"]
        year = date[week]["year"]
        if date_file > 28:
            month += 1
            if month == 13:
                month = 1
                year += 1


        day_date_file = f"{(dias[date_file]):02d}/{month:02d}/{year:02d}"

        request_date_file = sp.check_file(date=day_date_file, username=dict_profile["username"])

        if len(request_date_file.json()) > 0:
            text_date_file[0].value = f"Entrega de {day_date_file} realizada"
            text_date_file[0].color = ft.Colors.GREEN
        else:
            text_date_file[0].value = f"Entrega de {day_date_file} não realizada"
            text_date_file[0].color = ft.Colors.RED
            
        page.update()

    change_text_date(text_date_file, "now")    
    change_text_date(text_date_file_before, "before")    

    # Texto de verificação de entregaK)
    #....................................................................

    #....................................................................
    # Criação de tabelas

    # Tabela do Usuario
    table1 = geo_objects.view_user_data(row2)
    form1 = forms.create_forms_post(table1, "Informções", "Freelancer", ft.MainAxisAlignment.START)

    # Tabela do subprojeto
    table2 = ft.Container()
    if dict_profile["current_project"] not in [".", "", None]:
        table2 = geo_objects.view_user_data2(row3)
    form2 = ft.Container()
    if dict_profile["current_project"] not in [".", "", None]:
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
                    rows=dicio_total_deliverys,  
                ),
            )
        ],
        scroll=ft.ScrollMode.AUTO,  
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=300,  
        expand=True,  
    )

    def get_preview_image():
            
        if dict_profile["current_project"] not in [".", "", None]:

            if row3["preview"] in [".", "", None]:
                image = ft.Text("Sem Imagem", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
            else:
                image = ft.Image(  
                            src=row3["preview"],  
                            fit=ft.ImageFit.COVER,
                            expand=True,
                        )
        else:
            image = ft.Text("Sem Imagem", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)

        return image

    # Tabela da ortofoto
    container_ortofoto = ft.Container(content=get_preview_image(), border_radius=20, height=((page.height) / 2),)

    # Criação de tabelas
    #....................................................................

    #....................................................................
    # Inserção de arquivo

    def send_file(file_path):



        container = None
        overlay_copy = list(page.overlay)
        for item in overlay_copy:
                if item.data == "fp" or item.data == "bar":
                    pass
                else:
                    container = item
                    
        if container.controls[0].content.controls[3].value == "":
            snack_bar = ft.SnackBar(
                content=ft.Text("Preencha todos os campos!"),
                bgcolor=ft.Colors.RED,
                duration=2000,
                data="bar",
                )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
            return
            
        data = (container.controls[0].content.controls[3].value).split("/")

        extension = "dwg"
        if row3["type"] == "fotos":
            extension = "xlsx"
        name_file = f'{dict_profile["username"]}_{data[0]}{data[1]}{data[2]}.{extension}'

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

                data_convertida = datetime.strptime(date, "%d/%m/%Y").replace(hour=23, minute=59, second=59)
                data_atual = datetime.now()

                if data_convertida < data_atual:
                    delay = "Sim"
                else:
                    delay = "Não"

                response2 = sp.post_to_files(
                                            id=id,   
                                            date=container.controls[0].content.controls[3].value,
                                            username=dict_profile["username"],
                                            subproject=dict_profile["current_project"],
                                            type=row3["type"],
                                            average=row3["recommended_medium"],
                                            amount=container.controls[0].content.controls[7].value,
                                            delay = delay,
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
                    change_text_date(text_date_file, "now")
                    change_text_date(text_date_file_before, "before")
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

                    snack_bar = ft.SnackBar(
                    content=ft.Text(value=f"Falha ao enviar arquivo {response2.status_code} - {response2.text}", color=ft.Colors.BLACK),
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
        
        btn_send = buttons.create_button(on_click=lambda e: send_file(file_selected[0]),
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
                                    ft.Text(value="Arquivo:", color=ft.Colors.BLACK),
                                    ft.TextField(
                                        value=f"{file_name[0]}",
                                        read_only=True,
                                        bgcolor=ft.Colors.WHITE,
                                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                        border_radius=0,
                                    ),
                                    ft.Text(value="Data da entrega:", color=ft.Colors.BLACK),
                                    ft.Dropdown(
                                        value="",
                                        options=[
                                            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                                content=ft.Text(value=f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                                                color=ft.Colors.BLACK)),
                                            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                               content=ft.Text(value=f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                                                color=ft.Colors.BLACK)),
                                            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                               content=ft.Text(value=f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                                                color=ft.Colors.BLACK)),
                                            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                               content=ft.Text(value=f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                                                color=ft.Colors.BLACK)),
                                            ft.dropdown.Option(f"07/{next_month:02d}/{year:02d}",
                                                               content=ft.Text(value=f"07/{next_month:02d}/{year:02d}",
                                                                                color=ft.Colors.BLACK)),
                                        ],
                                        color=ft.Colors.BLACK,
                                        bgcolor=ft.Colors.WHITE,
                                        fill_color=ft.Colors.WHITE,
                                        filled=True,
                                        width=300,
                                    ),
                                    ft.Text(value="Tipo de entrega:", color=ft.Colors.BLACK),
                                    ft.TextField(
                                        value=row3["type"],
                                        read_only=True,
                                        bgcolor=ft.Colors.WHITE,
                                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                                        border_radius=0,
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
    
    url = None
    if dict_profile["current_project"] not in [".", "", None]:
        url = (((sp.get_one_project_data(row3["project"])).json())[0])["ecw"]

    btn_ecw = buttons.create_button(on_click=lambda e: page.launch_url(url),
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
    container_form3 = ft.Container(content=ft.Column(controls=[text_date_file_before[0], text_date_file[0], form3],
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
    dict_profile = page.client_storage.get("profile")
    
    btn_exit = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_login(page)),
                                      text="Logout",
                                      color=ft.Colors.RED,
                                      col=12,
                                      padding=10,)
    btn_projeto = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_project(page)),
                                      text= "Projetos",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)         
    btn_see_file = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_files(page)),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_deliverys(page)),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_freelancers(page)),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_see_models(page)),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: loading.new_loading_page(page=page, call_layout=lambda:create_page_payment(page)),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
        controls=[
            btn_projeto,
            btn_see_freelancers,
            btn_payment,
            btn_see_file,
            btn_see_deliverys,
            btn_see_models,
            btn_exit,
            ]
        )

    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto)  
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment) 
    
    page.drawer = drawer

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(drawer), icon_color=ft.Colors.BLACK),
        
        
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
        polygons = row["polygons"]
        photos = row["photos"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]
        warning = row["warning"]

        dicio_all_deliverys[id] = {
                                    "id": id,
                                    "username": username,
                                    "date": date,
                                    "name_subproject": name_subproject,
                                    "polygons": polygons,
                                    "photos": photos,
                                    "errors": errors,
                                    "discount": discount,
                                    "delay": delay,
                                    "warning": warning,
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

    response = sp.check_login(username=username, password=password, page=page)

    if response.status_code == 200 and len(response.json()) > 0:

        data = response.json()
        row = data[0]
        name = row["name"]
        username = row["username"]
        permission = row["permission"]
        current_project = row["current_project"]

        page.client_storage.set("profile", {
            "username": username,
            "name": name,
            "permission": permission,
            "current_project": current_project,
            "deliveries_filter": [None],
            "models_filter": [None],
            "freelancers_filter": [None],
            "files_filter": [None],
        })
        
        if permission == "user":

            loading.new_loading_page(page=page,
            call_layout=lambda:create_page_user(page),
            )

        elif permission != "adm":

            page.go("/files")

        else:
            page.go("/freelancers")
        
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
    dict_profile = page.client_storage.get("profile")
    buttons = Buttons(page)

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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)



    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    base = SupaBase(page=None)
    get_base = base.get_projects_data()
    get_json = get_base.json()

    def go_back():
        page.go("/freelancers")
   

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
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout
# Pagina Lateral de Projetos
def create_page_project_token(page, project):

    loading = LoadingPages(page=page)
    base = SupaBase(page=page)
    buttons = Buttons(page)
    get_base_Project = base.get_one_project_data(project)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )

    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]

    file_config = {
            "dwg": ["dwg", "dwg"],
            "planner1": ["xlsx", "planner1"],
            "planner2": ["xlsx", "planner2"],
            "preview": ["jpg", "preview"],
        }
  
    def editar_dados(view_project):
        
        data_project = view_project.copy()

        data_project["name_project"] = view_project["name_project"].value
        data_project["current_subprojects"] = view_project["current_subprojects"].value
        data_project["final_delivery"] = view_project["final_delivery"].value
        data_project["predicted_lots"] = view_project["predicted_lots"].value
        data_project["ecw"] = view_project["ecw"].value
        data_project["planner"] = view_project["planner"].value
        data_project["preview"] = view_project["preview"].value
        data_project["dwg"] = view_project["dwg"].value

        
        if add_file[0] == True:
            local = file_config[file_type[0]][1]
            ext = file_config[file_type[0]][0]
            response1 = base.add_subproject_storage(file_selected[0], file_name[0], ext, local)

            if response1.status_code == 200 or response1.status_code == 201:

                data_project[local] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/{local}//{file_name[0]}"
                response2 = base.edit_projects_data(data_project)

                if response2.status_code in [200, 204]:
                    loading.new_loading_page(page=page, call_layout=lambda: create_page_project_token(page=page, project=data_project["name_project"]))
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao enviar arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            base.edit_projects_data(data_project)
            loading.new_loading_page(page=page, call_layout=lambda: create_page_project_token(page=page, project=data_project["name_project"]))
            snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    
    view_project = {
        "name_project": ft.TextField(label="Nome do projeto", value=get_info2["name_project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), disabled=True),
        "current_subprojects": ft.TextField(label="Subprojetos", value=get_info2["current_subprojects"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), disabled=True),
        "final_delivery": ft.TextField(label="Entrega final", value=get_info2["final_delivery"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "predicted_lots": ft.TextField(label="Lotes Previstos", value=get_info2["predicted_lots"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "ecw": ft.TextField(label="Ortofotos", value=get_info2["ecw"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "planner": ft.TextField(label="Planilha", value=get_info2["planner"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "preview": ft.TextField(label="Prévia", value=get_info2["preview"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "dwg": ft.TextField(label="Dwg", value=get_info2["dwg"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
    }


    botao_edit = buttons.create_button(on_click=lambda e: editar_dados(view_project),
                                      text="Editar Dados",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5
                                      )


    def on_file_selected():

        name_file = f'{view_project["name_project"].value}.{file_config[file_type[0]][0]}'
        file_name.clear()
        file_name.append(name_file)

        view_project[file_config[file_type[0]][1]].value = file_old_name[0]

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


    view_column = ft.Column(
        controls=[
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    def delete_dwg(local, type, ext):

   
        name_file = f'{get_info2["name_project"]}.{ext}'
        response1 = base.delete_storage(local=local, object=f"{name_file}", type=type)
        if response1.status_code in [200, 204]:
            data = {}
            data["name_project"] = get_info2["name_project"]
            data[local] = "."
            response2 = base.edit_projects_data(data)

            if response2.status_code in [200, 204]:
                loading.new_loading_page(page=page, call_layout=lambda: create_page_project_token(page=page, project=data["name_project"]))
                snack_bar = ft.SnackBar(content=ft.Text(f"{local} excluido"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir {local}: {response1.text}"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    for item in view_project.items():
        
        if item[0] == "preview":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="preview"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("preview", "image/jpeg", "jpg"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        elif item[0] == "dwg":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="dwg"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("dwg", "image/vnd.dwg", "dwg"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        else:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))


    projects_token = ft.Container(
        content=view_column,
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(800, page.width * 0.9),  # Largura máxima de 800px ou 90% da tela
        height=min(900, page.height * 0.8),  # Altura máxima de 900px ou 80% da tela
        alignment=ft.alignment.center,  # Centraliza o conteúdo dentro do container
        margin=10,  # Margem externa
    )


    # Layout responsivo
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
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
        )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha no topo
        spacing=20,
        expand=True
    )


    return layout

def create_page_project_token_user(page):

    base = SupaBase(page=page)
    buttons = Buttons(page)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()
    dict_profile = page.client_storage.get("profile")
    project = dict_profile["current_project"]


    buttons = Buttons(page)
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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)



    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    get_base_Project = base.get_one_project_data(project)
    get_info1 = get_base_Project.json()

    get_info2 = {
        "preview": ".",
        "ecw": ".",
        "planner": ".",
    }

    if len(get_info1) > 0:
        get_info2 = get_info1[0]

    get_info3 = {
        "preview": ".",
        "ecw": ".",
    }

    get_base = base.get_all_subproject_data_type(project)

    if len(get_info1) > 0:
        get_info3 = get_base.json()
   
    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
    )

   
    def get_preview_image():
            if get_info2["preview"] in [".", "", None]:
                image = ft.Text("Sem Imagem", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
            else:
                image = ft.Image(  
                            src=get_info2["preview"],  
                            fit=ft.ImageFit.COVER,
                            expand=True,
                        )
            
            return image

    btn_download = buttons.create_button(on_click=lambda e: page.launch_url(get_info2["dwg"]),
                                      text="DWG Acumulado",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,)
    
    url = get_info2["ecw"]
    btn_ecw = buttons.create_button(on_click=lambda e: page.launch_url(url),
                                      text="Ortofoto e arquivos",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )
    url2 = get_info2["planner"]
    btn_planner = buttons.create_button(on_click=lambda e: page.launch_url(url2),
                                      text="Planilha",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,
                                      )


    preview_image = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value=project, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20),
                ft.Container(
                    width=500,
                    height=500,
                    alignment=ft.alignment.center,
                    content=get_preview_image(),
                    border=ft.Border(
                        left=ft.BorderSide(2, ft.Colors.BLACK),  
                        top=ft.BorderSide(2, ft.Colors.BLACK),    
                        right=ft.BorderSide(2, ft.Colors.BLACK), 
                        bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                    ),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=ft.border_radius.all(20),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
                btn_download,
                btn_ecw,
                btn_planner
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        ),
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(1000, page.width * 0.9),
        alignment=ft.alignment.center,  
        margin=10,
        expand=True  
    )

    

    if len(get_info1) == 0:
        preview_image.content.controls.remove(btn_download)
        preview_image.content.controls.remove(btn_ecw)
        preview_image.content.controls.remove(btn_planner)
    

    history_list = ft.Column(
        controls=[
            ft.Container(
                width=500,
                height=500,
                alignment=ft.alignment.center,
                border=ft.Border(
                    left=ft.BorderSide(2, ft.Colors.BLACK),  
                    top=ft.BorderSide(2, ft.Colors.BLACK),    
                    right=ft.BorderSide(2, ft.Colors.BLACK), 
                    bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                ),
                bgcolor=ft.Colors.WHITE,
                border_radius=ft.border_radius.all(20),
                padding=0,  
                expand=True,  
                theme=texttheme1,
                content=ft.DataTable(
                    data_row_max_height=50,
                    column_spacing=40,  
                    expand=True,  
                    columns=[
                        ft.DataColumn(ft.Text(value="Subprojeto", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Usuario", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                        ft.DataColumn(ft.Text(value="Perímetro", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
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

    users = {}
    get_users = (base.get_frella_user_data()).json()
    for item in get_users:
        users[item["current_project"]] = item["username"]

    if len(get_info1) > 0:
        for city in get_info3:

            def get_subproject(city):
                return city["name_subproject"]
            def get_name(city):
                return users.get(city["name_subproject"], ".")
            def get_url(city):
                return city["dwg"]


            history_list.controls[0].content.rows.append(
                ft.DataRow(cells=[
                                ft.DataCell(ft.Text(
                                    value=get_subproject(city),
                                    theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                    text_align=ft.TextAlign.CENTER,
                                    color=ft.Colors.BLACK,
                                    )),
                                ft.DataCell(ft.Text(
                                    value=get_name(city),
                                    theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                    text_align=ft.TextAlign.CENTER,
                                    color=ft.Colors.BLACK,
                                    )),

                                ft.DataCell(ft.ElevatedButton(
                                    text="Download",
                                    bgcolor=ft.Colors.AMBER,
                                    color=ft.Colors.WHITE,
                                    width=150,
                                    on_click=lambda e, url=get_url(city): page.launch_url(url),
                                )),
                ])
            )

    # Layout responsivo
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
            [
                ft.Container(
                    preview_image,
                    alignment=ft.alignment.center
                ),
            ],
            col={"sm": 12, "md": 6},
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
            [
                ft.Container(
                    history_list,
                    alignment=ft.alignment.center
                ),
            ],
            col={"sm": 12, "md": 6},
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha no topo
        spacing=20,
        expand=True
    )




    return layout

# Pagina de Ficha Editavel de Projetos
def create_page_new_project(page):

    loading = LoadingPages(page=page)
    sp = SupaBase(page)


    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
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
                new_dicio["preview"] = "."
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

    get_base_Project = base.get_one_project_data(project)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

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

    list_subprojects = []

    for city in get_json:
        name_subproject = city["name_subproject"]
        list_subprojects.append(name_subproject)
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


    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
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


    def get_preview_image():
        if get_info2["preview"] in [".", "", None]:
            image = ft.Text("Sem Imagem", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        else:
            image = ft.Image(  
                        src=get_info2["preview"],  
                        fit=ft.ImageFit.COVER,
                        expand=True,
                    )
        
        return image

    get_models = ((base.get_all_models()).json())

    count_poligons = 0
    count_unknown = 0
    models = 0

    for model in get_models:
        if model["subproject"] in list_subprojects:
            models += 1
            count_poligons = count_poligons + int(model["polygons"])
            count_unknown = count_unknown + (int(model["polygons"]) - int(model["numbers"]))

    if models == 0:
        text_poligons = ft.Text(value=f"0 / {get_info2["predicted_lots"]} ({count_poligons/(int(get_info2["predicted_lots"])/100):.2f}%)", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)
        text_regular = ft.Text(value=f"Regulares e Prefeitura: 0", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)
        text_unknown = ft.Text(value=f"Dúvidas: 0", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)
    else:    
        text_poligons = ft.Text(value=f"Imóveis: {count_poligons} / {get_info2["predicted_lots"]} ({count_poligons/(int(get_info2["predicted_lots"])/100):.2f}%)", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)
        text_regular = ft.Text(value=f"Regulares e Prefeitura: {count_poligons - count_unknown}", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)
        text_unknown = ft.Text(value=f"Dúvidas: {count_unknown} ({(count_unknown/(count_poligons/100)):.0f}%)", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, size=20)

    preview_image = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    width=500,
                    height=500,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                                controls=[
                                    get_preview_image(),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                scroll=ft.ScrollMode.AUTO,
                                expand=True,
                                spacing=10,
                            ),
                    border=ft.Border(
                        left=ft.BorderSide(2, ft.Colors.BLACK),  
                        top=ft.BorderSide(2, ft.Colors.BLACK),    
                        right=ft.BorderSide(2, ft.Colors.BLACK), 
                        bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                    ),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=ft.border_radius.all(20),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
                text_poligons,
                text_regular,
                text_unknown,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        ),
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(1000, page.width * 0.9),
        alignment=ft.alignment.center,  
        margin=10,
        expand=True  
    )

    
    # Layout responsivo
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
            [
                main_container
            ],
            col={"sm": 12, "md": 6},
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
                col={"sm": 12, "md": 6},
                controls=[
                    preview_image,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,  # Alinha no topo
                spacing=20,
                expand=True
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha no topo
        spacing=20,
        expand=True
    )

    return layout
# Pagina de Subprojetos - Continuação de Projetos

def create_page_subproject_token(page, subproject, back_project=None):
# Pagina de Ficha edital de subprojeto

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    sp = SupaBase(page)

    get_info2 = subproject


    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject(page=page , project=back_project))
        

    
    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]

    file_config = {
            "dwg": ["dwg", "dwg"],
            "planner1": ["xlsx", "planner1"],
            "planner2": ["xlsx", "planner2"],
            "preview": ["jpg", "preview"],
        }

    def editar_dados(view_subproject):
        
        data_subproject = view_subproject.copy()

        data_subproject["name_subproject"] = view_subproject["name_subproject"].value
        data_subproject["predicted_lots"] = view_subproject["predicted_lots"].value
        data_subproject["lots_done"] = view_subproject["lots_done"].value
        data_subproject["deliverys"] = view_subproject["deliverys"].value
        data_subproject["recommended_medium"] = view_subproject["recommended_medium"].value
        data_subproject["percent"] = view_subproject["percent"].value
        data_subproject["project"] = view_subproject["project"].value
        data_subproject["final_delivery"] = view_subproject["final_delivery"].value
        data_subproject["type"] = view_subproject["type"].value
        data_subproject["preview"] = view_subproject["preview"].value
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
                        snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao enviar arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
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
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )

    def go_download(view_deliveries, object):
        if view_deliveries[object].value != "." and view_deliveries[object].value != "":
            page.launch_url(view_deliveries[object].value)

    current_deliverys = sp.get_user_deliverys_data(subproject=get_info2["name_subproject"]) 
    data_current_deliverys = current_deliverys.json()
    
    subproject_polygons = 0   # Todos os poligonos feitos no subprojeto   
    number_current_deliverys = 0  # Todos as entregas feitas no subprojeto
    percent = f"0 %"

    if get_info2["name_subproject"] not in [".", "", None]:
        for row in data_current_deliverys:   #Filtrando entregas baseado no projeto atual

            polygons = row["polygons"]
            photos = row["photos"]

            number_current_deliverys += 1
            subproject_polygons += int(polygons)
        percent = f"{(subproject_polygons * 100) / (int(get_info2["predicted_lots"])):.2f} %"

    

    view_subproject = {

        "name_subproject":ft.TextField(label="Nome do Subprojeto", value=get_info2["name_subproject"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "predicted_lots":ft.TextField(label="Lotes Previstos", value=get_info2["predicted_lots"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "lots_done":ft.TextField(label="Lotes Feitos", value=subproject_polygons, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "deliverys":ft.TextField(label="Entregas", value=number_current_deliverys, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "recommended_medium":ft.TextField(label="Média Recomendada", value=get_info2["recommended_medium"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "percent":ft.TextField(label="Porcentagem", value=percent, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "project":ft.TextField(label="Projeto", value=get_info2["project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "final_delivery":ft.TextField(label="Entrega Final", value=get_info2["final_delivery"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "type":ft.TextField(label="Tipo", value=get_info2["type"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "preview":ft.TextField(label="Preview", value=get_info2["preview"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), on_click=lambda e: go_download(view_subproject, "preview")), 
        "dwg":ft.TextField(label="DWG", value=get_info2["dwg"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), on_click=lambda e: go_download(view_subproject, "dwg")), 
        "planner1":ft.TextField(label="Planilha 1", value=get_info2["planner1"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), on_click=lambda e: go_download(view_subproject, "planner1")), 
        "planner2":ft.TextField(label="Planilha 2", value=get_info2["planner2"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), on_click=lambda e: go_download(view_subproject, "planner2")), 
    }
    
    
    name_freela = "."
    try:
        name_freela = (((sp.get_user_by_subproject(subproject=get_info2["name_subproject"], permission="user")).json())[0])["username"]
    except:
        name_freela = "."

    def go_freelancer(name_freela):
        if name_freela not in [".", ""]:
            profile = page.client_storage.get("profile")
            profile.update({
                "freelancer": name_freela,
                "filtros": [None]
            })
            page.client_storage.set("profile", profile)
            page.go("/freelancers/token")
        else:
            pass

    freelancer = ft.Row(
                controls=[
                    ft.TextField(
                        label="Freelancer atual",
                        value=name_freela,
                        width=300,
                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                        read_only=True,
                        ),
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: go_freelancer(name_freela)
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
    
    name_est = "."
    try:
        name_est = (((sp.get_user_by_subproject(subproject=get_info2["name_subproject"], permission="est")).json())[0])["username"]
    except:
        name_est = "."

    def go_freelancer(name_est):
        if name_est not in [".", ""]:
            profile = page.client_storage.get("profile")
            profile.update({
                "freelancer": name_est,
                "filtros": [None]
            })
            page.client_storage.set("profile", profile)
            page.go("/freelancers/token")
        else:
            pass

    estagiario = ft.Row(
                controls=[
                    ft.TextField(
                        label="Estagiário atual",
                        value=name_est,
                        width=300,
                        text_style=ft.TextStyle(color=ft.Colors.BLACK),
                        read_only=True,
                        ),
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: go_freelancer(name_est)
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )


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


    def delete_dwg(local, type, ext):

        base = SupaBase(page=page)

        name_file = f'{get_info2["name_subproject"]}.{ext}'
        response1 = base.delete_storage(local=local, object=f"{name_file}", type=type)
        if response1.status_code in [200, 204]:
            data = {}
            data["name_subproject"] = get_info2["name_subproject"]
            data[local] = "."
            response2 = sp.edit_subproject_data(data)

            if response2.status_code in [200, 204]:
                get_info2[local] = "."  
                loading.new_loading_page(page=page, call_layout=lambda: create_page_subproject_token(page=page, subproject=get_info2))
                snack_bar = ft.SnackBar(content=ft.Text(f"{local} excluido"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir {local}: {response1.text}"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    btn_edit = buttons.create_button(on_click=lambda e: editar_dados(view_subproject),
                                      text="Editar Dados",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
    

    view_column = ft.Column(
        controls=[
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    for item in view_subproject.items():
        
        if item[0] == "preview":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="preview"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("preview", "image/jpeg", "jpg"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        elif item[0] == "dwg":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="dwg"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("dwg", "image/vnd.dwg", "dwg"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        elif item[0] == "planner1":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="planner1"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("planner1", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "xlsx"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        elif item[0] == "planner2":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="planner2"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_dwg("planner2", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "xlsx"),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        else:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))


    projects_token = ft.Container(
        content=ft.Column(
            controls=[
                view_column,
                ft.Text(""),
                ft.Text(""),
                ft.Text(""),
                freelancer,
                estagiario,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        ),
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(1000, page.width * 0.9),  
        alignment=ft.alignment.top_center,  
        margin=10,
        expand=True  
    )

    def get_preview_image():
        if subproject["preview"] in [".", "", None]:
            image = ft.Text("Sem Imagem", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        else:
            image = ft.Image(  
                        src=subproject["preview"],  
                        fit=ft.ImageFit.COVER,
                        expand=True,
                    )
        
        return image

    preview_image = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    width=500,
                    height=500,
                    alignment=ft.alignment.center,
                    content=get_preview_image(),
                    border=ft.Border(
                        left=ft.BorderSide(2, ft.Colors.BLACK),  
                        top=ft.BorderSide(2, ft.Colors.BLACK),    
                        right=ft.BorderSide(2, ft.Colors.BLACK), 
                        bottom=ft.BorderSide(2, ft.Colors.BLACK) 
                    ),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=ft.border_radius.all(20),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        ),
        padding=20,
        border=ft.border.all(2, ft.Colors.BLUE),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=min(1000, page.width * 0.9),
        alignment=ft.alignment.center,  
        margin=10,
        expand=True  
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
            ),
            ft.Column(
                col={"sm": 12, "md": 6},
                controls=[
                    preview_image
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,  # Alinha no topo
                spacing=20,
                expand=True
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha no topo
        spacing=20,
        expand=True
    )

    return layout

def create_page_new_subproject(page, project):

    sp = SupaBase(page=page)
    loading = LoadingPages(page=page)

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_project(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
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
        data_subproject["preview"] = "."
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
    buttons = Buttons(page)
    

    def go_back():
        loading.new_loading_page(page=page, call_layout=lambda: create_page_see_freelancers(page=page))

    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    dropdow3 = ft.Dropdown(
        options=[
            ft.dropdown.Option("adm"),
            ft.dropdown.Option("user"),
        ],
        label="Permissão",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        width=300,
        )

    # Campos do formulário
    view_user = {
        "name": ft.TextField(label="Nome", hint_text="Digite o nome", bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "username": ft.TextField(label="Usuario", hint_text="Digite o Usuario",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "password": ft.TextField(label="Senha", hint_text="Digite a Senha",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "payment": ft.TextField(label="Pagamento", hint_text="Digite o Pagamento",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "email": ft.TextField(label="Email", hint_text="Digite o email",bgcolor=ft.Colors.WHITE, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
        "permission": dropdow3
    }

    # Função para enviar os dados (simulação)
    def enviar_dados(view_user):
        
        data_subproject = view_user.copy()

        data_subproject["name"] = view_user["name"].value
        data_subproject["username"] = view_user["username"].value
        data_subproject["password"] = view_user["password"].value
        data_subproject["payment"] = view_user["payment"].value
        data_subproject["email"] = view_user["email"].value
        data_subproject["permission"] = view_user["permission"].value
        data_subproject["weekly_deliveries"] = "0"
        data_subproject["total_deliverys"] = "0"
        data_subproject["polygons_made"] = "0"
        data_subproject["delays"] = "0"
        data_subproject["warnings"] = "0"
        data_subproject["current_project"] = "."
        data_subproject["polygons_wrong"] = "0"


        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            sp = SupaBase(page)
            response = sp.create_user_data(data_subproject)
            if response.status_code in [200, 201]:
                loading.new_loading_page(page=page, call_layout=lambda: create_page_see_freelancers(page=page))
                snack_bar = ft.SnackBar(content=ft.Text("Usuário criado"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao criar usuário: {response.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

    botao_enviar = buttons.create_button(on_click=lambda e: enviar_dados(view_user),
                                      text="Enviar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)

    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Adicionar Freelancer", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                *[item for item in view_user.values()],
                botao_enviar
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
# Pagina de Fichas Criacionais de Freelancers
def create_page_new_delivery(page):

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    sp = SupaBase(page)
    dict_profile = page.client_storage.get("profile")

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        page.go("/deliveries")


    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]


    def editar_dados(view_deliveries):
        
        data_subproject = view_deliveries.copy()

        data_subproject["id"] = str(sp.get_delivery_id())
        data_subproject["username"] = view_deliveries["username"].value
        data_subproject["date"] = view_deliveries["date"].value
        data_subproject["name_subproject"] = view_deliveries["name_subproject"].value
        data_subproject["polygons"] = view_deliveries["polygons"].value
        data_subproject["errors"] = view_deliveries["errors"].value
        data_subproject["discount"] = view_deliveries["discount"].value
        data_subproject["warning"] = view_deliveries["warning"].value
        data_subproject["delay"] = view_deliveries["delay"].value
        data_subproject["photos"] = view_deliveries["photos"].value
        data_subproject["dwg"] = view_deliveries["dwg"].value

        del data_subproject["type"]
        

        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        
        if data_subproject["dwg"] == ".":
            snack_bar = ft.SnackBar(content=ft.Text("Insira um arquivo para fazer o envio"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return

        check = (sp.get_one_delivery_data(data_subproject["date"], data_subproject["name_subproject"])).json()

        if len (check) > 0:
            snack_bar = ft.SnackBar(content=ft.Text("Entrega especificada já cadastrada !!!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        
        check2 = (sp.get_one_file_data(data_subproject["date"], data_subproject["name_subproject"])).json()

        if len (check2) < 1:
            snack_bar = ft.SnackBar(content=ft.Text("Nenhum arquivo encontrado na data especificada !!!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return

        if add_file[0] == True:

            response1 = sp.add_subproject_storage(file_selected[0], file_name[0], file_type[0], "deliveries")

            if response1.status_code == 200 or response1.status_code == 201:
                data_subproject["dwg"] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/deliveries//{file_name[0]}"
                response2 = sp.post_to_deliverys_data(data_subproject)

                if response2.status_code in [200, 201]:
                    page.go("/deliveries")
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir tabela: {response2.text}"), bgcolor=ft.Colors.AMBER)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            response2 = sp.post_to_deliverys_data(data_subproject)

            if response2.status_code in [200, 204]:
                page.go("/deliveries")
                snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir tabela: {response2.text}"), bgcolor=ft.Colors.AMBER)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()


    # Campos para exibir os detalhes da entrega

    dropdow3 = ft.Dropdown(
        options=[
            ft.dropdown.Option("Sim", content=ft.Text(value="Sim", color=ft.Colors.BLACK)),
            ft.dropdown.Option("Não", content=ft.Text(value="Não", color=ft.Colors.BLACK)),
        ],
        label="Atraso",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        )

    subprojects = [ft.dropdown.Option(".", content=ft.Text(value=".", color=ft.Colors.BLACK))]
    if dict_profile["permission"] != "adm":
        project = ((sp.get_one_project_data(dict_profile["current_project"])).json())[0]
        subprojects_list = (project["current_subprojects"]).split(",")
        get_subprojects = (sp.get_all_subprojects_filter(subprojects_list, "poligonos,fotos")).json()
    else:
        get_subprojects = (sp.get_all_subprojects()).json()
    for item in get_subprojects:
        subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    dropdow2 = ft.Dropdown(
        options=subprojects,
        label="SubProjeto",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        )
    
    users = []
    if dict_profile["permission"] != "adm":
        get_users = (sp.get_frella_user_data_filter(subprojects_list)).json()
    else:
        get_users = (sp.get_frella_user_data()).json()
    for item in get_users:
        users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    find_file = ["."]

    def on_dropdow_changed(e):
        if e.control.data == "drop_user":
            value = (((sp.get_user_data(e.control.value)).json())[0])
            dropdow2.value = value["current_project"]
            find_file.clear()
            find_file.append(value["current_project"])
        else:
            if find_file[0] != ".":
                try:
                    dropdow3.value = (((sp.get_one_file_data(e.control.value, find_file[0])).json())[0])["delay"]
                except:
                    None

        page.update()

    dropdow1 = ft.Dropdown(
        options=users,
        label="Usuário",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        data="drop_user",
        on_change=on_dropdow_changed
        )
    
    
    next_month = datetime.now().month + 1
    year1 = datetime.now().year
    if next_month == 13:
        next_month = 1
        year1 += 1

    before_month = datetime.now().month - 1
    year2 = datetime.now().year
    if before_month == 0:
        before_month = 12
        year2 -= 1

    dropdow4 = ft.Dropdown(
        label="Data",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"28/{before_month:02d}/{year2:02d}",
                                content=ft.Text(value=f"28/{before_month:02d}/{year2:02d}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{next_month:02d}/{year1:02d}",
                                content=ft.Text(value=f"07/{next_month:02d}/{year1:02d}",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,
        data="drop_date",
        on_change=on_dropdow_changed
    )

    dropdow5 = ft.Dropdown(
        options=[
            ft.dropdown.Option("dwg", content=ft.Text(value="Poligonos", color=ft.Colors.BLACK)),
            ft.dropdown.Option("xlsx", content=ft.Text(value="Fotos", color=ft.Colors.BLACK)),
        ],
        label="Tipo",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        )

    dropdow1.value = dict_profile.get("delivery_username", "")
    dropdow4.value = dict_profile.get("delivery_date", "")
    dropdow2.value = dict_profile.get("delivery_subproject", "")
    dropdow3.value = dict_profile.get("delivery_delay", "")
    dropdow5.value = dict_profile.get("delivery_type", "")

    view_deliveries = {
        "username": dropdow1, 
        "date":dropdow4, 
        "name_subproject":dropdow2,   
        "polygons":ft.TextField(label="Polígonos", value=dict_profile["delivery_polygons"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)), 
        "errors":ft.TextField(label="Erros", value=dict_profile["delivery_errors"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)), 
        "discount":ft.TextField(label="Descontos", value=dict_profile["delivery_discount"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)), 
        "warning":ft.TextField(label="Advertências", value=dict_profile["delivery_warning"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)), 
        "delay":dropdow3, 
        "photos":ft.TextField(label="Fotos", value=dict_profile["delivery_photos"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)), 
        "type":dropdow5, 
        "dwg":ft.TextField(label="DWG", value=f"", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True), 
    }

    def on_keyboard(e: ft.KeyboardEvent):
        profile = page.client_storage.get("profile")
        profile.update({
            "delivery_username": dropdow1.value,
            "delivery_date": dropdow4.value,
            "delivery_subproject": dropdow2.value,
            "delivery_type": dropdow5.value,
            "delivery_delay": dropdow3.value,
            "delivery_polygons": view_deliveries["polygons"].value,
            "delivery_errors": view_deliveries["errors"].value,  
            "delivery_discount": view_deliveries["discount"].value,  
            "delivery_warning": view_deliveries["warning"].value,  
            "delivery_photos": view_deliveries["photos"].value,  
        })
        page.client_storage.set("profile", profile)

    page.on_keyboard_event = on_keyboard

    def on_file_selected():

        date = (view_deliveries["date"].value).split("/")

        name_file = f'{view_deliveries["username"].value}_{view_deliveries["name_subproject"].value}_{date[0]}{date[1]}{date[2]}.{file_type[0]}'
        file_name.clear()
        file_name.append(name_file)

        view_deliveries["dwg"].value = file_old_name[0]

        add_file[0] = True

        page.update()

    def get_uploaded_file_bytes(e: ft.FilePickerUploadEvent):

        dropdow1.disabled = True
        dropdow2.disabled = True
        dropdow4.disabled = True

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

    def open_gallery(e, type, view_deliveries):

        copy = view_deliveries.copy()

        del copy["dwg"]

        if any(field.value == "" or field.value is None for field in copy.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return

        fp.pick_files(              
            allow_multiple=False,
        )

        file_type.clear()
        file_type.append(type)

    def remove_dwg(e):

        view_deliveries["dwg"].value=""

        file_selected.clear()
        file_name.clear()
        file_type.clear()
        file_old_name.clear()
        add_file[0] = False

        dropdow1.disabled = False
        dropdow2.disabled = False
        dropdow4.disabled = False


        page.update()


    botao_edit = buttons.create_button(on_click=lambda e: editar_dados(view_deliveries),
                                      text="Enviar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
     
    btn_dwg = buttons.create_button(on_click=lambda e: open_gallery(e, type=view_deliveries["type"].value, view_deliveries=view_deliveries),
                                      text="Upload Arquivo",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,) 
    
    btn_remove_dwg = buttons.create_button(on_click=lambda e: remove_dwg(e),
                                      text="Remover Arquivo",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5,)

    main_container = ft.Container(
        content=ft.Column(
            controls=[
                *(view_deliveries.values()),
                btn_dwg,
                btn_remove_dwg
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
        alignment=ft.alignment.top_center,  # Alinhamento no topo para melhor distribuição
        margin=10,
        expand=True  # Permite que o Container expanda verticalmente
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
# Pagina de Fichas Criacionais de Entregas
def create_page_payment(page, month=None):

    textthemes = TextTheme()
    buttons = Buttons(page)
    sp = SupaBase(page)
    texttheme1 = textthemes.create_text_theme1()
    loading = LoadingPages(page)
    dict_profile = page.client_storage.get("profile")
    buttons = Buttons(page)
    
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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)



    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    meses_pt_1 = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
    7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    mes_atual = str(meses_pt_1[datetime.now().month])
    ano_atual = str(datetime.now().year)

    if month == None:
        month = mes_atual
        
    request_all_deliverys = sp.get_all_deliverys()
    request_all_deliverys_json = request_all_deliverys.json()
    dicio_all_deliverys = {}

    for row in request_all_deliverys_json:
        
        id = row["id"]
        username = row["username"]
        date = row["date"]
        name_subproject = row["name_subproject"]
        polygons = row["polygons"]
        photos = row["photos"]
        errors = row["errors"]
        discount = row["discount"]
        delay = row["delay"]
        warning = row["warning"]


        dicio_all_deliverys[id] = {
                                    "id": id,
                                    "username": username,
                                    "date": date,
                                    "name_subproject": name_subproject,
                                    "polygons": polygons,
                                    "photos": photos,
                                    "errors": errors,
                                    "discount": discount,
                                    "delay": delay,
                                    "warning": warning,
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
        ft.dropdown.Option("2026"),
    ],
    value="2025",
    text_style=ft.TextStyle(color=ft.Colors.BLACK),
    bgcolor=ft.Colors.WHITE,
    col=6)

    meses_pt_2 = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
    }

    mes = meses_pt_2[dropdown1.value]

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

 
        total = float((delivery_07[0]+delivery_14[0]+delivery_21[0]+delivery_28[0]) * 0.60) + (float((delivery_07[1]+delivery_14[1]+delivery_21[1]+delivery_28[1]) * 0.20))
        total_format = format(total, ".2f")
        

        if number_total_deliverys > 0:

            linha = ft.DataRow(cells=[
                            ft.DataCell(ft.Text(value=name, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK)),
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
                        ft.DataColumn(ft.Text(value="Nome", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Pix", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 07", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 14", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 21", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Entrega dia 28", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
                        ft.DataColumn(ft.Text(value="Total", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),  
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
    


    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                controls=[
                    ft.Text("Relatório Financeiro", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),

                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                container_form2 
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

    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout
# Pagina de Status Financeiros
def create_page_see_freelancers(page):

    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    filtros = dict_profile["freelancers_filter"]
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()

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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_profile = buttons.create_button(on_click=lambda e: page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)


    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    get_base = base.get_all_user_data()
    get_json = get_base.json()

    dicio_projects = {}
    list_projects = (base.get_all_project_data()).json()

    for item in list_projects:

        dicio_projects[item["name_project"]] = (item["current_subprojects"]).split(",")
        dicio_projects[item["name_project"]].append(item["name_project"])

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
                        ft.DataColumn(ft.Text(value="", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
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

    list_filtros = [None]

    # Preenche a lista com os dados das entregas
    for delev in get_json:

        project = next((k for k, v in dicio_projects.items() if delev['current_project'] in v), ".")

        def go_token(delev):
            profile = page.client_storage.get("profile")
            profile.update({
                "freelancer": delev['username'],
                "freelancers_filter": list_filtros
            })
            page.client_storage.set("profile", profile)
            page.go("/freelancers/token")

        perfil = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    content=ft.Image(  # Mova a imagem para o content
                        src=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/freelancers//{delev['username']}.jpg",  
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
        
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(perfil),
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
                                data=project
                                )),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, delev=delev: go_token(delev),
                                )),
                            
                        ]
                )
        )

    filtros_ativos = {
    "permission": None,
    "projeto": None,
    }

    # Função para filtrar a tabela
    def aplicar_filtros(update=True):
        for item in history_list.controls[0].content.rows:
            permission = item.cells[2].content.value  
            project = item.cells[3].content.data  

            # Verifica se o item atende a TODOS os filtros ativos
            item.visible = (
                (filtros_ativos["permission"] is None or filtros_ativos["permission"] == permission) and
                (filtros_ativos["projeto"] is None or filtros_ativos["projeto"] == project)
            )

        if update == True:
            history_list.update()  

        list_filtros[0] = filtros_ativos

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()

    name_projects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    name_projects.append(ft.dropdown.Option(".", content=ft.Text(value=f"Sem Projeto", color=ft.Colors.BLACK)))
    for item in list_projects:
        name_projects.append(ft.dropdown.Option(item["name_project"], content=ft.Text(value=item["name_project"], color=ft.Colors.BLACK)))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Permissão",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                width=300,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("user", content=ft.Text(value=f"Freelancer", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("est", content=ft.Text(value=f"Estagiário", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("ldr", content=ft.Text(value=f"Lider", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("adm", content=ft.Text(value=f"Administrador", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "permission"),
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Projeto",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_projects,
                on_change=lambda e: on_dropdown_change(e, "projeto"),
                enable_filter=True,
                editable=True,
                width=300,
            ),
            
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def filtrar_usuarios(e):
        texto = e.control.value.lower().strip()
        
        for item in history_list.controls[0].content.rows:
            item.visible = texto in item.cells[1].content.value.lower() if texto else True

        list_dropdown.controls[0].value = "Nulo"
        list_dropdown.controls[1].value = "Nulo"

        list_dropdown.controls[0].update()
        list_dropdown.controls[1].update()
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

    if filtros[0] != None:
        
        list_dropdown.controls[0].value = filtros[0]["permission"]
        list_dropdown.controls[1].value = filtros[0]["projeto"]

        filtros_ativos = filtros[0]
        aplicar_filtros(update=False)

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
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[0],
                        list_dropdown.controls[1],
                    ]
                ),
                ft.Container(
                    content=history_list,
                    expand=True,
                    padding=ft.padding.only(bottom=20)
                ),  
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
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout

def create_page_freelancer_token(page):

    loading = LoadingPages(page=page)
    base = SupaBase(page=page)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    est = dict_profile["permission"] != "adm"
    if est == False:
        username = dict_profile["freelancer"]
    else:
        username = dict_profile["username"]
    get_base_Project = base.get_user_data(username)
    get_info1 = get_base_Project.json()
    get_info2 = get_info1[0]

    def go_back():
        if est == True:
            page.go("/files")
        else:
            page.go("/freelancers")

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK)
        ],
    )


    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]

    def editar_dados(view_project):
        
        data_project = view_project.copy()

        data_project["name"] = view_project["name"].value
        data_project["current_project"] = view_project["current_project"].value
        data_project["username"] = view_project["username"].value
        data_project["password"] = view_project["password"].value
        data_project["email"] = view_project["email"].value
        data_project["permission"] = view_project["permission"].value
        data_project["payment"] = view_project["payment"].value
        data_project["weekly_deliveries"] = view_project["weekly_deliveries"].value
        data_project["total_deliverys"] = view_project["total_deliverys"].value
        data_project["polygons_made"] = view_project["polygons_made"].value
        data_project["delays"] = view_project["delays"].value
        data_project["warnings"] = view_project["warnings"].value
        data_project["polygons_wrong"] = view_project["polygons_wrong"].value

        del data_project["image"]

        if any(field == "" or field is None for field in data_project.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            if add_file[0] == True:
                response1 = base.add_subproject_storage(file_selected[0], file_name[0], file_type[0], "freelancers")
                if response1.status_code == 200 or response1.status_code == 201:
                    response2 = base.edit_user_data(data_project)
                    if response2.status_code in [200, 204]:
                        snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                    else:
                        snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response2.text}"), bgcolor=ft.Colors.RED)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()

                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao enviar imagem: {response1.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()

            else:
                response = base.edit_user_data(data_project)
                if response.status_code in [200, 204]:
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()



     #....................................................................
    #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas

    total_deliverys = base.get_deliverys_data_total(username=get_info2["username"])  
    data_total_deliverys = total_deliverys.json()
    
    total_polygons = 0  # Todos os poligonos que o usuario fez
    total_errors = 0  # Todos os erros que o usuario cometeu
    total_delays = 0  # Todos os atrasos que o usuario cometeu
    number_total_deliverys = 0  # Todos as entregas que o usuario fez

    for row in data_total_deliverys:  #Calculo de tudo que já foi feito pelo usuario baseado em todas as entregas

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

    is_editable1 = dict_profile["permission"] != "adm"

    subprojects = []
    subprojects.append(ft.dropdown.Option(".", content=ft.Text(value=".", color=ft.Colors.BLACK)))
    get_subprojects = (base.get_all_subprojects()).json()
    get_projects = (base.get_projects_data()).json()
    for item in get_subprojects:
        subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))
    for item in get_projects:
        subprojects.append(ft.dropdown.Option(item["name_project"], content=ft.Text(value=item["name_project"], color=ft.Colors.BLACK)))

    dropdow2 = ft.Dropdown(
        options=subprojects,
        label="SubProjeto",
        value=get_info2["current_project"],
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=is_editable1,
        )
    
    if est == True:
        dropdow2 = ft.TextField(label="SubProjeto Atual", value=get_info2["current_project"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1)

    dropdow3 = ft.Dropdown(
        options=[
            ft.dropdown.Option("adm", content=ft.Text(value="adm", color=ft.Colors.BLACK)),
            ft.dropdown.Option("est", content=ft.Text(value="est", color=ft.Colors.BLACK)),
            ft.dropdown.Option("ldr", content=ft.Text(value="ldr", color=ft.Colors.BLACK)),
        ],
        label="Permissão",
        value=get_info2["permission"],
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=is_editable1,
        )
    
    view_user ={
        "name": ft.TextField(label="Nome do Freelancer", value=get_info2["name"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "username": ft.TextField(label="Nome de Usuario", value=get_info2["username"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "password": ft.TextField(label="Senha", value=get_info2["password"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "email": ft.TextField(label="Email", value=get_info2["email"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "permission": dropdow3,
        "payment": ft.TextField(label="Pagamento", value=get_info2["payment"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "total_deliverys": ft.TextField(label="Entregas Totais", value=get_info2["total_deliverys"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "weekly_deliveries": ft.TextField(label="Entregas Semanais", value=number_total_deliverys, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "polygons_made": ft.TextField(label="Poligonos Feitos", value=total_polygons, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "polygons_wrong": ft.TextField(label="Poligonos Errados", value=total_errors, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "delays": ft.TextField(label="Atrasos", value=total_delays, width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True),
        "warnings": ft.TextField(label="Advertencias", value=get_info2["warnings"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1),
        "current_project": dropdow2,
        "image": ft.TextField(label="Imagem", value=".", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK)),
    }

    if est == True:
        view_user.pop("payment")
        view_user.pop("total_deliverys")
        view_user.pop("weekly_deliveries")
        view_user.pop("polygons_made")
        view_user.pop("polygons_wrong")
        view_user.pop("delays")
        view_user.pop("warnings")
        view_user.pop("image")

    perfil = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=150,
                height=150,
                alignment=ft.alignment.center,
                content=ft.Image(  # Mova a imagem para o content
                    src=f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/freelancers//{get_info2["username"]}.jpg",  
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
                border_radius=ft.border_radius.all(75),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            )
        ]
    )

    def on_file_selected():

        name_file = f'{view_user["username"].value}.jpg'
        file_name.clear()
        file_name.append(name_file)

        view_user["image"].value = file_old_name[0]

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

    def delete_user(view_files):

        base = SupaBase(page=page)

        data_subproject = view_files.copy()

        data_subproject["username"] = view_files["username"].value

        name_file = f'{view_files["username"].value}.jpg'
        response1 = base.delete_storage(local="freelancers", object=f"{name_file}", type="image/jpeg")   
        response2 = base.delete_user_data(data_subproject)
        if response1.status_code in [200, 204]:
            response2 = base.delete_user_data(data_subproject)
            if response2.status_code in [200, 204]:
                page.go("/freelancers")
                snack_bar = ft.SnackBar(content=ft.Text("Usuário Excluido"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    def delete_image(view_files):

            base = SupaBase(page=page)

            data_subproject = view_files.copy()

            data_subproject["username"] = view_files["username"].value

            name_file = f'{view_files["username"].value}.jpg'
            response1 = base.delete_storage(local="freelancers", object=f"{name_file}", type="image/jpeg")   

            if response1.status_code in [200, 204]:   
                snack_bar = ft.SnackBar(content=ft.Text("Imagem excluida"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir imagem: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()


    botao_edit = buttons.create_button(on_click=lambda e: editar_dados(view_user),
                                      text="Editar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
     
    botao_delete_user = buttons.create_button(on_click=lambda e: delete_user(view_user),
                                      text="Excluir",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5,) 


    view_column = ft.Column(
        controls=[
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    for item in view_user.items():
        
        if item[0] == "image" and est == False:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="jpg"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_image(view_user),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        else:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))


    projects_token = ft.Container(
        content=ft.Column(
            controls=[
                perfil,
                view_column,
                ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.center,  
        margin=10,  
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
                ),
                ft.Container(
                    botao_delete_user,
                    alignment=ft.alignment.center
                ),
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

    if est == True:
        layout.controls[0].controls.pop(2)
        layout.controls[0].controls.pop(1)


    return layout



def create_page_see_deliverys(page):

    buttons = Buttons(page)
    base = SupaBase(page=None)
    textthemes = TextTheme()
    texttheme1 = textthemes.create_text_theme1()
    dict_profile = page.client_storage.get("profile")
    filtros = dict_profile["deliveries_filter"]

    buttons = Buttons(page)
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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)



    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    if dict_profile["permission"] != "adm":
        project = ((base.get_one_project_data(dict_profile["current_project"])).json())[0]
        subprojects_list = (project["current_subprojects"]).split(",")
        get_json = (base.get_all_deliverys_filter(subprojects_list)).json()
    else:
        get_json = (base.get_all_deliverys()).json()
        subprojects_list = (base.get_all_subprojects()).json()

    dicio_projects = {}

    if dict_profile["permission"] != "adm":
        list_projects = [project]
    else:
        list_projects = (base.get_all_project_data()).json()

    for item in list_projects:

        dicio_projects[item["name_project"]] = (item["current_subprojects"]).split(",")

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

    list_filtros = [None]

    # Preenche a lista com os dados das entregas
    for delev in get_json:
        
        project = next((k for k, v in dicio_projects.items() if delev['name_subproject'] in v), None)

        def go_token(delev):
            profile = page.client_storage.get("profile")
            profile.update({
                "delivery": { **delev, "dwg": delev.get("dwg") or "" },
                "deliveries_filter": list_filtros
            })
            page.client_storage.set("profile", profile)
            page.go("/deliveries/token")

    
        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['date']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['name_subproject']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                data=project
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['polygons']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['photos']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                expand=True,
                                on_click=lambda e, delev=delev: go_token(delev),
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            
                        ]
                )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
    )

    filtros_ativos = {
    "dia": None,
    "mes": None,
    "ano": None,
    "usuario": None,
    "projeto": None,
    "subprojeto": None
    }

    # Função para filtrar a tabela
    def aplicar_filtros(update=True):
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
                (filtros_ativos["projeto"] is None or filtros_ativos["projeto"] == project) and
                (filtros_ativos["subprojeto"] is None or filtros_ativos["subprojeto"] == subproject) and
                (filtros_ativos["usuario"] is None or filtros_ativos["usuario"] == usuario)
            )

        if update == True:
            history_list.update()

        list_filtros[0] = filtros_ativos  

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()


    name_projects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in list_projects:
        name_projects.append(ft.dropdown.Option(item["name_project"], content=ft.Text(value=item["name_project"], color=ft.Colors.BLACK)))

    if dict_profile["permission"] != "adm":
        subprojects = (base.get_all_subprojects_filter(subprojects_list, type="poligonos,fotos")).json()
    else:
        subprojects = (base.get_all_subprojects()).json()
    name_subprojects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in subprojects:
        name_subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    users = (base.get_frella_user_data()).json()
    name_users = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in users:
        name_users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Dia",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("14", content=ft.Text(value=f"14", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("21", content=ft.Text(value=f"21", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("28", content=ft.Text(value=f"28", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "dia"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Mês",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("01", content=ft.Text(value=f"01", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("02", content=ft.Text(value=f"02", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("03", content=ft.Text(value=f"03", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("04", content=ft.Text(value=f"04", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("05", content=ft.Text(value=f"05", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("06", content=ft.Text(value=f"06", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("08", content=ft.Text(value=f"08", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("09", content=ft.Text(value=f"09", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("10", content=ft.Text(value=f"10", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("11", content=ft.Text(value=f"11", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("12", content=ft.Text(value=f"12", color=ft.Colors.BLACK)),  
                ],
                on_change=lambda e: on_dropdown_change(e, "mes"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Ano",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2025", content=ft.Text(value=f"2025", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2026", content=ft.Text(value=f"2026", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "ano"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Usuário",
                expand=True,
                options=name_users,
                on_change= lambda e: on_dropdown_change(e, "usuario"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Projeto",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_projects,
                on_change=lambda e: on_dropdown_change(e, "projeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Subprojeto",
                expand=True,
                options=name_subprojects,
                on_change=lambda e: on_dropdown_change(e, "subprojeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    if filtros[0] != None:

        list_dropdown.controls[0].value = filtros[0]["dia"]
        list_dropdown.controls[1].value = filtros[0]["mes"]
        list_dropdown.controls[2].value = filtros[0]["ano"]
        list_dropdown.controls[3].value = filtros[0]["usuario"]
        list_dropdown.controls[4].value = filtros[0]["projeto"]
        list_dropdown.controls[5].value = filtros[0]["subprojeto"]

        filtros_ativos = filtros[0]
        aplicar_filtros(update=False)

    def go_insert():
            profile = page.client_storage.get("profile")
            profile.update({
                "deliveries_filter": list_filtros,
                "delivery_username": "",
                "delivery_date": "",
                "delivery_subproject": "",
                "delivery_type": "",
                "delivery_delay": "",
                "delivery_polygons": "",
                "delivery_errors": "",  
                "delivery_discount": "",  
                "delivery_warning": "",  
                "delivery_photos": "",
                })
            page.client_storage.set("profile", profile)
            page.go("/deliveries/insert")

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                controls=[
                    ft.Text("Entregas", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: go_insert(),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[4],
                        list_dropdown.controls[5],
                        list_dropdown.controls[3],
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[0],
                        list_dropdown.controls[1],
                        list_dropdown.controls[2],
                    ]
                ),
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

    if dict_profile["permission"] == "est":
        main_container.content.controls[0].controls.pop(1)

    # Layout da página
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout
# Pagina De Visualização de Entregas
def create_page_delivery_details(page):

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    delivery = dict_profile["delivery"]
    sp = SupaBase(page)

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        page.go("/deliveries")


    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )


    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]


    def editar_dados(view_deliveries):
        
        data_subproject = view_deliveries.copy()

        data_subproject["username"] = view_deliveries["username"].value
        data_subproject["date"] = view_deliveries["date"].value
        data_subproject["name_subproject"] = view_deliveries["name_subproject"].value
        data_subproject["polygons"] = view_deliveries["polygons"].value
        data_subproject["errors"] = view_deliveries["errors"].value
        data_subproject["discount"] = view_deliveries["discount"].value
        data_subproject["warning"] = view_deliveries["warning"].value
        data_subproject["delay"] = view_deliveries["delay"].value
        data_subproject["photos"] = view_deliveries["photos"].value
        data_subproject["dwg"] = view_deliveries["dwg"].value

        del data_subproject["type"]
        

        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:

            if add_file[0] == True:
        
                response1 = sp.add_subproject_storage(file_selected[0], file_name[0], file_type[0], "deliveries")

                if response1.status_code == 200 or response1.status_code == 201:
                    data_subproject["dwg"] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/deliveries//{file_name[0]}"
                    response2 = sp.edit_delivery_data(data_subproject)

                    if response2.status_code in [200, 204]:
                        profile = page.client_storage.get("profile")
                        profile.update({
                            "delivery": data_subproject,
                        })
                        page.client_storage.set("profile", profile)
                        view_deliveries["dwg"].value = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/deliveries//{file_name[0]}"
                        snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                    else:
                        snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response2.text}"), bgcolor=ft.Colors.RED)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao enviar imagem: {response1.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                response2 = sp.edit_delivery_data(data_subproject)

                if response2.status_code in [200, 204]:
                    profile = page.client_storage.get("profile")
                    profile.update({
                        "delivery": data_subproject,
                    })
                    page.client_storage.set("profile", profile)
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()


    # Campos para exibir os detalhes da entrega
    
    is_editable1 = dict_profile["permission"] != "adm"

    dropdow3 = ft.Dropdown(
        options=[
            ft.dropdown.Option("Sim", content=ft.Text(value="Sim", color=ft.Colors.BLACK)),
            ft.dropdown.Option("Não", content=ft.Text(value="Não", color=ft.Colors.BLACK)),
        ],
        value=delivery['delay'],
        label="Atraso",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        disabled=is_editable1,
        )

    subprojects = [ft.dropdown.Option(".", content=ft.Text(value=".", color=ft.Colors.BLACK))]
    get_subprojects = (sp.get_all_subprojects()).json()
    for item in get_subprojects:
        subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    dropdow2 = ft.Dropdown(
        options=subprojects,
        value=delivery['name_subproject'],
        label="SubProjeto",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=True,
        )

    users = []
    get_users = (sp.get_all_user_data()).json()
    for item in get_users:
        users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    find_file = ["."]

    def on_dropdow_changed(e):
        if e.control.data == "drop_user":
            value = (((sp.get_user_data(e.control.value)).json())[0])
            dropdow2.value = value["current_project"]
            find_file.clear()
            find_file.append(value["current_project"])
        else:
            if find_file[0] != ".":
                dropdow3.value = (((sp.get_one_file_data(e.control.value, find_file[0])).json())[0])["delay"]

        page.update()

    dropdow1 = ft.Dropdown(
        options=users,
        value=delivery['username'],
        label="Usuário",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        data="drop_user",
        on_change=on_dropdow_changed,
        disabled=True,
        )


    next_month = datetime.now().month + 1
    year1 = datetime.now().year
    if next_month == 13:
        next_month = 1
        year1 += 1

    before_month = datetime.now().month - 1
    year2 = datetime.now().year
    if before_month == 0:
        before_month = 12
        year2 -= 1

    dropdow4 = ft.Dropdown(
        value=delivery['date'],
        label="Data",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"28/{before_month:02d}/{year2:02d}",
                                content=ft.Text(value=f"28/{before_month:02d}/{year2:02d}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{next_month:02d}/{year1:02d}",
                                content=ft.Text(value=f"07/{next_month:02d}/{year1:02d}",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,
        data="drop_date",
        on_change=on_dropdow_changed,
        disabled=True,
    )

    current_extension = {
        True: "dwg",
        False: "xlsx"
    }

    dropdow5 = ft.Dropdown(
        options=[
            ft.dropdown.Option("dwg", content=ft.Text(value="Poligonos", color=ft.Colors.BLACK)),
            ft.dropdown.Option("xlsx", content=ft.Text(value="Fotos", color=ft.Colors.BLACK)),
        ],
        label="Tipo",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        value=current_extension[delivery['photos'] == "0"]
        )

    view_deliveries = {
        "username": dropdow1, 
        "date": dropdow4, 
        "name_subproject":dropdow2, 
        "polygons":ft.TextField(label="Polígonos", value=f"{delivery['polygons']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "errors":ft.TextField(label="Erros", value=f"{delivery['errors']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "discount":ft.TextField(label="Descontos", value=f"{delivery['discount']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "warning":ft.TextField(label="Advertências", value=f"{delivery['warning']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "delay":dropdow3,
        "photos":ft.TextField(label="Fotos", value=f"{delivery['photos']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "type":dropdow5, 
        "dwg":ft.TextField(label="DWG", value=f"{delivery['dwg']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True), 
    }

    def on_file_selected():

        date = (view_deliveries["date"].value).split("/")

        name_file = f'{view_deliveries["username"].value}_{view_deliveries["name_subproject"].value}_{date[0]}{date[1]}{date[2]}.{file_type[0]}'
        file_name.clear()
        file_name.append(name_file)

        view_deliveries["dwg"].value = file_old_name[0]

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

    def delete_delivery(view_deliveries):

            base = SupaBase(page=page)

            data_subproject = view_deliveries.copy()

            data_subproject["username"] = view_deliveries["username"].value
            data_subproject["date"] = view_deliveries["date"].value
            data_subproject["name_subproject"] = view_deliveries["name_subproject"].value
            data_subproject["type"] = view_deliveries["type"].value

            extension = {
                "dwg": "image/vnd.dwg",
                "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            }


            date = (data_subproject["date"]).split("/")
            name_file = f'{view_deliveries["username"].value}_{view_deliveries["name_subproject"].value}_{date[0]}{date[1]}{date[2]}.{data_subproject["type"]}'

            response1 = base.delete_storage(local="deliveries", object=f"{name_file}", type=extension[data_subproject["type"]])  
            if response1.status_code in [200, 204]: 
                response2 = base.delete_delivery(data_subproject)

                if response2.status_code in [200, 204]:
                
                        page.go("/deliveries")
                        snack_bar = ft.SnackBar(content=ft.Text("Entrega excluida"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    page.go("/deliveries")
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

    def delete_file(view_deliveries):

            base = SupaBase(page=page)

            data_subproject = view_deliveries.copy()

            data_subproject["username"] = view_deliveries["username"].value
            data_subproject["date"] = view_deliveries["date"].value
            data_subproject["name_subproject"] = view_deliveries["name_subproject"].value
            data_subproject["type"] = view_deliveries["type"].value

            extension = {
                "dwg": "image/vnd.dwg",
                "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            }


            date = (data_subproject["date"]).split("/")
            name_file = f'{view_deliveries["username"].value}_{view_deliveries["name_subproject"].value}_{date[0]}{date[1]}{date[2]}.{data_subproject["type"]}'
            response1 = base.delete_storage(local="deliveries", object=f"{name_file}", type=extension[data_subproject["type"]])
            if response1.status_code in [200, 204]:   
                data_dwg = {"dwg":".", "username": data_subproject["username"], "date": data_subproject["date"], "name_subproject": data_subproject["name_subproject"]}
                response2 = sp.edit_delivery_data(data_dwg)
                if response2.status_code in [200, 204]:
                        profile = page.client_storage.get("profile")
                        profile.update({
                            "delivery": data_dwg,
                        })
                        page.client_storage.set("profile", profile)
                        view_deliveries["dwg"].value = "."
                        snack_bar = ft.SnackBar(content=ft.Text("Arquivo excluido"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

    btn_download = buttons.create_button(on_click=lambda e: page.launch_url(delivery["dwg"]),
                                      text="Download",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,) 
    
    btn_edit = buttons.create_button(on_click=lambda e: editar_dados(view_deliveries),
                                      text="Editar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,) 
    
    btn_delete=ft.Column(
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    col=7,
                    controls=[
                            ft.Container(
                                    alignment=ft.alignment.center,
                                    col=7,
                                    padding=5,
                                    expand=True,
                                    content=ft.ElevatedButton(
                                        text="Excluir",
                                        bgcolor=ft.Colors.RED,
                                        color=ft.Colors.WHITE,
                                        width=150,
                                        on_long_press= lambda e: delete_delivery(view_deliveries),
                                    )
                                )
                            ]    
                        ) 

 
    view_column = ft.Column(
        controls=[
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    for item in view_deliveries.items():
        
        if item[0] == "dwg" and dict_profile["permission"] == "adm":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type=view_deliveries["type"].value),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_file(view_deliveries),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        else:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))


    main_container = ft.Container(
        content=ft.Column(
            controls=[
                view_column
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
        alignment=ft.alignment.top_center,  # Alinhamento no topo para melhor distribuição
        margin=10,
        expand=True  # Permite que o Container expanda verticalmente
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},
                controls=[main_container, btn_download, btn_edit, btn_delete],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    if dict_profile["permission"] != "adm":
        layout.controls[0].controls.remove(btn_delete)
        layout.controls[0].controls.remove(btn_edit)

    return layout
# Pagina De Visualização de Todas as Informações de Entregas



def create_page_files(page, filtros=[None]):

    loading = LoadingPages(page=page)
    base = SupaBase(page=None)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    filtros = dict_profile["files_filter"]


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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)
    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto) 
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    if dict_profile["permission"] != "adm":
        project = ((base.get_one_project_data(dict_profile["current_project"])).json())[0]
        subprojects_list = (project["current_subprojects"]).split(",")
        get_json = (base.get_all_files_filter(subprojects_list)).json()
    else:
        get_json = (base.get_all_files()).json()
        subprojects_list = (base.get_all_subprojects()).json()

    dicio_projects = {}

    if dict_profile["permission"] != "adm":
        list_projects = [project]
    else:
        list_projects = (base.get_all_project_data()).json()

    for item in list_projects:

        dicio_projects[item["name_project"]] = (item["current_subprojects"]).split(",")

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
                        ft.DataColumn(ft.Text(value="Meta", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),
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

    list_filtros = [None]

    # Preenche a lista com os dados das entregas
    for delev in get_json:

        project = next((k for k, v in dicio_projects.items() if delev['subproject'] in v), None)

        def go_token(delev):
            profile = page.client_storage.get("profile")
            profile.update({
                "file": delev,
                "files_filter": list_filtros
            })
            page.client_storage.set("profile", profile)
            page.go("/files/token")

        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['date']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['subproject']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                data=project
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['type']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['amount']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['average']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e, delev=delev: go_token(delev),
                                )),
                            
                        ]
                )
        )

    
    filtros_ativos = {
    "dia": None,
    "mes": None,
    "ano": None,
    "usuario": None,
    "projeto": None,
    "subprojeto": None
    }

    # Função para filtrar a tabela
    def aplicar_filtros(update=True):
        for item in history_list.controls[0].content.rows:
            dia = ((item.cells[1].content.value).split("/"))[0]  
            mes = ((item.cells[1].content.value).split("/"))[1]  
            ano = ((item.cells[1].content.value).split("/"))[2]  
            usuario = item.cells[0].content.value  
            project = item.cells[2].content.data  
            subproject = item.cells[2].content.value  

            # Verifica se o item atende a TODOS os filtros ativos
            item.visible = (
                (filtros_ativos["dia"] is None or filtros_ativos["dia"] == dia) and
                (filtros_ativos["mes"] is None or filtros_ativos["mes"] == mes) and
                (filtros_ativos["ano"] is None or filtros_ativos["ano"] == ano) and
                (filtros_ativos["projeto"] is None or filtros_ativos["projeto"] == project) and
                (filtros_ativos["subprojeto"] is None or filtros_ativos["subprojeto"] == subproject) and
                (filtros_ativos["usuario"] is None or filtros_ativos["usuario"] == usuario)
            )

        if update == True:
            history_list.update()  

        list_filtros[0] = filtros_ativos

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()

    
    name_projects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in list_projects:
        name_projects.append(ft.dropdown.Option(item["name_project"], content=ft.Text(value=item["name_project"], color=ft.Colors.BLACK)))


    if dict_profile["permission"] != "adm":
        subprojects = (base.get_all_subprojects_filter(subprojects_list, type="poligonos,fotos")).json()
    else:
        subprojects = (base.get_all_subprojects()).json()
    name_subprojects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in subprojects:
        name_subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))


    users = (base.get_frella_user_data()).json()
    name_users = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in users:
        name_users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Dia",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("14", content=ft.Text(value=f"14", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("21", content=ft.Text(value=f"21", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("28", content=ft.Text(value=f"28", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "dia"),
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Mês",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("01", content=ft.Text(value=f"01", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("02", content=ft.Text(value=f"02", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("03", content=ft.Text(value=f"03", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("04", content=ft.Text(value=f"04", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("05", content=ft.Text(value=f"05", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("06", content=ft.Text(value=f"06", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("08", content=ft.Text(value=f"08", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("09", content=ft.Text(value=f"09", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("10", content=ft.Text(value=f"10", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("11", content=ft.Text(value=f"11", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("12", content=ft.Text(value=f"12", color=ft.Colors.BLACK)),  
                ],
                on_change=lambda e: on_dropdown_change(e, "mes"),
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Ano",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2025", content=ft.Text(value=f"2025", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2026", content=ft.Text(value=f"2026", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "ano"),
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Usuário",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_users,
                on_change= lambda e: on_dropdown_change(e, "usuario"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Projeto",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_projects,
                on_change=lambda e: on_dropdown_change(e, "projeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Subprojeto",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_subprojects,
                on_change=lambda e: on_dropdown_change(e, "subprojeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


    if filtros[0] != None:
        
        list_dropdown.controls[0].value = filtros[0]["dia"]
        list_dropdown.controls[1].value = filtros[0]["mes"]
        list_dropdown.controls[2].value = filtros[0]["ano"]
        list_dropdown.controls[3].value = filtros[0]["usuario"]
        list_dropdown.controls[4].value = filtros[0]["projeto"]
        list_dropdown.controls[5].value = filtros[0]["subprojeto"]

        filtros_ativos = filtros[0]
        aplicar_filtros(update=False)

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Arquivos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[4],
                        list_dropdown.controls[5],
                        list_dropdown.controls[3],
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[0],
                        list_dropdown.controls[1],
                        list_dropdown.controls[2],
                    ]
                ),
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
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout
# Pagina de Visualização de Arquivos
def create_page_files_details(page):

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    files = dict_profile["file"]

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        page.go("/files")

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    is_editable1 = dict_profile["permission"] != "adm"


    view_files = {
      
        "username": ft.TextField(label="Usuário", value=f"{files['username']}", width=300, color=ft.Colors.BLACK, read_only=True),  # usuario_field
        "date": ft.TextField(label="Data", value=f"{files['date']}", width=300, color=ft.Colors.BLACK, read_only=True),  # data_field
        "subproject": ft.TextField(label="Subprojeto", value=f"{files['subproject']}", width=300, color=ft.Colors.BLACK, read_only=True),  # subprojeto_field
        "type": ft.TextField(label="Tipo", value=f"{files['type']}", width=300, color=ft.Colors.BLACK, read_only=True),  # erros_field
        "average": ft.TextField(label="Média", value=f"{files['average']}", width=300, color=ft.Colors.BLACK, read_only=True),  # desconto_field
        "amount": ft.TextField(label="Montante", value=f"{files['amount']}", width=300, color=ft.Colors.BLACK, read_only=True),  # desconto_field
        "delay": ft.TextField(label="Atraso", value=f"{files['delay']}", width=300, color=ft.Colors.BLACK, read_only=True),  # desconto_field
        "url": ft.TextField(label="url", value=f"{files['url']}", width=300, color=ft.Colors.BLACK, read_only=True),  # advertencias_field

    }

    def delete_file(view_files):

        base = SupaBase(page=page)

        data_subproject = view_files.copy()

        data_subproject["username"] = view_files["username"].value
        data_subproject["date"] = view_files["date"].value

        ext = {"poligonos": "dwg", "fotos": "xlsx"}
        type = {"poligonos": "image/vnd.dwg", "fotos": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}
        
        date = (data_subproject["date"]).split("/")
        name_file = f'{view_files["username"].value}_{date[0]}{date[1]}{date[2]}.{ext[view_files["type"].value]}'
        response1 = base.delete_storage(local="files", object=f"{name_file}", type=type[view_files["type"].value])   
        response2 = base.delete_file_data(data_subproject)

        if response2.status_code in [200, 204]:
            page.go("/files")
            snack_bar = ft.SnackBar(content=ft.Text("Arquivo excluido"), bgcolor=ft.Colors.GREEN)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            page.go("/files")
            snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()


    btn_download = buttons.create_button(on_click=lambda e: page.launch_url(view_files["url"].value),
                                      text="Download",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,) 
    

    btn_delete = ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            col=7,
            controls=[
                    ft.Container(
                            alignment=ft.alignment.center,
                            col=7,
                            padding=5,
                            expand=True,
                            content=ft.ElevatedButton(
                                text="Excluir",
                                bgcolor=ft.Colors.RED,
                                color=ft.Colors.WHITE,
                                width=150,
                                on_long_press= lambda e: delete_file(view_files),
                            )
                        )
                    ]    
                 ) 
    
    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                *(view_files.values()),
                btn_download
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,  # Permite que a Column expanda com o conteúdo
        ),
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
                controls=[main_container, btn_delete],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    if dict_profile["permission"] != "adm":
        layout.controls[0].controls.remove(btn_delete)

    return layout
# Pagina De Visualização de Todas as Informações de Arquivos


def create_page_see_models(page):

    base = SupaBase(page=None)
    textthemes = TextTheme()
    dict_profile = page.client_storage.get("profile")
    filtros = dict_profile["models_filter"]
    texttheme1 = textthemes.create_text_theme1()

    buttons = Buttons(page)
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
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,) 
    btn_see_file = buttons.create_button(on_click=lambda e: go_url("/files"),
                                            text= "Arquivos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_deliverys = buttons.create_button(on_click=lambda e: go_url("/deliveries"),
                                            text= "Entregas",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_freelancers = buttons.create_button(on_click=lambda e: go_url("/freelancers"),
                                            text= "Freelancers",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_see_models = buttons.create_button(on_click=lambda e: go_url("/models"),
                                            text= "Modelos",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    btn_payment = buttons.create_button(on_click=lambda e: page.go("/payment"),
                                            text= "Financeiro",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)
    
    btn_projeto_user = buttons.create_button(on_click=lambda e: page.go("/project/user"),
                                      text= "Projeto",
                                      color=ft.Colors.GREY,
                                      col=12,
                                      padding=10,)



    btn_profile = buttons.create_button(on_click=lambda e:  page.go("/freelancers/token"),
                                            text= "Perfil",
                                            color=ft.Colors.GREY,
                                            col=12,
                                            padding=10,)

    drawer = ft.NavigationDrawer(
    controls=[
        btn_projeto,
        btn_projeto_user,
        btn_see_freelancers,
        btn_payment,
        btn_see_file,
        btn_see_deliverys,
        btn_see_models,
        btn_exit,
        ]
    )
    
    if dict_profile["permission"] != "adm":
        drawer.controls.remove(btn_projeto)  
        drawer.controls.remove(btn_see_freelancers) 
        drawer.controls.remove(btn_payment)
        drawer.controls.insert(0, btn_profile)

    page.drawer = drawer

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda e:page.open(page.drawer), icon_color=ft.Colors.BLACK),
    )

    if dict_profile["permission"] != "adm":
        project = ((base.get_one_project_data(dict_profile["current_project"])).json())[0]
        subprojects_list = (project["current_subprojects"]).split(",")
        get_json = (base.get_all_models_filter(subprojects_list)).json()
    else:
        get_json = (base.get_all_models()).json()
        subprojects_list = (base.get_all_subprojects()).json()

    dicio_projects = {}

    if dict_profile["permission"] != "adm":
        list_projects = [project]
    else:
        list_projects = (base.get_all_project_data()).json()

    for item in list_projects:

        dicio_projects[item["name_project"]] = (item["current_subprojects"]).split(",")

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
                        ft.DataColumn(ft.Text(value="Status", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
                        ft.DataColumn(ft.Text(value="Porcentagem", text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900, expand=True)),
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

    list_filtros = [None]

    # Preenche a lista com os dados das entregas
    for delev in get_json:

        project = next((k for k, v in dicio_projects.items() if delev['subproject'] in v), None)
        
        def go_token(delev):
            profile = page.client_storage.get("profile")
            profile.update({
                "model": { **delev, "dwg": delev.get("dwg") or "" },
                "models_filter": list_filtros
            })
            page.client_storage.set("profile", profile)
            page.go("/models/token")

        history_list.controls[0].content.rows.append(
            ft.DataRow(cells=[
                            ft.DataCell(ft.Text(
                                value=f"{delev['username']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['date']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['subproject']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                data=project
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['polygons']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{delev['status']}",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.Text(
                                value=f"{(int((int(delev['numbers']))/((int(delev['polygons']))/100)))}%",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.BLACK,
                                expand=True,
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            ft.DataCell(ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE,
                                expand=True,
                                on_click=lambda e, delev=delev: go_token(delev),
                                ),
                                on_long_press=lambda e, delev=delev: go_token(delev)
                                ),
                            
                        ]
                )
        )

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
    )


    filtros_ativos = {
    "dia": None,
    "mes": None,
    "ano": None,
    "usuario": None,
    "projeto": None,
    "subprojeto": None
    }

    # Função para filtrar a tabela
    def aplicar_filtros(update=True):
        for item in history_list.controls[0].content.rows:
            dia = ((item.cells[1].content.value).split("/"))[0]  
            mes = ((item.cells[1].content.value).split("/"))[1]  
            ano = ((item.cells[1].content.value).split("/"))[2]  
            usuario = item.cells[0].content.value
            project = item.cells[2].content.data  
            subproject = item.cells[2].content.value  

            # Verifica se o item atende a TODOS os filtros ativos
            item.visible = (
                (filtros_ativos["dia"] is None or filtros_ativos["dia"] == dia) and
                (filtros_ativos["mes"] is None or filtros_ativos["mes"] == mes) and
                (filtros_ativos["ano"] is None or filtros_ativos["ano"] == ano) and
                (filtros_ativos["projeto"] is None or filtros_ativos["projeto"] == project) and
                (filtros_ativos["subprojeto"] is None or filtros_ativos["subprojeto"] == subproject) and
                (filtros_ativos["usuario"] is None or filtros_ativos["usuario"] == usuario)
            )

        if update == True:
            history_list.update()  

        list_filtros[0] = filtros_ativos

    # Função chamada quando um Dropdown muda
    def on_dropdown_change(e, filtro):
        filtros_ativos[filtro] = e.control.value if e.control.value and e.control.value != "Nulo" else None
        aplicar_filtros()

    name_projects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in list_projects:
        name_projects.append(ft.dropdown.Option(item["name_project"], content=ft.Text(value=item["name_project"], color=ft.Colors.BLACK)))

    if dict_profile["permission"] != "adm":
        subprojects = (base.get_all_subprojects_filter(subprojects_list, type="poligonos")).json()
    else:
        subprojects = (base.get_all_subprojects()).json()
    name_subprojects = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in subprojects:
        name_subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    users = (base.get_est_user_data()).json()
    name_users = [ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK))]
    for item in users:
        name_users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    list_dropdown = ft.Row(
        controls=[
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Dia",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("14", content=ft.Text(value=f"14", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("21", content=ft.Text(value=f"21", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("28", content=ft.Text(value=f"28", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "dia"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Mês",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("01", content=ft.Text(value=f"01", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("02", content=ft.Text(value=f"02", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("03", content=ft.Text(value=f"03", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("04", content=ft.Text(value=f"04", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("05", content=ft.Text(value=f"05", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("06", content=ft.Text(value=f"06", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("07", content=ft.Text(value=f"07", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("08", content=ft.Text(value=f"08", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("09", content=ft.Text(value=f"09", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("10", content=ft.Text(value=f"10", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("11", content=ft.Text(value=f"11", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("12", content=ft.Text(value=f"12", color=ft.Colors.BLACK)),  
                ],
                on_change=lambda e: on_dropdown_change(e, "mes"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Ano",
                expand=True,
                options=[
                    ft.dropdown.Option("Nulo", content=ft.Text(value=f"Nulo", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2025", content=ft.Text(value=f"2025", color=ft.Colors.BLACK)),
                    ft.dropdown.Option("2026", content=ft.Text(value=f"2026", color=ft.Colors.BLACK)),
                ],
                on_change=lambda e: on_dropdown_change(e, "ano"),
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Usuário",
                expand=True,
                options=name_users,
                on_change= lambda e: on_dropdown_change(e, "usuario"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label="Projeto",
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                expand=True,
                options=name_projects,
                on_change=lambda e: on_dropdown_change(e, "projeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
            ft.Dropdown(
                text_style=ft.TextStyle(color=ft.Colors.BLACK),
                color=ft.Colors.BLACK,
                bgcolor=ft.Colors.WHITE,
                fill_color=ft.Colors.WHITE,
                filled=True,
                label_style=ft.TextStyle(color=ft.Colors.BLACK),
                label="Subprojeto",
                expand=True,
                options=name_subprojects,
                on_change=lambda e: on_dropdown_change(e, "subprojeto"),
                enable_filter=True,
                editable=True,
                width=250,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    if filtros[0] != None:
        
        list_dropdown.controls[0].value = filtros[0]["dia"]
        list_dropdown.controls[1].value = filtros[0]["mes"]
        list_dropdown.controls[2].value = filtros[0]["ano"]
        list_dropdown.controls[3].value = filtros[0]["usuario"]
        list_dropdown.controls[4].value = filtros[0]["projeto"]
        list_dropdown.controls[5].value = filtros[0]["subprojeto"]

        filtros_ativos = filtros[0]
        aplicar_filtros(update=False)

    def go_insert():
            profile = page.client_storage.get("profile")
            profile.update({
                "models_filter": list_filtros,
                "model_username": "",
                "model_date": "",
                "model_subproject": "",
                "model_polygons": "",
                "model_numbers": "",
                "model_status": "",
            })
            page.client_storage.set("profile", profile)
            page.go("/models/insert")

    # Container principal
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                controls=[
                    ft.Text("Modelos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda e: go_insert(),
                        bgcolor=ft.Colors.GREEN,
                        icon_color=ft.Colors.WHITE,
                    )
                ],  
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[4],
                        list_dropdown.controls[5],
                        list_dropdown.controls[3],
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        list_dropdown.controls[0],
                        list_dropdown.controls[1],
                        list_dropdown.controls[2],
                    ]
                ),
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
    layout = ft.Column(
        controls=[main_container],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    return layout

def create_page_models_details(page):

    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    model = dict_profile["model"]
    sp = SupaBase(page)

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        page.go("/models")

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )

    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]


    def editar_dados(view_deliveries):
        
        data_subproject = view_deliveries.copy()

        data_subproject["username"] = view_deliveries["username"].value
        data_subproject["date"] = view_deliveries["date"].value
        data_subproject["subproject"] = view_deliveries["subproject"].value
        data_subproject["polygons"] = view_deliveries["polygons"].value
        data_subproject["numbers"] = view_deliveries["numbers"].value
        data_subproject["status"] = view_deliveries["status"].value
        data_subproject["dwg"] = view_deliveries["dwg"].value
        

        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:

            if add_file[0] == True:

                response1 = sp.add_subproject_storage(file_selected[0], file_name[0], file_type[0], "models")

                if response1.status_code == 200 or response1.status_code == 201:
                    data_subproject[file_type[0]] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/models//{file_name[0]}"
                    response2 = sp.edit_model_data(data_subproject)

                    if response2.status_code in [200, 204]:
                        profile = page.client_storage.get("profile")
                        profile.update({
                            "model": data_subproject,
                        })
                        page.client_storage.set("profile", profile)
                        view_deliveries["dwg"].value = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/models//{file_name[0]}"
                        snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                    else:
                        snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response2.text}"), bgcolor=ft.Colors.RED)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao enviar imagem: {response1.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                response2 = sp.edit_model_data(data_subproject)

                if response2.status_code in [200, 204]:
                    profile = page.client_storage.get("profile")
                    profile.update({
                        "model": data_subproject,
                    })
                    page.client_storage.set("profile", profile)
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar dados: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()


    # Campos para exibir os detalhes da entrega
    
    is_editable1 = dict_profile["permission"] != "adm"

    users = []
    get_users = (sp.get_all_user_data()).json()
    for item in get_users:
        users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    dropdow1 = ft.Dropdown(
        options=users,
        value=model['username'],
        label="Usuário",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=True,
        )
    
    subprojects = []
    get_subprojects = (sp.get_all_subprojects()).json()
    for item in get_subprojects:
        subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    dropdow2 = ft.Dropdown(
        options=subprojects,
        value=model['subproject'],
        label="Subprojeto",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=True,
        )
    
    next_month = datetime.now().month + 1
    year1 = datetime.now().year
    if next_month == 13:
        next_month = 1
        year1 += 1

    before_month = datetime.now().month - 1
    year2 = datetime.now().year
    if before_month == 0:
        before_month = 12
        year2 -= 1

    dropdow4 = ft.Dropdown(
        value=model["date"],
        label="Data",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"28/{before_month:02d}/{year2:02d}",
                                content=ft.Text(value=f"28/{before_month:02d}/{year2:02d}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{next_month:02d}/{year1:02d}",
                                content=ft.Text(value=f"07/{next_month:02d}/{year1:02d}",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,
        disabled=True,
        )

    dropdow5 = ft.Dropdown(
        value=model["status"],
        label="Status",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"Completo",
                                content=ft.Text(value=f"Completo",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"Incompleto",
                                content=ft.Text(value=f"Incompleto",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,

        )

    def go_download(view_deliveries, object):
        if view_deliveries[object].value != "." and view_deliveries[object].value != "":
            page.launch_url(view_deliveries[object].value)

    view_deliveries = {
        "username": dropdow1, 
        "date":dropdow4, 
        "subproject":dropdow2, 
        "polygons":ft.TextField(label="Polígonos", value=f"{model['polygons']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "numbers":ft.TextField(label="Numeros", value=f"{model['numbers']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=is_editable1), 
        "status":dropdow5,
        "dwg":ft.TextField(label="DWG", value=f"{model['dwg']}", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True), 
    }

    def on_file_selected():

        date = (view_deliveries["date"].value).split("/")

        name_file = f'{view_deliveries["username"].value}_{view_deliveries["subproject"].value}_{date[0]}{date[1]}{date[2]}.{file_type[0]}'
        file_name.clear()
        file_name.append(name_file)

        view_deliveries["dwg"].value = file_old_name[0]

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

    def delete_delivery(view_deliveries):

            base = SupaBase(page=page)

            data_subproject = view_deliveries.copy()

            data_subproject["username"] = view_deliveries["username"].value
            data_subproject["date"] = view_deliveries["date"].value
            data_subproject["subproject"] = view_deliveries["subproject"].value


            date = (data_subproject["date"]).split("/")
            name_file = f'{view_deliveries["username"].value}_{view_deliveries["subproject"].value}_{date[0]}{date[1]}{date[2]}.dwg'
            response1 = base.delete_storage(local="models", object=f"{name_file}", type="image/vnd.dwg")   
            if response1.status_code in[200, 204]:
                response2 = base.delete_model(data_subproject)
                if response2.status_code in [200, 204]:
                    page.go("/models")
                    snack_bar = ft.SnackBar(content=ft.Text("Modelo excluido"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    page.go("/models")
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()


    def delete_file(view_deliveries):

            base = SupaBase(page=page)

            data_subproject = view_deliveries.copy()

            data_subproject["username"] = view_deliveries["username"].value
            data_subproject["date"] = view_deliveries["date"].value
            data_subproject["subproject"] = view_deliveries["subproject"].value
            data_subproject["polygons"] = view_deliveries["polygons"].value
            data_subproject["numbers"] = view_deliveries["numbers"].value


            date = (data_subproject["date"]).split("/")
            name_file = f'{view_deliveries["username"].value}_{view_deliveries["subproject"].value}_{date[0]}{date[1]}{date[2]}.dwg'
            response1 = base.delete_storage(local="models", object=f"{name_file}", type="image/vnd.dwg")
            if response1.status_code in [200, 204]:

                data_dwg = {
                    "dwg":".",
                    "username": data_subproject["username"],
                    "date": data_subproject["date"], 
                    "subproject": data_subproject["subproject"],
                    "polygons": data_subproject["polygons"],
                    "numbers": data_subproject["numbers"],
                    }


                response2 = sp.edit_model_data(data_dwg)
                if response2.status_code in [200, 204]:
                        profile = page.client_storage.get("profile")
                        profile.update({
                            "model": data_dwg,
                        })
                        page.client_storage.set("profile", profile)
                        view_deliveries["dwg"].value = "."
                        snack_bar = ft.SnackBar(content=ft.Text("Arquivo excluido"), bgcolor=ft.Colors.GREEN)
                        page.overlay.append(snack_bar)
                        snack_bar.open = True
                        page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao editar tabela: {response2.text}"), bgcolor=ft.Colors.RED)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Falha ao excluir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()

    btn_download = buttons.create_button(on_click=lambda e: page.launch_url(model["dwg"]),
                                      text="Download",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,) 

    btn_edit = buttons.create_button(on_click=lambda e: editar_dados(view_deliveries),
                                      text="Salvar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,) 
    
    btn_delete=ft.Column(
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    col=7,
                    controls=[
                            ft.Container(
                                    alignment=ft.alignment.center,
                                    col=7,
                                    padding=5,
                                    expand=True,
                                    content=ft.ElevatedButton(
                                        text="Excluir",
                                        bgcolor=ft.Colors.RED,
                                        color=ft.Colors.WHITE,
                                        width=150,
                                        on_long_press= lambda e: delete_delivery(view_deliveries),
                                    )
                                )
                            ]    
                        ) 
    
    view_column = ft.Column(
        controls=[
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    for item in view_deliveries.items():
        
        if item[0] == "dwg" and dict_profile["permission"] == "adm":
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD,
                        bgcolor=ft.Colors.BLUE,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: open_gallery(e, type="dwg"),
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: delete_file(view_deliveries),
                        ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))
        else:
            view_column.controls.append(ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                    item[1],
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.WHITE,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ))


    main_container = ft.Container(
        content=ft.Column(
            controls=[
                view_column
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
        alignment=ft.alignment.top_center,  # Alinhamento no topo para melhor distribuição
        margin=10,
        expand=True  # Permite que o Container expanda verticalmente
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"sm": 12, "md": 8, "lg": 6},
                controls=[main_container, btn_download, btn_edit, btn_delete],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    if dict_profile["permission"] != "adm":
        layout.controls[0].controls.remove(btn_delete)
        layout.controls[0].controls.remove(btn_edit)

    return layout

def create_page_new_model(page):

    loading = LoadingPages(page=page)
    buttons = Buttons(page)
    dict_profile = page.client_storage.get("profile")
    sp = SupaBase(page)

    # Definir o tema global para garantir que o texto seja preto por padrão

    def go_back():
        page.go("/models")

    # AppBar
    page.appbar = ft.AppBar(
        leading_width=40,
        center_title=True,
        title=ft.Text("Atta'm Engenharia e Aerolevantamento"),
        bgcolor=ft.Colors.WHITE70,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN, on_click=lambda e: go_back(), icon_color=ft.Colors.BLACK),
        ],
    )


    file_selected = []
    file_name = []
    file_type =[]
    file_old_name = []
    add_file = [False]


    def editar_dados(view_deliveries):
        
        data_subproject = view_deliveries.copy()

        data_subproject["id"] = str(sp.get_model_id())
        data_subproject["username"] = view_deliveries["username"].value
        data_subproject["date"] = view_deliveries["date"].value
        data_subproject["subproject"] = view_deliveries["subproject"].value
        data_subproject["polygons"] = view_deliveries["polygons"].value
        data_subproject["numbers"] = view_deliveries["numbers"].value
        data_subproject["status"] = view_deliveries["status"].value
        data_subproject["dwg"] = view_deliveries["dwg"].value
        

        if any(field == "" or field is None for field in data_subproject.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        
        if data_subproject["dwg"] == ".":
            snack_bar = ft.SnackBar(content=ft.Text("Insira um arquivo para fazer o envio"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        
        check = (sp.get_one_model_data(data_subproject["date"], data_subproject["subproject"])).json()

        if len (check) > 0:
            snack_bar = ft.SnackBar(content=ft.Text("Modelo especificado já cadastrado !!!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        
        check2 = (sp.get_one_delivery_data(data_subproject["date"], data_subproject["subproject"])).json()

        if len (check2) < 1:
            snack_bar = ft.SnackBar(content=ft.Text("Nenhuma entrega encontrada na data especificada !!!"), bgcolor=ft.Colors.YELLOW)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return
        

        if add_file[0] == True:

            response1 = sp.add_subproject_storage(file_selected[0], file_name[0], file_type[0], "models")

            if response1.status_code == 200 or response1.status_code == 201:
                data_subproject[file_type[0]] = f"https://kowtaxtvpawukwzeyoif.supabase.co/storage/v1/object/public/models//{file_name[0]}"
                response2 = sp.post_to_models_data(data_subproject)

                if response2.status_code in [200, 201]:
                    page.go("/models")
                    snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
                else:
                    snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir tabela: {response2.text}"), bgcolor=ft.Colors.AMBER)
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir arquivo: {response1.text}"), bgcolor=ft.Colors.RED)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        else:
            response2 = sp.post_to_models_data(data_subproject)

            if response2.status_code in [200, 204]:
                page.go("/models")
                snack_bar = ft.SnackBar(content=ft.Text("Dados atualizados com sucesso"), bgcolor=ft.Colors.GREEN)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            else:
                snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao inserir tabela: {response2.text}"), bgcolor=ft.Colors.AMBER)
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()


    # Campos para exibir os detalhes da entrega
    
    users = []
    if dict_profile["permission"] != "adm":
        get_users = (sp.get_all_user_data_filter_project(dict_profile["current_project"])).json()
    else:
        get_users = (sp.get_all_user_data_filter_est()).json()
    for item in get_users:
        users.append(ft.dropdown.Option(item["username"], content=ft.Text(value=item["username"], color=ft.Colors.BLACK)))

    dropdow1 = ft.Dropdown(
        value=dict_profile["username"],
        options=users,
        label="Usuário",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        disabled=dict_profile["permission"] == "est",
        )
    
    if dict_profile["permission"] != "adm":
        project = ((sp.get_one_project_data(dict_profile["current_project"])).json())[0]
        subprojects_list = (project["current_subprojects"]).split(",")
        get_subprojects = (sp.get_all_subprojects_filter(subprojects_list, "poligonos")).json()
    else:
        get_subprojects = (sp.get_all_subprojects()).json()

    subprojects = []
    for item in get_subprojects:
        subprojects.append(ft.dropdown.Option(item["name_subproject"], content=ft.Text(value=item["name_subproject"], color=ft.Colors.BLACK)))

    dropdow2 = ft.Dropdown(
        options=subprojects,
        label="SubProjeto",
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        enable_filter=True,
        editable=True,
        )
    
    next_month = datetime.now().month + 1
    year1 = datetime.now().year
    if next_month == 13:
        next_month = 1
        year1 += 1

    before_month = datetime.now().month - 1
    year2 = datetime.now().year
    if before_month == 0:
        before_month = 12
        year2 -= 1

    dropdow4 = ft.Dropdown(
        label="Data",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"21/{before_month:02d}/{year2:02d}",
                                content=ft.Text(value=f"21/{before_month:02d}/{year2:02d}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"28/{before_month:02d}/{year2:02d}",
                                content=ft.Text(value=f"28/{before_month:02d}/{year2:02d}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"07/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"14/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"21/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                content=ft.Text(value=f"28/{datetime.now().strftime("%m")}/{datetime.now().year}",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"07/{next_month:02d}/{year1:02d}",
                                content=ft.Text(value=f"07/{next_month:02d}/{year1:02d}",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,

        )

    dropdow5 = ft.Dropdown(
        label="Status",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        options=[
            ft.dropdown.Option(f"Completo",
                                content=ft.Text(value=f"Completo",
                                                color=ft.Colors.BLACK)),
            ft.dropdown.Option(f"Incompleto",
                                content=ft.Text(value=f"Incompleto",
                                                color=ft.Colors.BLACK)),
        ],
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        filled=True,
        width=300,

        )

    dropdow1.value = dict_profile.get("model_username", "")
    dropdow4.value = dict_profile.get("model_date", "")
    dropdow2.value = dict_profile.get("model_subproject", "")

    view_deliveries = {
        "username": dropdow1, 
        "date": dropdow4, 
        "subproject":dropdow2,   
        "polygons":ft.TextField(label="Polígonos", value=dict_profile["model_polygons"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), keyboard_type=ft.KeyboardType.NUMBER), 
        "numbers":ft.TextField(label="Numeros", value=dict_profile["model_numbers"], width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), keyboard_type=ft.KeyboardType.NUMBER), 
        "status":dropdow5,
        "dwg":ft.TextField(label="DWG", value=f".", width=300, text_style=ft.TextStyle(color=ft.Colors.BLACK), read_only=True), 
    }

    def on_keyboard(e: ft.KeyboardEvent):
        profile = page.client_storage.get("profile")
        profile.update({
            "model_username": dropdow1.value,
            "model_date": dropdow4.value,
            "model_subproject": dropdow2.value,
            "model_polygons": view_deliveries["polygons"].value,
            "model_numbers": view_deliveries["numbers"].value,  
            "model_status": view_deliveries["status"].value,  
        })
        page.client_storage.set("profile", profile)

    page.on_keyboard_event = on_keyboard

    def on_file_selected():

        date = (view_deliveries["date"].value).split("/")

        name_file = f'{view_deliveries["username"].value}_{view_deliveries["subproject"].value}_{date[0]}{date[1]}{date[2]}.{file_type[0]}'
        file_name.clear()
        file_name.append(name_file)

        view_deliveries["dwg"].value = file_old_name[0]

        add_file[0] = True

        page.update()

    def get_uploaded_file_bytes(e: ft.FilePickerUploadEvent):

        dropdow1.disabled = True
        dropdow2.disabled = True
        dropdow4.disabled = True

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

    def open_gallery(e, type, view_deliveries):

        copy = view_deliveries.copy()

        del copy["dwg"]

        if any(field.value == "" or field.value is None for field in copy.values()):
            snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=ft.Colors.RED)
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            return

        fp.pick_files(              
            allow_multiple=False,
        )

        file_type.clear()
        file_type.append(type)

    def remove_dwg(e):

        view_deliveries["dwg"].value=""

        file_selected.clear()
        file_name.clear()
        file_type.clear()
        file_old_name.clear()
        add_file[0] = False

        dropdow1.disabled = False
        dropdow2.disabled = False
        dropdow4.disabled = False


        page.update()


    botao_edit = buttons.create_button(on_click=lambda e: editar_dados(view_deliveries),
                                      text="Enviar",
                                      color=ft.Colors.BLUE,
                                      col=7,
                                      padding=5,)
     
    btn_dwg = buttons.create_button(on_click=lambda e: open_gallery(
                                                                e,
                                                                type="dwg",
                                                                view_deliveries=view_deliveries
                                                                ),
                                      text="Upload DWG",
                                      color=ft.Colors.AMBER,
                                      col=7,
                                      padding=5,) 
    
    btn_remove_dwg = buttons.create_button(on_click=lambda e: remove_dwg(e),
                                      text="Remover DWG",
                                      color=ft.Colors.RED,
                                      col=7,
                                      padding=5,) 
    
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                *(view_deliveries.values()),
                btn_dwg,
                btn_remove_dwg
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
        alignment=ft.alignment.top_center,  # Alinhamento no topo para melhor distribuição
        margin=10,
        expand=True  # Permite que o Container expanda verticalmente
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





















































































































