import flet as ft
from Components.TableView import TableView


class ComponentMapping:
    def __init__(self):
        self.components = {
            "dashboard": TableView(),
            "candidates": ft.Text("king upadhyay"),
        }

    def addComponent(self, key, value):
        self.components[key] = value

    def getComponent(self, key):
        return self.components[key]

    def removeComponent(self, key):
        if key in self.components:
            del self.components[key]

    def __repr__(self):
        return str(self.components)



