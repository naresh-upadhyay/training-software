
import flet as ft


from Components.MainPageView import MainPageView
from Components.MainPageData import MainPageData

def main(page: ft.Page):
    page.title = "Training software"
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
        "RobotoSlab": "RobotoSlab[wght].ttf",        
    }
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.AppBar(
        leading= ft.Icon(ft.Icons.PALETTE),
        leading_width = 10,
        title=ft.Text("Training Software Offcampuscareer",
            style=ft.TextStyle(size=16, height=.2)),
        center_title=True,
        bgcolor=ft.Colors.INVERSE_PRIMARY,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)
        ],
        toolbar_height = 40
    )

    #page.horizontal_alignment = ft.CrossAxisAlignment.START
    #page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "adaptive"

    mainPageData = MainPageData()
    main_page = MainPageView(mainPageData)

    # Define routes and their corresponding page functions
    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            page.go("/dashboard")
        else:
            # gallery.selected_control_group = gallery.get_control_group(route_list[0])
            if len(route_list) == 1:
                main_page.display_controls_grid(route_list[0])
            #elif len(route_list) == 2:
                #gallery_view.display_control_examples(route_list[0], route_list[1])
            else:
                print("Invalid route")

    page.on_route_change = route_change
    page.add(main_page)
    main_page.resize(page)
    #page.add(ft.Text("Body"))
    page.on_resized = lambda e: main_page.resize(page)  # Calls resize when window is resized


ft.app(port=8082, target=main, view=ft.WEB_BROWSER)