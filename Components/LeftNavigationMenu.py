import flet as ft
from Components.NavigationColumn import NavigationColumn
from Models.PopupColorItem import PopupColorItem


class LeftNavigationMenu(ft.Column):
    def __init__(self, mainPageData):
        super().__init__()
        self.mainPageData = mainPageData
        self.alignment = ft.MainAxisAlignment.START
        self.cross_axis_alignment = ft.CrossAxisAlignment.START  # Align the children vertically to the top


        self.rail = NavigationColumn(mainPageData=mainPageData)

        self.dark_light_text = ft.Text("Light theme")
        self.dark_light_icon = ft.IconButton(
            icon=ft.Icons.BRIGHTNESS_2_OUTLINED,
            tooltip="Toggle brightness",
            on_click=self.theme_changed,
        )

        self.controls = [
            self.rail,
            ft.Column(
                expand=1,
                controls=[
                    ft.Row(
                        controls=[
                            self.dark_light_icon,
                            self.dark_light_text,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.PopupMenuButton(
                                icon=ft.Icons.COLOR_LENS_OUTLINED,
                                items=[
                                    PopupColorItem(
                                        color="deeppurple", name="Deep purple"
                                    ),
                                    PopupColorItem(color="indigo", name="Indigo"),
                                    PopupColorItem(color="blue", name="Blue (default)"),
                                    PopupColorItem(color="teal", name="Teal"),
                                    PopupColorItem(color="green", name="Green"),
                                    PopupColorItem(color="yellow", name="Yellow"),
                                    PopupColorItem(color="orange", name="Orange"),
                                    PopupColorItem(
                                        color="deeporange", name="Deep orange"
                                    ),
                                    PopupColorItem(color="pink", name="Pink"),
                                ],
                            ),
                            ft.Text("Seed color"),
                        ]
                    ),
                ],
            ),
        ]

    def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.dark_light_text.value = "Dark theme"
            self.dark_light_icon.icon = ft.Icons.BRIGHTNESS_HIGH
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.dark_light_text.value = "Light theme"
            self.dark_light_icon.icon = ft.Icons.BRIGHTNESS_2
        self.page.update()
