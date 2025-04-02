import flet as ft
import requests
import flet.map as map
from datetime import datetime
from collections import defaultdict
from datetime import datetime



class Poste:

    def __init__(self, number, ip, situacao, tipo, pontos, bairro, logradouro, lat, long):
        self.number = number
        self.ip = ip
        self.situacao = situacao
        self.tipo = tipo
        self.pontos = pontos
        self.bairro = bairro
        self.logradouro = logradouro
        self.lat = lat
        self.long = long


class TextTheme:

    def __init__(self):
        None

    def create_text_theme1(self):
        
        return ft.Theme(
        text_theme=ft.TextTheme(
            title_large=ft.TextStyle(
                size=15,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_900,
            ),
            title_medium=ft.TextStyle(
                size=15,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_400,
            ),
            title_small=ft.TextStyle(
                size=12,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_400,
            ),
            )
        )


class Buttons:
    
    def __init__(self, page):
        self.page = page
    
    # Método base para criar os botões
    def create_button(self, on_click, text, color, col, padding, width=150):
        return ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            col=col,
            controls=[
                    ft.Container(
                            alignment=ft.alignment.center,
                            col=col,
                            padding=padding,
                            expand=True,
                            content=ft.ElevatedButton(
                                text=text,
                                bgcolor=color,
                                color=ft.Colors.WHITE,
                                on_click=on_click,
                                width=width,
                            )
                        )
                    ]    
                 )

    
    def create_call_location_button(self, icon, on_click, color, col, padding, icon_color=ft.Colors.RED):
        return ft.Column(
            col=col,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                    ft.Container(
                            alignment=ft.alignment.center,
                            col=col,
                            width=50,
                            height=50,
                            border_radius=ft.border_radius.all(25),
                            padding=padding,
                            bgcolor=color,
                            content=ft.IconButton(
                                icon=icon,
                                icon_color=icon_color,
                                on_click=on_click,
                            )
                        )
                    ]    
                 )

    def create_icon_button(self, icon, on_click, color, col, padding, icon_color):
        return ft.Column(
            col=col,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                    ft.Container(
                            alignment=ft.alignment.center,
                            col=col,
                            width=40,
                            height=40,
                            border_radius=ft.border_radius.all(20),
                            padding=padding,
                            bgcolor=color,
                            content=ft.IconButton(
                                icon=icon,
                                icon_color=icon_color,
                                on_click=on_click,
                            )
                        )
                    ]    
                 )
    
          
    
    def create_point_button_post(self, on_click, text, color, size, visible):
        
        return ft.Container(
            width=size,
            height=size,
            bgcolor=color,
            on_click=on_click,
            border_radius=((int(size))/2)
            )
    
    def create_point_button_tree(self, on_click, text, color, size, visible):
        
        new_size = size + 5

        return ft.Container(
            on_click=on_click,
            content=ft.Icon(
                name=ft.Icons.PARK_SHARP,
                color=color,
                size=new_size
            ),
            )
    
    def create_point_button_grass(self, on_click, text, color, size, visible):
        
        new_size = size + 5

        return ft.Container(
            on_click=on_click,
            content=ft.Icon(
                name=ft.Icons.GRASS,
                color=color,
                size=new_size
            ),
            )
        
          
    
    def create_location_button(self):
        return ft.Column(
                spacing=0,
                controls=[
                    ft.ElevatedButton(
                        on_click=None,
                        width=20,
                        height=20,
                        bgcolor=ft.Colors.BLUE,
                        text="",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                ]
            )
    
    def create_point_marker(self, content, x, y, data):
        return map.Marker(
                content=content,
                coordinates=map.MapLatitudeLongitude(x, y),
                rotate=True,
                data=data, 
                )
    

class Web_Image:

    def __init__(self, page):
        self.page = page

    def get_image_url(self, name):
        SUPABASE_URL = "https://kowtaxtvpawukwzeyoif.supabase.co"
        SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtvd3RheHR2cGF3dWt3emV5b2lmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk0NzIyODQsImV4cCI6MjA1NTA0ODI4NH0.DWq3PkIZaLS6qq-tLu6vmFI4ESiXuof7477izTfsR9k"
        TABLE_NAME = "assets_geopostes"
        COLUMN_NAME = name

        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
        
        # Faz a requisição GET para buscar pela coluna 'nome'
        response = requests.get(f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}?nome=eq.{COLUMN_NAME}", headers=headers)
        
        if response.status_code == 200 and response.json():
            # Pegando a URL da imagem a partir da coluna 'imagem_url'
            image_url = response.json()[0]["imagem_url"]
            return image_url
        else:
            print("Erro ao buscar a imagem.")
            return None
        
    def create_web_image(self, src):

        return ft.Image(src=src, repeat=None)


class CallText:

    def __init__(self, page):
        self.page = page

    
    def create_calltext(self, text, color, size, font, col, padding, visible):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        return  ft.Container(
            visible=visible,
            col=col,
            padding=padding,
            content=ft.Text(
                value=text,
                text_align=ft.TextAlign.CENTER,
                size=size,
                color=color,
                weight=font,
            ),
            theme=texttheme1,
        )
    
    def create_container_calltext1(self):

        buttons = Buttons(self.page)
        btn_null = buttons.create_point_button(on_click=None, text=None)
        btn_null.controls[1].visible = False

        return  ft.Column(
                col=12,
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[ ft.Container(
                            visible=True,
                            padding=10,
                            col=7,
                            bgcolor=ft.Colors.BLUE_900,
                            border_radius=10,
                            content=ft.Column(    
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                            controls=[
                            ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True,    
                            controls=[  
                            ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value="No mapa acima, clique em um",
                                    color=ft.Colors.WHITE,
                                    size=15,
                                    weight=ft.FontWeight.W_600,
                                    font_family="Tahoma",
                                    ),]),
                            ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,      
                            controls=[  
                            ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value="Ponto de poste:",
                                    color=ft.Colors.WHITE,
                                    size=15,
                                    weight=ft.FontWeight.W_600,
                                    font_family="Tahoma",
                                    ),btn_null]),

                                    ])
                        )
                        ]
                        )
    
    def create_container_calltext2(self, text):

        return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ ft.Container(
                    visible=True,
                    padding=10,
                    col=12,
                    bgcolor=ft.Colors.BLUE_700,
                    border_radius=10,
                    content= ft.Text(
                            value=text,
                            color=ft.Colors.WHITE,
                            size=40,
                            weight=ft.FontWeight.W_600,
                            font_family="Tahoma",
                            ),)
                ]
                )
        

class CheckBox:

    def __init__(self, page):
        self.page = page


    def create_checkbox(self, text, size, on_change, col, data=None, value=False):

        return ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.START,
            col=col,
            controls=[
                ft.Checkbox(
                    value=value,
                    label=text,
                    data = data,
                    on_change=on_change,
                    label_style=ft.TextStyle(
                        color=ft.Colors.BLACK,
                        size=size,    
                        )
                    )
            ]
        )

    def create_checkbox2(self, text, size, on_change, col, data=None, value=False):

        return ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.START,
            col=col,
            controls=[
                ft.Checkbox(
                    value=value,
                    label=text,
                    data = data,
                    on_change=on_change,
                    label_style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=size,    
                        )
                    )
            ]
        )


class TextField:

    def __init__(self, page):
        self.page = page


    def create_textfield(self,value, text, password, read=False, input_filter=None, keyboard_type=None, multiline=False):

        return  ft.TextField(
            value=value,
            label= text,
            password=password,
            multiline=multiline,
            label_style= ft.TextStyle(color=ft.Colors.BLACK, size=12),
            text_style= ft.TextStyle(color=ft.Colors.BLACK, size=12),
            col=8,
            read_only=read,
            input_filter=input_filter,
            keyboard_type=keyboard_type
            )
    
    def create_textfield2(self,value, text, password, read=False, input_filter=None, keyboard_type=None, multiline=False, reveal_password=False):

        return ft.Column(
                    [
                        ft.TextField(
                            value=value,
                            label=text,
                            password=password,
                            can_reveal_password=reveal_password,
                            multiline=multiline,
                            label_style=ft.TextStyle(color=ft.Colors.BLACK, size=15),
                            text_style=ft.TextStyle(color=ft.Colors.BLACK, size=15),
                            width=370,  
                            read_only=read,
                            input_filter=input_filter,
                            keyboard_type=keyboard_type,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=400,  
                )
    
    def create_description_textfield(self, text):

        return  ft.Column(
                controls=[
                    ft.Container(
                        col=12,
                        alignment=ft.alignment.center,
                        content=ft.TextField(
                            label=text,
                            text_align=ft.TextAlign.CENTER,
                            min_lines=3,
                            label_style=ft.TextStyle(size=20),
                            text_style=ft.TextStyle(color=ft.Colors.BLACK),
                            )
                        )
                    ]
                )


class SettingsMenu:

    def __init__(self, page):
        self.page = page


    def itens_settings_menu(self, text, color, action):

        return ft.PopupMenuItem(
                on_click=action,
                content=(
                    ft.Text(value=text, color=color)
                ))

    def create_settings_menu(self, color, col, action):

        return ft.Column(
                col=col,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=50,
                        height=50,
                        alignment=ft.alignment.center,
                        bgcolor=color,
                        border_radius=ft.border_radius.all(25),
                        padding=0,
                        content=(
                            ft.IconButton(
                                icon=ft.Icons.MENU,
                                icon_color=ft.Colors.BLUE,
                                bgcolor=ft.Colors.WHITE,
                                on_click=action,
                            )
                        )
                    )
                ]
            )    


class Forms:

    def __init__(self, page):
        self.page = page

    def create_forms_post(self, dict_forms, string1, string2, alignment):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        itens_forms = []

        for n in range(len(dict_forms)):
            key = list(dict_forms.keys())[n]
            value = list(dict_forms.values())[n]

            itens_forms.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(value=key, size=15, color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text(value=value.value, size=15, color=ft.Colors.BLACK)),
                
            ]))

        objects = Objects(page=None)
        method_map = objects.form_object1()

        return ft.Column([
                    ft.Container(
                        padding=0,
                        col=12,
                        theme=texttheme1,  
                        content=ft.DataTable(
                            data_row_max_height=55,
                            column_spacing=30,
                            columns=[
                                ft.DataColumn(ft.Text(value=string1, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                                ft.DataColumn(ft.Text(value=string2, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK, weight=ft.FontWeight.W_900)),  
                            ],
                            rows= itens_forms,
                        ),
                    )
                    ],
                    alignment=alignment,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    )
    
    def create_user_form(self, list_user_form):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        return ft.Column([
                    ft.Container(
                            padding=0,
                            col=12,
                            theme=texttheme1,  
                            content=ft.DataTable(
                                data_row_max_height=50,
                                column_spacing=10,
                                columns=[
                                    ft.DataColumn(ft.Text(value="")),  
                                    ft.DataColumn(ft.Text(value="")),  
                                ],
                                rows=[
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="ID", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM), width=200)
                                        )
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="Usuário", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM), width=200)
                                        )
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="E-mail", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[2], theme_style=ft.TextThemeStyle.TITLE_SMALL), width=200)
                                        )
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="Numero", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM), width=200)
                                        )
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="Senha", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM), width=200)
                                        )
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text(value="Permissão", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                        ft.DataCell(
                                            ft.Container(content=ft.Text(value=list_user_form[5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM), width=200)
                                        )
                                    ]),
                                ],
                            ),
                        )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        height=400,
                        width=440,  
                        expand=True,
                        )
    
    def create_os_forms(self, dict_forms, object):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        itens_forms = []

        for n in range(len(dict_forms)):
            key = list(dict_forms.keys())[n]
            value = list(dict_forms.values())[n]

            itens_forms.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(value=key, theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                ft.DataCell(
                    ft.Container(content=value, width=200)  
                )
            ]))

        objects = Objects(page=None)
        method_map = objects.form_object2()

        return ft.Column([
                    ft.Container(
                            padding=0,
                            col=12,
                            theme=texttheme1,  
                            content=ft.DataTable(
                                data_row_max_height=60,
                                column_spacing=10,
                                columns=[
                                    ft.DataColumn(ft.Text(value="Ordem de", theme_style=ft.TextThemeStyle.TITLE_LARGE)),  
                                    ft.DataColumn(ft.Text(value=method_map[object], theme_style=ft.TextThemeStyle.TITLE_LARGE)),  
                                ],
                                rows=itens_forms,
                            ),
                        )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        height=900,
                        width=440,  
                        expand=True,
                        )


    def create_add_forms(self, dict_forms):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        itens_forms = []

        for n in range(len(dict_forms)):
            key = list(dict_forms.keys())[n]
            value = list(dict_forms.values())[n]

            itens_forms.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(value=key, theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                ft.DataCell(
                    ft.Container(content=value, width=200)  
                )
            ]))


        return ft.Column([
                    ft.Container(
                        padding=0,
                        col=12,
                        theme=texttheme1,
                        content=ft.DataTable(
                            data_row_max_height=60,
                            column_spacing=10,
                            columns=[
                                ft.DataColumn(ft.Text(value="")),  
                                ft.DataColumn(ft.Text(value="")),  
                            ],
                            rows=itens_forms,
                        ),
                    )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    height=470,
                    expand=True,
                    )
    
    def create_add_os_forms(self, dict_forms):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()

        itens_forms = []

        for n in range(len(dict_forms)):
            key = list(dict_forms.keys())[n]
            value = list(dict_forms.values())[n]

            itens_forms.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(value=key, theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                ft.DataCell(
                    ft.Container(content=value, width=200)  
                )
            ]))

        return ft.Column([
                    ft.Container(
                            padding=0,
                            col=12,
                            theme=texttheme1,
                            content=ft.DataTable(
                                data_row_max_height=60,
                                column_spacing=10,
                                columns=[
                                    ft.DataColumn(ft.Text(value="")),  
                                    ft.DataColumn(ft.Text(value="")), 
                                ],
                                rows=itens_forms,
                            ),
                        )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        height=900,
                        width=440,  
                        expand=True,
                        )
    
    def create_add_user_forms(self, list_user_forms, new=False):

        textthemes = TextTheme()
        texttheme1 = textthemes.create_text_theme1()
        textfields = TextField(self.page)

        user_name_field = textfields.create_textfield(value=list_user_forms[0], text=None, password=False)
        user_email_field = textfields.create_textfield(value=list_user_forms[1], text=None, password=False, read=True)
        if new == True:
            user_email_field = textfields.create_textfield(value=list_user_forms[1], text=None, password=False, read=False)
        user_phone_field = textfields.create_textfield(value=list_user_forms[2], text=None, password=False)
        user_password_field = textfields.create_textfield(value=list_user_forms[3], text=None, password=False)
        user_permission_field = textfields.create_textfield(value=list_user_forms[4], text=None, password=False)

        def drop_down_menu(value=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None):
            list = [opt1, opt2, opt3, opt4, opt5, opt6]
            list_option = []
            for opt in list:
                if opt != None:
                    list_option.append(ft.dropdown.Option(opt))

            menu = ft.Dropdown(
                options=list_option,
                value=value,
                label_style=ft.TextStyle(color=ft.Colors.BLACK, size=12),
                bgcolor=ft.Colors.WHITE,
                options_fill_horizontally=True,
                text_style= ft.TextStyle(size=12, color=ft.Colors.BLACK)
            )
            return menu
       
        return ft.Column([
                    ft.Container(
                        padding=0,
                        col=12,
                        theme=texttheme1,
                        content=ft.DataTable(
                            data_row_max_height=60,
                            column_spacing=10,
                            columns=[
                                ft.DataColumn(ft.Text(value="")),  
                                ft.DataColumn(ft.Text(value="")), 
                            ],
                            rows=[
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(value="Usuário", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                    ft.DataCell(
                                        ft.Container(content=user_name_field, width=200)  
                                    )
                                ]),
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(value="E-mail", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                    ft.DataCell(
                                        ft.Container(content=user_email_field, width=200)  
                                    )
                                ]),
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(value="Numero", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                    ft.DataCell(
                                        ft.Container(content=user_phone_field, width=200)
                                    )
                                ]),
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(value="Senha", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                    ft.DataCell(
                                        ft.Container(content=user_password_field, width=200)
                                    )
                                ]),
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(value="Permissão", theme_style=ft.TextThemeStyle.TITLE_LARGE)),
                                    ft.DataCell(
                                        ft.Container(content=drop_down_menu(list_user_forms[4], "adm", "convidado"), width=200)
                                    )
                                ]),
                            
                            ],
                        ),
                    )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    height=400,
                    width=440,  
                    expand=True,
                    )


class LoadingPages:

    def __init__(self, page):
        self.page = page

    def new_loading_page(self, page, call_layout, text="Carregando", route ="/"):

        page.floating_action_button = None
        page.bottom_appbar = None
        page.appbar = None
        page.clean()
        page.controls.clear()
        page.overlay.clear()

        loading_text = ft.Column(
                            controls=[
                                ft.Container(
                                    visible=True,
                                    alignment=ft.alignment.center,
                                    expand=True,
                                    height=960,
                                    col=12,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,  
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value=text,
                                                text_align=ft.TextAlign.CENTER,
                                                size=30,
                                                color=ft.Colors.BLACK,
                                                weight=ft.FontWeight.W_400,
                                            ),
                                            ft.ProgressRing(color=ft.Colors.BLACK)
                                        ])
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                        )

        page.add(loading_text)
        page.update()

        layout = call_layout()

        page.add(layout)

        page.scroll_to(1)

        if loading_text in page.controls:
            page.remove(loading_text)
        
        page.update()
        page.go(route)

    def new_loading_overlay_page(self, page, call_layout, text="Carregando"):

        overlay_copy = list(page.overlay)
        for item in overlay_copy:
            if item.data == "geolocator":
                pass
            else:
                page.overlay.remove(item)
            
        loading_text = ft.Row([
                        ft.Container(
                            bgcolor=ft.Colors.WHITE,
                            padding=10,
                            margin=10,
                            height=700,
                            width=370,
                            border_radius=20,
                            col=12,
                            content= ft.Column(
                                        controls=[
                                            ft.Container(
                                            visible=True,
                                            alignment=ft.alignment.center,
                                            expand=True,
                                            height=700,
                                            col=12,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,  
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        value=text,
                                                        text_align=ft.TextAlign.CENTER,
                                                        size=30,
                                                        color=ft.Colors.BLACK,
                                                        weight=ft.FontWeight.W_400,
                                                    ),
                                                    ft.ProgressRing(color=ft.Colors.BLACK)
                                                ])
                                        ),
                                        ],
                                        scroll=ft.ScrollMode.AUTO,  
                                        expand=True,
                            ), 
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    alignment=ft.MainAxisAlignment.CENTER,
                    )

        page.overlay.append(loading_text)
        page.update()

        overlay_layout = call_layout()

        def go_back():
            
            overlay_copy = list(page.overlay)
            for item in overlay_copy:
                if item.data == "geolocator":
                        pass
                else:
                    page.overlay.remove(item)
            page.update()


        close_button = ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            alignment=ft.alignment.center,
                            on_click=lambda e: go_back(),
                        )],
                        alignment=ft.MainAxisAlignment.CENTER,
                        col=12,
                        expand=True
        )

        container_overlay_layout = ft.Row([
                ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=10,
                    margin=10,
                    height=700,
                    width=370,
                    border_radius=20,
                    col=12,
                    content= ft.Column(
                                controls=[close_button, overlay_layout],
                                scroll=ft.ScrollMode.AUTO,  
                                expand=True,
                    ), 
                )
            ],
            vertical_alignment=ft.CrossAxisAlignment.END,
            alignment=ft.MainAxisAlignment.CENTER,
            )

        page.overlay.insert(1,container_overlay_layout)

        if loading_text in page.overlay:
            page.overlay.remove(loading_text)
        
        page.update()

    
    def add_loading_overlay_page(self, page, call_layout, current_container, text="Carregando"):

        current_container.controls[0].content.controls.clear() 

        loading_text = ft.Row([
                        ft.Container(
                            bgcolor=ft.Colors.WHITE,
                            padding=10,
                            margin=10,
                            height=700,
                            width=370,
                            border_radius=20,
                            col=12,
                            content= ft.Column(
                                        controls=[
                                            ft.Container(
                                            visible=True,
                                            alignment=ft.alignment.center,
                                            expand=True,
                                            height=700,
                                            col=12,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,  
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        value=text,
                                                        text_align=ft.TextAlign.CENTER,
                                                        size=30,
                                                        color=ft.Colors.BLACK,
                                                        weight=ft.FontWeight.W_400,
                                                    ),
                                                    ft.ProgressRing(color=ft.Colors.BLACK)
                                                ])
                                        ),
                                        ],
                                        scroll=ft.ScrollMode.AUTO,  
                                        expand=True,
                            ), 
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    alignment=ft.MainAxisAlignment.CENTER,
                    )
        
        current_container.controls[0].content.controls.append(loading_text)

        page.update()

        overlay_layout = call_layout()

        current_container.controls[0].content.controls.remove(loading_text)

        def go_back():
       
            overlay_copy = list(page.overlay)
            for item in overlay_copy:
                if item.data == "geolocator":
                        pass
                else:
                    page.overlay.remove(item)
            page.update()


        close_button = ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            alignment=ft.alignment.center,
                            on_click=lambda e: go_back(),
                        )],
                        alignment=ft.MainAxisAlignment.CENTER,
                        col=12,
                        expand=True
        )

        current_container.controls[0].content.controls.append(close_button)
        current_container.controls[0].content.controls.append(overlay_layout)

        page.update()

    def add_loading_overlay_page2(self, page, call_layout, current_container, text="Carregando"):

        current_container.content.controls.clear() 

        loading_text = ft.Row([
                        ft.Container(
                            bgcolor=ft.Colors.WHITE,
                            padding=10,
                            margin=10,
                            height=700,
                            width=370,
                            border_radius=20,
                            col=12,
                            content= ft.Column(
                                        controls=[
                                            ft.Container(
                                            visible=True,
                                            alignment=ft.alignment.center,
                                            expand=True,
                                            height=700,
                                            col=12,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,  
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        value=text,
                                                        text_align=ft.TextAlign.CENTER,
                                                        size=30,
                                                        color=ft.Colors.BLACK,
                                                        weight=ft.FontWeight.W_400,
                                                    ),
                                                    ft.ProgressRing(color=ft.Colors.BLACK)
                                                ])
                                        ),
                                        ],
                                        scroll=ft.ScrollMode.AUTO,  
                                        expand=True,
                            ), 
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    alignment=ft.MainAxisAlignment.CENTER,
                    )
        
        current_container.content.controls.append(loading_text)

        page.update()

        layout = call_layout()

        current_container.content.controls.remove(loading_text)

        close_button = ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            alignment=ft.alignment.center,
                            on_click=None,
                        )],
                        alignment=ft.MainAxisAlignment.CENTER,
                        col=12,
                        expand=True
        )

        current_container.content.controls.append(close_button)
        current_container.content.controls.append(layout)
        current_container.height = None

        page.update()

    def back_home(self, page):

        overlay_copy = list(page.overlay)
        for item in overlay_copy:
            if item.data == "geolocator":
                    pass
            else:
                page.overlay.remove(item)
        page.update()


class SupaBase:

    def __init__(self, page):
        self.page = page
        self.supabase_url = "https://kowtaxtvpawukwzeyoif.supabase.co"
        self.supabase_key = (
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtvd3RheHR2cGF3dWt3emV5b2lmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk0NzIyODQsImV4cCI6MjA1NTA0ODI4NH0.DWq3PkIZaLS6qq-tLu6vmFI4ESiXuof7477izTfsR9k"
        )


    def get_url(self):
        return self.supabase_url
    
    def get_key(self):
        return self.supabase_key

    def get_file_id(self):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
            "select": "id"  # Seleciona todos os IDs
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            params=params,
        )

        if response.status_code == 200 and response.json():
            ids = [int(item["id"]) for item in response.json()]  # Obtém todos os IDs e converte para int
            maior_id = max(ids)  # Encontra o maior ID
            return maior_id + 1  # Retorna o próximo ID disponível
        else:
            return 1  # Se não houver registros, começa do 1
        
    def get_delivery_id(self):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
            "select": "id"  # Seleciona todos os IDs
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            params=params,
        )

        if response.status_code == 200 and response.json():
            ids = [int(item["id"]) for item in response.json()]  # Obtém todos os IDs e converte para int
            maior_id = max(ids)  # Encontra o maior ID
            return maior_id + 1  # Retorna o próximo ID disponível
        else:
            return 1  # Se não houver registros, começa do 1
        

    def get_storage(self):

        profile = CurrentProfile()
        dict_profile = profile.return_current_profile()

        storage_path = f'subprojects_ortofoto/{dict_profile["current_project"]}.jpg'
        public_url = f"{self.supabase_url}/storage/v1/object/public/{storage_path}"
        response = requests.get(public_url)
        if response.status_code == 200:
            return public_url 
        else:
            url = "Nulo"
            return url

    def get_all_user_data(self):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "select": "*"
        }


        response = requests.get(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )

        return response

    def get_all_project_data(self):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "select": "*"
        }


        response = requests.get(
            f'{self.supabase_url}/rest/v1/projects',
            headers=headers,
            params=params,
        )

        return response
    
    def get_all_files_data(self):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        params = {
                   "select": "*"
        }
        response = requests.get(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            params=params,
        )
        return response
    
    def get_all_subprojects(self):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        
        params = { 
                   "select": "*"        
                   }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/subprojects',
            headers=headers,
            params=params,
        )

        return response
    
    def get_all_subproject_data(self, project):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        
        params = { 
                   "project": f"eq.{project}",
                   "select": "*"        
                   }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/subprojects',
            headers=headers,
            params=params,
        )

        return response

    def get_subproject_data(self, subproject):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { "name_subproject": f"eq.{subproject}",
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/subprojects',
            headers=headers,
            params=params,
        )

        return response

    def get_user_data_SubPro(self, subproject):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { 
                   "current_project": f"eq.{subproject}",
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )

        return response

    def get_all_deliverys(self):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { 
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            params=params,
        )

        return response
    
    def get_all_files(self):#
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {                    
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            params=params,
        )

        return response

    def get_projects_data(self):

        # É esse aqui

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        params = {
                   "select": "*"
        }
        response = requests.get(
            f'{self.supabase_url}/rest/v1/projects',
            headers=headers,
            params=params,
        )   
        return response
    
    # 25/03/2025
    def get_one_project_data(self, project):

        # É esse aqui

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        params = {
                   "name_project":  f"eq.{project}", 
                   "select": "*"
        }
        response = requests.get(
            f'{self.supabase_url}/rest/v1/projects',
            headers=headers,
            params=params,
        )   
        return response

    def get_one_subproject_data(self, subprojects):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        params = {
                   "name_project":  f"eq.{subprojects}", 
                   "select": "*"
        }
        response = requests.get(
            f'{self.supabase_url}/rest/v1/subprojects',
            headers=headers,
            params=params,
        )   
        return response

    def get_form_user(self, user):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
        "usuario": f"eq.{user}",
        "select": "user_id, usuario, email, numero, senha, permission",
        }

        profile = CurrentProfile()
        current_profile = profile.return_current_profile()

        response = requests.get(
            f'{self.supabase_url}/rest/v1/users_{current_profile["city_call_name"]}',
            headers=headers,
            params=params,
        )

        return response

    def get_user_data(self, users):


        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { 
                   "username": f"eq.{users}",
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )   

        return response     

    def get_forms(self, name, object):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        geo_objects = Objects(page=None)
        method_map = geo_objects.sp_get_forms_object(name)

        profile = CurrentProfile()
        current_profile = profile.return_current_profile()

        response = requests.get(
            f'{self.supabase_url}/rest/v1/form_{object}_{current_profile["city_call_name"]}',
            headers=headers,
            params=method_map[object],
        )

        return response
    
    def post_to_deliverys_data(self, data):
            
        headers= {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
                }

        response = requests.post(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            json=data,
        )

        return response
     
    def post_to_files(self, id, date, username, subproject, type, amount, url):
            
        headers= {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
                }
        
        data= { 
                "id": id,
                "username": username,
                "date": date,
                "subproject": subproject,
                "type": type,
                "amount": amount,
                "url": url,
                }
        
        response = requests.post(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            json=data,
        )

        return response

    def post_project_data(self, name_project, current_subprojects, final_delivery, predicted_lots):
            
            headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
            }

            get_pjc = { 
                "name_project": name_project,
                "current_subprojects": current_subprojects,
                "final_delivery": final_delivery,
                "predicted_lots": predicted_lots,
                "lots_done": "0",
                "percent": "0",         
            }

            response = requests.post(
                f'{self.supabase_url}/rest/v1/projects',
                headers=headers,
                json=get_pjc,
            )

            return response 
    
    def post_subproject_data(self, data):
            
            headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
            }

            response = requests.post(
                f'{self.supabase_url}/rest/v1/subprojects',
                headers=headers,
                json=data,
            )

            return response
     

    def get_deliverys_data_total(self, username):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { "username": f"eq.{username}",
                   "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            params=params,
        )

        return response

    def get_user_deliverys_data(self, subproject, username):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { 
                "name_subproject": f"eq.{subproject}",
                "username": f"eq.{username}",
                "select": "*"
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            params=params,
        )

        return response

    def get_all_username(self, username):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = { 
                "username": f"eq.{username}",
                
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )

        return response
        
    

    

    def add_file_storage(self, file, name_file, type):

        if type == "poligonos":
            content_type = "image/vnd.dwg"
        elif type == "fotos":
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        headers = {
            'Authorization': f'Bearer {self.supabase_key}',
            'Content-Type': content_type,
        }

        bytes = []
        bytes.append(file)

        if not self.page.web:
            with open(file.path, 'rb') as file_data:
                bytes[0] = file_data.read()

        response = requests.post(
                f'{self.supabase_url}/storage/v1/object/files/{name_file}',  
                headers=headers,
                data=bytes[0]
            )

        return response
    
    def add_subproject_storage(self, file, name_file, type, local):

        if type == "dwg":
            content_type = "image/vnd.dwg"
        elif type == "xlsx":
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        headers = {
            'Authorization': f'Bearer {self.supabase_key}',
            'Content-Type': content_type,
        }

        bytes = []
        bytes.append(file)

        if not self.page.web:
            with open(file.path, 'rb') as file_data:
                bytes[0] = file_data.read()

        response = requests.post(
                f'{self.supabase_url}/storage/v1/object/{local}/{name_file}',  
                headers=headers,
                data=bytes[0]
            )

        return response




    def create_user_data(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            json=data,
        )

        return response    

    
    def edit_subproject_data(self, subproject_data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.patch(
            f'{self.supabase_url}/rest/v1/subprojects?name_subproject=eq.{subproject_data["name_subproject"]}',
            headers=headers,
            json=subproject_data,
        )   
        return response

    def edit_projects_data(self, data_project):

        headers = {

            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.patch(

            f'{self.supabase_url}/rest/v1/projects?name_project=eq.{data_project["name_project"]}',
            headers=headers,
            json=data_project,
        )   
        return response


    def edit_user_data(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.patch(
            f'{self.supabase_url}/rest/v1/users?username=eq.{data["username"]}',
            headers=headers,
            json=data,
        )

        return response    

    def edit_delivery_data(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "username":  f"eq.{data["username"]}", 
                   "date":  f"eq.{data["date"]}", 
                   "select": "*"
        }

        response = requests.patch(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            json=data,
            params=params,
        )

        return response    

    def edit_files(self,supa_list):
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }
        
        data = {   
            "date": supa_list[0],
            "username": supa_list[1],
            "subproject": supa_list[2],
            "polygons": supa_list[3],
            "type": supa_list[4],     
            "amount": supa_list[5],
            "url": supa_list[6],                       
        }

        response = requests.patch(
            f'{self.supabase_url}/rest/v1/files?username=eq.{supa_list[1]}',
            headers=headers,
            json=data,
        )

        return response    

    def check_login(self, username, password):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
            "or": f"(username.eq.{username},email.eq.{username})",
            "password": f"eq.{password}",
            "select": "*"
        }

        profile = CurrentProfile()
        current_profile = profile.return_current_profile()

        response = requests.get(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )

        return response
    
    def check_file(self, date, username):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
        "username": f"eq.{username}",   
        "date": f"eq.{date}",
        "select": "*",
        }

        response = requests.get(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            params=params,
        )

        return response

    
    def delete_subproject(self, subproject):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.delete(
            f'{self.supabase_url}/rest/v1/subprojects?name_subproject=eq.{subproject}',
            headers=headers,
        )

        return response
    
    def delete_delivery(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "username":  f"eq.{data["username"]}", 
                   "date":  f"eq.{data["date"]}", 
                   "select": "*"
        }

        response = requests.delete(
            f'{self.supabase_url}/rest/v1/deliverys',
            headers=headers,
            params=params,
        )

        return response

    def delete_file_data(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "username":  f"eq.{data["username"]}", 
                   "date":  f"eq.{data["date"]}", 
                   "select": "*"
        }

        response = requests.delete(
            f'{self.supabase_url}/rest/v1/files',
            headers=headers,
            params=params,
        )

        return response
    
    def delete_user_data(self, data):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        params = {
                   "username":  f"eq.{data["username"]}", 
                   "select": "*"
        }

        response = requests.delete(
            f'{self.supabase_url}/rest/v1/users',
            headers=headers,
            params=params,
        )

        print(response.text)

        return response
    
    def delete_project(self, project):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

        response = requests.delete(
            f'{self.supabase_url}/rest/v1/projects?name_project=eq.{project}',
            headers=headers,
        )

        return response
    
    def delete_storage(self, local, object, type):

        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": type,
        }

        response = requests.delete(
            f'{self.supabase_url}/storage/v1/object/{local}/{object}',  
            headers=headers,
        )

        print(response.text)

        return response
    

class CurrentMapPoints:
    current_points = []

    def return_current_points(self):
        return self.current_points

    def add_list_point(self, points):
        self.current_points.clear()
        for item in points:
            self.current_points.append(item)

    def add_point(self, point):
        self.current_points.append(point)

    def remove_point(self, name_point):
        for item in self.current_points:
            if item.data[0] == name_point:
                self.current_points.remove(item)

    def filter_points(self, new_filter, new_order_filter):
        for item in self.current_points:
            if item.data == "point_location":
                continue  

            if item.data[1] not in new_filter:
                item.content.opacity = 0  
                continue  

            if item.data[4] not in new_order_filter:
                item.content.opacity = 0 
            else:
                item.content.opacity = 1  


class CurrentProfile:
    current_profile = {
        "username": None,
        "name": None,
        "permission": None,
        "current_project": None,
    }

    def return_current_profile(self):
        return self.current_profile

    def add_current_project(self, current_project):
        self.current_profile["current_project"] = current_project

    def add_username(self, username):
        self.current_profile["username"] = username

    def add_name(self, name):
        self.current_profile["name"] = name

    def add_permission(self, permission):
        self.current_profile["permission"] = permission

    
class Objects:

    def __init__(self, page):
        self.page = page

    def city_objects(self, list_objects):

        list_current_objects = []
        if "post" in list_objects:
            list_current_objects.append("post")
        if "tree" in list_objects:
            list_current_objects.append("tree")
        if "grass" in list_objects:
            list_current_objects.append("grass")
        
        return list_current_objects


    def form_object1(self):

        method_map = {
            "IP" : "Poste",
            "IA": "Árvore",
            "IV": "Vegetação",
        }

        return method_map
    
    def form_object2(self):

        method_map = {
            "post" : "Poste",
            "tree": "Árvore",
            "grass": "Vegetação",
        }

        return method_map

    def add_object(self, object):

        textfields = TextField(self.page)
        sp = SupaBase(self.page)
        new_number = sp.get_last_form(object)

        def drop_down_menu(value=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None):

                list = [opt1, opt2, opt3, opt4, opt5, opt6]
                list_option = []
                for opt in list:
                    if opt != None:
                        list_option.append(ft.dropdown.Option(opt))

                menu = ft.Dropdown(
                    options=list_option,
                    value=value,
                    label_style=ft.TextStyle(color=ft.Colors.BLACK, size=12),
                    bgcolor=ft.Colors.WHITE,
                    options_fill_horizontally=True,
                    text_style= ft.TextStyle(size=12, color=ft.Colors.BLACK)
                )
                return menu

        dicio_add_object = {
                    "post": {
                        "IP": textfields.create_textfield(value=new_number, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Situação": drop_down_menu(None, "Com iluminação", "Sem iluminação"),
                        "Tipo de Lâmpada": drop_down_menu(None, ".", "Lâmpada LED", "Lâmpada de vapor de sódio"),
                        "Pontos": drop_down_menu(None, "0","1", "2", "3", "4", "5"),
                        "Bairro": textfields.create_textfield(value=None, text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=None, text=None, password=False)
                    },
                    "tree": {
                        "IA": textfields.create_textfield(value=new_number, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Tipo": drop_down_menu(None, "Frutífera", "Infrutífera"),
                        "Altura aproximada": textfields.create_textfield(value=None, text=None, password=False),
                        "Diâmetro do tronco": textfields.create_textfield(value=None, text=None, password=False),
                        "Bairro": textfields.create_textfield(value=None, text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=None, text=None, password=False)
                    },
                    "grass": {
                        "IV": textfields.create_textfield(value=new_number, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Tipo": drop_down_menu(None, "Grama", "Capim"),
                        "Altura aproximada": textfields.create_textfield(value=None, text=None, password=False),
                        "Local": drop_down_menu(None, "Público", "Particular"),
                        "Bairro": textfields.create_textfield(value=None, text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=None, text=None, password=False)
                    }
                }
        
        return dicio_add_object

    def view_object(self, name, object):

        sp = SupaBase(self.page)

        point = sp.get_forms(name, object)
        data = point.json()
        row = data[0]

        default_value = "N/A"

        method_map = {
            "post": [
                row.get("name", default_value), 
                row.get("situation", default_value), 
                row.get("type", default_value), 
                row.get("point", default_value), 
                row.get("hood", default_value), 
                row.get("address", default_value)
            ],
            "tree": [
                row.get("name", default_value), 
                row.get("type", default_value), 
                row.get("height", default_value), 
                row.get("diameter", default_value), 
                row.get("hood", default_value), 
                row.get("address", default_value)
            ],
            "grass": [
                row.get("name", default_value), 
                row.get("type", default_value), 
                row.get("height", default_value), 
                row.get("local", default_value), 
                row.get("hood", default_value), 
                row.get("address", default_value)
            ],
        }
        
        dicio_view_object = {
            "post": {
                "IP": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Situação": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Tipo de Lâmpada": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Pontos": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Bairro": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Logradouro": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
                },
            "tree": {
                "IA": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Tipo": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Altura aproximada": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Diâmetro do tronco": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Bairro": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Logradouro": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
                },
            "grass": {
                "IV": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Tipo": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Altura aproximada": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Local": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Bairro": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Logradouro": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
                },
        }

        return dicio_view_object

    def edit_object(self, name, object, row):

        sp = SupaBase(self.page)
        textfields = TextField(self.page)

        numero = int(row["name"].split('-')[1])
        default_value = "N/A"

        def drop_down_menu(value=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None):

                list = [opt1, opt2, opt3, opt4, opt5, opt6]
                list_option = []
                for opt in list:
                    if opt != None:
                        list_option.append(ft.dropdown.Option(opt))

                menu = ft.Dropdown(
                    options=list_option,
                    value=value,
                    label_style=ft.TextStyle(color=ft.Colors.BLACK, size=12),
                    bgcolor=ft.Colors.WHITE,
                    options_fill_horizontally=True,
                    text_style= ft.TextStyle(size=12, color=ft.Colors.BLACK)
                )
                return menu

        dicio_edit_object = {
                    "post": {
                        "IP": textfields.create_textfield(value=numero, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Situação": drop_down_menu(row.get("situation", default_value), "Com iluminação", "Sem iluminação"),
                        "Tipo de Lâmpada": drop_down_menu(row.get("type", default_value), ".", "Lâmpada LED", "Lâmpada de vapor de sódio"),
                        "Pontos": drop_down_menu(row.get("point", default_value), "0","1", "2", "3", "4", "5"),
                        "Bairro": textfields.create_textfield(value=row.get("hood", default_value), text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=row.get("address", default_value), text=None, password=False)
                    },
                    "tree": {
                        "IA": textfields.create_textfield(value=numero, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Tipo": drop_down_menu(row.get("type", default_value), "Frutífera", "Infrutífera"),
                        "Altura aproximada": textfields.create_textfield(value=row.get("height", default_value), text=None, password=False),
                        "Diâmetro do tronco": textfields.create_textfield(value=row.get("diameter", default_value), text=None, password=False),
                        "Bairro": textfields.create_textfield(value=row.get("hood", default_value), text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=row.get("address", default_value), text=None, password=False)
                    },
                    "grass": {
                        "IA": textfields.create_textfield(value=numero, text=None, password=False, read=None, input_filter=ft.NumbersOnlyInputFilter(), keyboard_type=ft.KeyboardType.NUMBER),
                        "Tipo": drop_down_menu(row.get("type", default_value), "Grama", "Capim"),
                        "Altura aproximada": textfields.create_textfield(value=row.get("height", default_value), text=None, password=False),
                        "Local": drop_down_menu(row.get("local", default_value), "Público", "Particular"),
                        "Bairro": textfields.create_textfield(value=row.get("hood", default_value), text=None, password=False),
                        "Logradouro": textfields.create_textfield(value=row.get("address", default_value), text=None, password=False)
                    },
                }
        
        return dicio_edit_object

    def add_os_object(self, name, object):

        sp = SupaBase(self.page)
        textfields = TextField(self.page)

        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y")
        id = str(sp.get_os_id(object))
        new_order = id.zfill(4)
        profile = CurrentProfile()
        dict_profile = profile.return_current_profile()

        def drop_down_menu(value=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None):

            list = [opt1, opt2, opt3, opt4, opt5, opt6]
            list_option = []
            for opt in list:
                if opt != None:
                    list_option.append(ft.dropdown.Option(opt))

            menu = ft.Dropdown(
                options=list_option,
                value=value,
                label_style=ft.TextStyle(color=ft.Colors.BLACK, size=12),
                bgcolor=ft.Colors.WHITE,
                options_fill_horizontally=True,
                text_style= ft.TextStyle(size=12, color=ft.Colors.BLACK)
            )
            return menu

        dicio_add_order = {
                    "post": {
                        "Data de Criação": textfields.create_textfield(value=data_formatada, text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=name, text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=dict_profile["user"], text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=dict_profile["permission"], text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=dict_profile["number"], text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=new_order, text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=None, text=None, password=False),
                        "Observação": textfields.create_textfield(value=None, text=None, password=False),
                        "Material": textfields.create_textfield(value=None, text=None, password=False),
                        "Ponto Queimado": drop_down_menu(None, "1", "2", "3", "4", "5"),
                        "Status": drop_down_menu("Aberto", "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Equipe": textfields.create_textfield(value=None, text=None, password=False), 
                    },
                    "tree": {
                        "Data de Criação": textfields.create_textfield(value=data_formatada, text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=name, text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=dict_profile["user"], text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=dict_profile["permission"], text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=dict_profile["number"], text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=new_order, text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=None, text=None, password=False),
                        "Observação": textfields.create_textfield(value=None, text=None, password=False),
                        "Material": textfields.create_textfield(value=None, text=None, password=False),
                        "Altura": drop_down_menu(None, "1", "2", "3", "4", "5"),
                        "Status": drop_down_menu("Aberto", "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Equipe": textfields.create_textfield(value=None, text=None, password=False), 
                    },
                    "grass": {
                        "Data de Criação": textfields.create_textfield(value=data_formatada, text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=name, text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=dict_profile["user"], text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=dict_profile["permission"], text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=dict_profile["number"], text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=new_order, text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=None, text=None, password=False),
                        "Observação": textfields.create_textfield(value=None, text=None, password=False),
                        "Material": textfields.create_textfield(value=None, text=None, password=False),
                        "Local": drop_down_menu(None, "Público", "Particular"),
                        "Status": drop_down_menu("Aberto", "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value="Pendente", text=None, password=False),
                        "Equipe": textfields.create_textfield(value=None, text=None, password=False), 
                    },
                }
        
        return dicio_add_order
    
    def view_os_object(self, order, object):

        sp = SupaBase(self.page)

        os = sp.get_os(order, object)

        data = os.json()

        row = data[0]

        default_value = "N/A"

        method_map = {
            "post": [
                row.get("created_at", default_value), 
                row.get("ip", default_value), 
                row.get("reclamante", default_value), 
                row.get("function", default_value), 
                row.get("celular", default_value), 
                row.get("order_id", default_value),
                row.get("origem", default_value),
                row.get("observacao", default_value),
                row.get("materiais", default_value),
                row.get("ponto", default_value),
                row.get("status", default_value),
                row.get("data_andamento", default_value),
                row.get("data_conclusao", default_value),
                row.get("equipe", default_value),
            ],
            "tree": [
                row.get("created_at", default_value), 
                row.get("ip", default_value), 
                row.get("reclamante", default_value), 
                row.get("function", default_value), 
                row.get("celular", default_value), 
                row.get("order_id", default_value),
                row.get("origem", default_value),
                row.get("observacao", default_value),
                row.get("materiais", default_value),
                row.get("altura", default_value),
                row.get("status", default_value),
                row.get("data_andamento", default_value),
                row.get("data_conclusao", default_value),
                row.get("equipe", default_value),
            ],
            "grass": [
                row.get("created_at", default_value), 
                row.get("ip", default_value), 
                row.get("reclamante", default_value), 
                row.get("function", default_value), 
                row.get("celular", default_value), 
                row.get("order_id", default_value),
                row.get("origem", default_value),
                row.get("observacao", default_value),
                row.get("materiais", default_value),
                row.get("local", default_value),
                row.get("status", default_value),
                row.get("data_andamento", default_value),
                row.get("data_conclusao", default_value),
                row.get("equipe", default_value),
            ],
        }

        dicio_view_os = {
            "post" : {
                "Criação": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "IP": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Reclamante": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Usuário": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Celular": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Ordem": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Origem": ft.Text(value=method_map[object][6], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Observação": ft.Text(value=method_map[object][7], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Materiais": ft.Text(value=method_map[object][8], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Ponto": ft.Text(value=method_map[object][9], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Status": ft.Text(value=method_map[object][10], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data do andamento": ft.Text(value=method_map[object][11], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data da conclusão": ft.Text(value=method_map[object][12], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Equipe": ft.Text(value=method_map[object][13], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                },
            "tree": {
                "Criação": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "IP": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Reclamante": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Usuário": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Celular": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Ordem": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Origem": ft.Text(value=method_map[object][6], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Observação": ft.Text(value=method_map[object][7], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Materiais": ft.Text(value=method_map[object][8], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Altura": ft.Text(value=method_map[object][9], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Status": ft.Text(value=method_map[object][10], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data do andamento": ft.Text(value=method_map[object][11], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data da conclusão": ft.Text(value=method_map[object][12], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Equipe": ft.Text(value=method_map[object][13], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                },
            "grass": {
                "Criação": ft.Text(value=method_map[object][0], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "IP": ft.Text(value=method_map[object][1], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Reclamante": ft.Text(value=method_map[object][2], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Usuário": ft.Text(value=method_map[object][3], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Celular": ft.Text(value=method_map[object][4], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Ordem": ft.Text(value=method_map[object][5], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Origem": ft.Text(value=method_map[object][6], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Observação": ft.Text(value=method_map[object][7], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Materiais": ft.Text(value=method_map[object][8], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Local": ft.Text(value=method_map[object][9], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Status": ft.Text(value=method_map[object][10], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data do andamento": ft.Text(value=method_map[object][11], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Data da conclusão": ft.Text(value=method_map[object][12], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                "Equipe": ft.Text(value=method_map[object][13], theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                },
        }

        return dicio_view_os

    def view_window_object(self, dicio_filter):
        pass

    def edit_os_object(self, order, object):
       
        sp = SupaBase(self.page)
        textfields = TextField(self.page) 

        os = sp.get_os(order, object)
        data = os.json()
        row = data[0]
        default_value = "N/A"

        def drop_down_menu(value=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None):

                list = [opt1, opt2, opt3, opt4, opt5, opt6]
                list_option = []
                for opt in list:
                    if opt != None:
                        list_option.append(ft.dropdown.Option(opt))

                menu = ft.Dropdown(
                    options=list_option,
                    value=value,
                    label_style=ft.TextStyle(color=ft.Colors.BLACK, size=12),
                    bgcolor=ft.Colors.WHITE,
                    options_fill_horizontally=True,
                    text_style= ft.TextStyle(size=12, color=ft.Colors.BLACK)
                )
                return menu

        dicio_edit_os_object = {
                    "post": {
                        "Data de Criação": textfields.create_textfield(value=row.get("created_at", default_value), text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=row.get("ip", default_value), text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=row.get("reclamante", default_value), text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=row.get("function", default_value), text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=row.get("celular", default_value), text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=row.get("order_id", default_value), text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=row.get("origem", default_value), text=None, password=False),
                        "Observação": textfields.create_textfield(value=row.get("observacao", default_value), text=None, password=False),
                        "Material": textfields.create_textfield(value=row.get("materiais", default_value), text=None, password=False),
                        "Ponto Queimado": drop_down_menu(row.get("ponto", default_value), "1", "2", "3", "4", "5"),
                        "Status": drop_down_menu(row.get("status", default_value), "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value=row.get("data_andamento", default_value), text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value=row.get("data_conclusao", default_value), text=None, password=False),
                        "Equipe": textfields.create_textfield(value=row.get("equipe", default_value), text=None, password=False), 
                    },
                    "tree": {
                        "Data de Criação": textfields.create_textfield(value=row.get("created_at", default_value), text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=row.get("ip", default_value), text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=row.get("reclamante", default_value), text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=row.get("function", default_value), text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=row.get("celular", default_value), text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=row.get("order_id", default_value), text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=row.get("origem", default_value), text=None, password=False),
                        "Observação": textfields.create_textfield(value=row.get("observacao", default_value), text=None, password=False),
                        "Material": textfields.create_textfield(value=row.get("materiais", default_value), text=None, password=False),
                        "Altura": drop_down_menu(row.get("altura", default_value), "1", "2", "3", "4", "5"),
                        "Status": drop_down_menu(row.get("status", default_value), "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value=row.get("data_andamento", default_value), text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value=row.get("data_conclusao", default_value), text=None, password=False),
                        "Equipe": textfields.create_textfield(value=row.get("equipe", default_value), text=None, password=False), 
                    },
                    "grass": {
                        "Data de Criação": textfields.create_textfield(value=row.get("created_at", default_value), text=None, password=False, read=True),
                        "IP": textfields.create_textfield(value=row.get("ip", default_value), text=None, password=False, read=True),
                        "Reclamante": textfields.create_textfield(value=row.get("reclamante", default_value), text=None, password=False, read=True),
                        "Usuário": textfields.create_textfield(value=row.get("function", default_value), text=None, password=False, read=True),
                        "Celular": textfields.create_textfield(value=row.get("celular", default_value), text=None, password=False, read=True),
                        "Ordem": textfields.create_textfield(value=row.get("order_id", default_value), text=None, password=False, read=True),
                        "Origem": textfields.create_textfield(value=row.get("origem", default_value), text=None, password=False),
                        "Observação": textfields.create_textfield(value=row.get("observacao", default_value), text=None, password=False),
                        "Material": textfields.create_textfield(value=row.get("materiais", default_value), text=None, password=False),
                        "Local": drop_down_menu(row.get("local", default_value), "Público", "Particular"),
                        "Status": drop_down_menu(row.get("status", default_value), "Aberto", "Andamento", "Concluido"),
                        "Data de Andamento": textfields.create_textfield(value=row.get("data_andamento", default_value), text=None, password=False),
                        "Data de Conclusão": textfields.create_textfield(value=row.get("data_conclusao", default_value), text=None, password=False),
                        "Equipe": textfields.create_textfield(value=row.get("equipe", default_value), text=None, password=False), 
                    },
                }
        
        return dicio_edit_os_object
    
    def add_point_object(self, new_number):

        profile = CurrentProfile()
        current_profile = profile.return_current_profile()

        dicio_point_object = {
                "post": f'IP {current_profile["city_acronym"]}-{new_number}',
                "tree": f'IA {current_profile["city_acronym"]}-{new_number}',
                "grass": f'IV {current_profile["city_acronym"]}-{new_number}',
            }
        
        return dicio_point_object
    
    def add_button_point_object(self):

        buttons = Buttons(self.page)

        dicio_button_point_object = {
                "post": buttons.create_point_button_post,
                "tree": buttons.create_point_button_tree,
                "grass": buttons.create_point_button_grass,
            }
        
        return dicio_button_point_object
    
    def sp_get_forms_object(self, name):

        method_map = {
            "post": {"name": f"eq.{name}","select": "name, situation, type, point, hood, address"},
            "tree": {"name": f"eq.{name}","select": "name, type, height, diameter, hood, address"},
            "grass": {"name": f"eq.{name}","select": "name, type, height, local, hood, address"},
        }

        return method_map
    
    def sp_get_os_object(self, order):

        method_map = {
            "post": {
                    "order_id": f"eq.{order}",
                    "select": "created_at, ip, reclamante, function, celular, order_id, origem, observacao, materiais, ponto, status, data_andamento, data_conclusao, equipe",
                    },

            "tree": {
                    "order_id": f"eq.{order}",
                    "select": "created_at, ip, reclamante, function, celular, order_id, origem, observacao, materiais, altura, status, data_andamento, data_conclusao, equipe",
                    },
            "grass": {
                    "order_id": f"eq.{order}",
                    "select": "created_at, ip, reclamante, function, celular, order_id, origem, observacao, materiais, local, status, data_andamento, data_conclusao, equipe",
                    },
        }

        return method_map
    
    def sp_add_point1_object(self):

        method_map = {
                "post": {
                        "Lâmpada LED": "white",
                        "Lâmpada de vapor de sódio": "yellow",
                        ".": "blue"
                        },
                "tree": defaultdict(lambda: "green"),
                "grass": defaultdict(lambda: "green"),
            }

        return method_map
    
    def sp_add_point2_object(self, list_forms, method_map, object):

        method_map = {
                "post": {
                    "name": method_map[object],
                    "situation": list_forms[1],
                    "type": list_forms[2],
                    "point": list_forms[3],
                    "hood": list_forms[4],
                    "address": list_forms[5],
                },
                "tree": {
                    "name": method_map[object],
                    "type": list_forms[1],
                    "height": list_forms[2],
                    "diameter": list_forms[3],
                    "hood": list_forms[4],
                    "address": list_forms[5],
                },
                "grass": {
                    "name": method_map[object],
                    "type": list_forms[1],
                    "height": list_forms[2],
                    "local": list_forms[3],
                    "hood": list_forms[4],
                    "address": list_forms[5],
                },
                
            }

        return method_map
    
    def sp_add_point3_object(self, list_forms, method_map, object, coordinates, point_color, data_formatada, dict_profile):

        method_map = {
                "post": {
                    "name": method_map[object],
                    "x": coordinates[0],
                    "y": coordinates[1],
                    "type": list_forms[2],
                    "color": point_color,
                    "changed_at": data_formatada,
                    "changed_by": dict_profile["user"],
                    "object": object,
                },
                "tree": {
                    "name": method_map[object],
                    "x": coordinates[0],
                    "y": coordinates[1],
                    "type": "tree",
                    "color": point_color,
                    "changed_at": data_formatada,
                    "changed_by": dict_profile["user"],
                    "object": object,
                },
                "grass": {
                    "name": method_map[object],
                    "x": coordinates[0],
                    "y": coordinates[1],
                    "type": "grass",
                    "color": point_color,
                    "changed_at": data_formatada,
                    "changed_by": dict_profile["user"],
                    "object": object,
                },
                
            }

        return method_map

    def sp_add_os_object(self, list_add_os, number):

        method_map = {
                "post": {
                    "created_at": list_add_os[0],
                    "ip": list_add_os[1],
                    "numero": number,
                    "reclamante": list_add_os[2],
                    "function": list_add_os[3],
                    "celular": list_add_os[4],
                    "order_id": list_add_os[5],
                    "origem": list_add_os[6],
                    "observacao": list_add_os[7],
                    "materiais": list_add_os[8],
                    "ponto": list_add_os[9],
                    "status": list_add_os[10],
                    "data_andamento": list_add_os[11],
                    "data_conclusao": list_add_os[12],
                    "equipe": list_add_os[13],
                    },
                "tree": {
                    "created_at": list_add_os[0],
                    "ip": list_add_os[1],
                    "numero": number,
                    "reclamante": list_add_os[2],
                    "function": list_add_os[3],
                    "celular": list_add_os[4],
                    "order_id": list_add_os[5],
                    "origem": list_add_os[6],
                    "observacao": list_add_os[7],
                    "materiais": list_add_os[8],
                    "altura": list_add_os[9],
                    "status": list_add_os[10],
                    "data_andamento": list_add_os[11],
                    "data_conclusao": list_add_os[12],
                    "equipe": list_add_os[13],
                    },
                "grass": {
                    "created_at": list_add_os[0],
                    "ip": list_add_os[1],
                    "numero": number,
                    "reclamante": list_add_os[2],
                    "function": list_add_os[3],
                    "celular": list_add_os[4],
                    "order_id": list_add_os[5],
                    "origem": list_add_os[6],
                    "observacao": list_add_os[7],
                    "materiais": list_add_os[8],
                    "local": list_add_os[9],
                    "status": list_add_os[10],
                    "data_andamento": list_add_os[11],
                    "data_conclusao": list_add_os[12],
                    "equipe": list_add_os[13],
                    },
                
            }
        return method_map

    def sp_edit_point_object(self, previous_data):

        default_value = "N/A"

        method_map = {
                "post": {
                    "name": previous_data.get("name", default_value),
                    "situation": previous_data.get("situation", default_value),
                    "type": previous_data.get("type", default_value),
                    "point": previous_data.get("point", default_value),
                    "hood": previous_data.get("hood", default_value),
                    "address": previous_data.get("address", default_value),
                },
                "tree": {
                    "name": previous_data.get("name", default_value),
                    "type": previous_data.get("type", default_value),
                    "height": previous_data.get("height", default_value),
                    "diameter": previous_data.get("diameter", default_value),
                    "hood": previous_data.get("hood", default_value),
                    "address": previous_data.get("address", default_value),
                },
                "grass": {
                    "name": previous_data.get("name", default_value),
                    "type": previous_data.get("type", default_value),
                    "height": previous_data.get("height", default_value),
                    "local": previous_data.get("local", default_value),
                    "hood": previous_data.get("hood", default_value),
                    "address": previous_data.get("address", default_value),
                },
                
            }
        
        return method_map

    def sp_edit_os_object(self, list_edited_os_forms, number):

        method_map = {
                "post": {
                    "created_at": list_edited_os_forms[0],
                    "ip": list_edited_os_forms[1],
                    "numero": number,
                    "reclamante": list_edited_os_forms[2],
                    "function": list_edited_os_forms[3],
                    "celular": list_edited_os_forms[4],
                    "order_id": list_edited_os_forms[5],
                    "origem": list_edited_os_forms[6],
                    "observacao": list_edited_os_forms[7],
                    "materiais": list_edited_os_forms[8],
                    "ponto": list_edited_os_forms[9],
                    "status": list_edited_os_forms[10],
                    "data_andamento": list_edited_os_forms[11],
                    "data_conclusao": list_edited_os_forms[12],
                    "equipe": list_edited_os_forms[13],
                    },
                "tree": {
                    "created_at": list_edited_os_forms[0],
                    "ip": list_edited_os_forms[1],
                    "numero": number,
                    "reclamante": list_edited_os_forms[2],
                    "function": list_edited_os_forms[3],
                    "celular": list_edited_os_forms[4],
                    "order_id": list_edited_os_forms[5],
                    "origem": list_edited_os_forms[6],
                    "observacao": list_edited_os_forms[7],
                    "materiais": list_edited_os_forms[8],
                    "altura": list_edited_os_forms[9],
                    "status": list_edited_os_forms[10],
                    "data_andamento": list_edited_os_forms[11],
                    "data_conclusao": list_edited_os_forms[12],
                    "equipe": list_edited_os_forms[13],
                    },  
                "grass": {
                    "created_at": list_edited_os_forms[0],
                    "ip": list_edited_os_forms[1],
                    "numero": number,
                    "reclamante": list_edited_os_forms[2],
                    "function": list_edited_os_forms[3],
                    "celular": list_edited_os_forms[4],
                    "order_id": list_edited_os_forms[5],
                    "origem": list_edited_os_forms[6],
                    "observacao": list_edited_os_forms[7],
                    "materiais": list_edited_os_forms[8],
                    "local": list_edited_os_forms[9],
                    "status": list_edited_os_forms[10],
                    "data_andamento": list_edited_os_forms[11],
                    "data_conclusao": list_edited_os_forms[12],
                    "equipe": list_edited_os_forms[13],
                    },  
                }
        
        return method_map
    
    def data_objects(self):

        all_list_objects = [["post","Lista de Postes", "OS de Postes", "Adicionar Poste"],
                        ["tree","Lista de Àrvores", "OS de Àrvores", "Adicionar Árvore"],
                        ["grass","Lista de Vegetação Densa", "OS de Vegetação Densa", "Adicionar Vegetação Densa"],
                    ]
        current_list_objects = []
        profile = CurrentProfile()
        current_profile = profile.return_current_profile()
        current_objects = current_profile["city_objects"]
        for item in all_list_objects:
            if item[0] in current_objects:
                current_list_objects.append(item)
            else:
                pass

        return current_list_objects
    
    def container_add_object(self, list_actions):

        list_objects = []
        profile = CurrentProfile()
        current_profile = profile.return_current_profile()
        current_objects = current_profile["city_objects"]
        if "post" in current_objects:
            list_objects.append("Informações de Postes")
        if "tree" in current_objects:
            list_objects.append("Informações de Àrvores")
        if "grass" in current_objects:
            list_objects.append("Informações de Vegetação Densa")
        list_name = []
        n = 0
        for object in list_objects:
            tile = ft.ListTile(
                title=ft.Text(value=object, color=ft.Colors.BLACK),
                on_click=list_actions[n],
                bgcolor=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),
            )
            list_name.append(tile)
            n += 1
        return list_name
    
    def container_add_object2(self, list_name_actions):

        list_name = []
        for object in list_name_actions:
            tile = ft.ListTile(
                title=ft.Text(value=object[0], color=ft.Colors.BLACK),
                on_click=object[1],
                bgcolor=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),
            )
            list_name.append(tile)
        return list_name
    
    def pdf_os_object(self):

        method_map = {
            "post": ["Criação", "Nome", "Reclamante", "Usuário", "Celular", "Ordem", "Origem", "Observação", "Materiais", "Pontos", "Status", "Data do andamento", "Data da conclusão", "Equipe"],
            "tree": ["Criação", "Nome", "Reclamante", "Usuário", "Celular", "Ordem", "Origem", "Observação", "Materiais", "Altura", "Status", "Data do andamento", "Data da conclusão", "Equipe"],
            "grass": ["Criação", "Nome", "Reclamante", "Usuário", "Celular", "Ordem", "Origem", "Observação", "Materiais", "Local", "Status", "Data do andamento", "Data da conclusão", "Equipe"],
        }

        return method_map
    
    def pdf_forms_object(self):

        method_map = {
            "post": ["Nome", "Situação", "Tipo", "Pontos", "Bairro", "Rua"],
            "tree": ["Nome", "Situação", "Tipo", "Altura", "Bairro", "Rua"],
            "grass": ["Nome", "Situação", "Tipo", "Local", "Bairro", "Rua"],
        }

        return method_map
    
    def view_user_data(self, row):

        default_value = "N/A"

        dicio_view_object = {

            "Nome": ft.Text(value=row.get("name", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Entregas semanais": ft.Text(value=row.get("weekly_deliveries", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Entregas Totais": ft.Text(value=row.get("total_deliverys", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Poligonos Feitos": ft.Text(value=row.get("polygons_made", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Poligonos Errados": ft.Text(value=row.get("polygons_wrong", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Atrasos": ft.Text(value=row.get("delays", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Advertencias": ft.Text(value=row.get("warnings", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM)

        }

        return dicio_view_object

    def view_user_data2(self, row):

        default_value = "N/A"

        dicio_view_object = {

            "Nome": ft.Text(value=row.get("name_subproject", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Lotes Previstos": ft.Text(value=row.get("predicted_lots", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Lotes Feitos": ft.Text(value=row.get("lots_done", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Entrega Final": ft.Text(value=row.get("final_delivery", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Entregas": ft.Text(value=row.get("deliverys", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Média recomendada": ft.Text(value=row.get("recommended_medium", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Média atual": ft.Text(value=row.get("current_average", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Porcentagem": ft.Text(value=row.get("percent", default_value), theme_style=ft.TextThemeStyle.TITLE_MEDIUM)

        }

        return dicio_view_object
    
    def view_user_data3(self, polygons, photos, total):

        dicio_view_object = {

            "Poligonos (x0,50)": ft.Text(value=f"{polygons}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Fotos 360 (x0,20)": ft.Text(value=f"{photos}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            "Total": ft.Text(value=f"R$ {total}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
        }

        return dicio_view_object