
class ControlGroup:
    def __init__(self, name, label, icon, selected_icon, index):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.index = index
        self.grid_items = []