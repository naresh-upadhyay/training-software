import flet as ft
from Models.ControlGroup import ControlGroup
    
class MainPageData:
    def __init__(self):
        self.control_groups = [
            ControlGroup(
                name="dashboard",
                label="Dashboard",
                icon=ft.Icons.GRID_VIEW,
                selected_icon=ft.Icons.GRID_VIEW_SHARP,
                index=0
            ),
            ControlGroup(
                name="candidates",
                label="Candidates",
                icon=ft.Icons.PERSON_PIN,
                selected_icon=ft.Icons.PERSON_PIN_SHARP,
                index=1
            )
        ]    