import flet as ft
from Components.ComponentMapping import ComponentMapping
from Components.LeftNavigationMenu import LeftNavigationMenu


class MainPageView(ft.Row):
    def __init__(self, mainPageData):
        super().__init__()

        self.mainPageData = mainPageData
        self.leftNavigation = LeftNavigationMenu(mainPageData)
        self.rightPage = ComponentMapping()

        # Container for left navigation
        self.leftNavigationContainer = ft.Container(
            content=self.leftNavigation,
            padding=10,  # Add some padding inside the border
            alignment=ft.alignment.top_left,  # Align content to the top-left
        )

        # Right page container
        self.rightPageContainer = ft.Container(
            content=self.rightPage.getComponent("dashboard"),
            padding=10,  # Add some padding inside the border
            alignment=ft.alignment.top_left,  # Align content to the top-left
        )

        # Setting controls and alignment
        self.controls = self.getFullScreenData()
        self.alignment = ft.MainAxisAlignment.START  # Align items horizontally to start
        self.vertical_alignment = ft.CrossAxisAlignment.START  # Align items vertically to start

    def resize(self, window):
        # Get the window size when it's resized
        window_width = window.width  # Use window.width to get the width
        window_height = window.height  # Use window.height to get the height
        print(window_width, window_height)

        # Update left navigation width to 20% of the window width
        left_navigation_width = window_width * 0.2
        self.leftNavigationContainer.width = left_navigation_width  # Update the width of the container
        self.leftNavigationContainer.height = window_height * 0.8  # Update the height of the container
        self.update()  # Refresh the layout to reflect the change

    def getFullScreenData(self):
        fullScreenData = [
            self.leftNavigationContainer,
            ft.VerticalDivider(width=1),
            self.rightPageContainer,
        ]
        return fullScreenData

    def display_controls_grid(self, control_group_name):
        self.rightPageContainer.content = self.rightPage.getComponent(control_group_name)
        self.controls = self.getFullScreenData()
        self.page.update()

