import flet as ft

class DataColumns(ft.DataColumn):
    def __init__(self, columnData):
        super().__init__()
        self.columnData = columnData
        self.isSorted = columnData.isSorted #Sorting will be one column at a time.
        self.columnImage = columnData.columnImage
        self.columnText = columnData.columnText
        self.isCheckbox = columnData.isCheckbox
        self.isSelected = columnData.isSelected
        self.isAccending = columnData.isAccending

