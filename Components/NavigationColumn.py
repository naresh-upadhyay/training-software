import pprint
from datetime import datetime

import flet as ft
from Models.NavigationItem import NavigationItem


class NavigationColumn(ft.Column):
    def __init__(self, mainPageData):
        super().__init__()
        self.expand = 4
        self.spacing = 0
        self.scroll = ft.ScrollMode.ALWAYS
        self.width = 200
        self.mainPageData = mainPageData
        self.selected_index = 0
        self.controls = self.get_navigation_items()

    def before_update(self):
        super().before_update()
        self.update_selected_item()

    def get_navigation_items(self):
        navigation_items = []
        for destination in self.mainPageData.control_groups:
            navigation_items.append(
                NavigationItem(destination, item_clicked=self.item_clicked)
            )
        return navigation_items

    def item_clicked(self, e):
        self.selected_index = e.control.destination.index
        self.update_selected_item()
        self.page.go(f"/{e.control.destination.name}")

    def update_selected_item(self):
        for item in self.controls:
            item.bgcolor = None
            item.content.controls[0].name = item.destination.icon
        self.controls[self.selected_index].bgcolor = ft.Colors.SECONDARY_CONTAINER
        self.controls[self.selected_index].content.controls[0].name = self.controls[
            self.selected_index
        ].destination.selected_icon


