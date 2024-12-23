import flet as ft


class DataTableApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.data = [
            {"id": i, "name": f"User {i}", "age": 20 + (i % 10)}
            for i in range(1, 101)
        ]
        self.rows_per_page = 10
        self.current_page = 1
        self.selected_rows = set()
        self.select_all = False

    def build(self):
        """Build the Flet UI and return the root control."""
        # Create the "Select All" checkbox in the header
        select_all_checkbox = ft.Checkbox(
            label="Select All",
            value=self.select_all,
            on_change=self.select_all_changed,
        )

        # Create the DataTable with columns
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(select_all_checkbox),
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("Age")),
                ft.DataColumn(ft.Text("Actions")),
            ],
            rows=self.get_table_rows(),  # Set the initial rows
            #width=500  # Adjust the width if necessary
        )

        # Create a Scrollable container for the DataTable
        scrollable_table = ft.Column(
            controls=[self.data_table],
            height=300,  # Set a fixed height for scrolling
            scroll=True,  # Enable scrolling
        )

        # Pagination controls
        pagination_controls = ft.Row(
            controls=[
                ft.ElevatedButton("Previous", on_click=self.go_to_previous_page),
                ft.Text(f"Page {self.current_page} of {self.total_pages()}", size=16),
                ft.ElevatedButton("Next", on_click=self.go_to_next_page),
                ft.ElevatedButton("Delete Selected", on_click=self.delete_selected_rows),
                # Button to delete selected rows
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # Return the container with the scrollable table and pagination controls
        return ft.Column(
            controls=[scrollable_table, pagination_controls],
            spacing=10,
        )

    def get_table_rows(self):
        """Generate the rows for the table."""
        rows = []
        start = (self.current_page - 1) * self.rows_per_page
        end = start + self.rows_per_page
        for row in self.data[start:end]:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Checkbox(
                                on_change=self.checkbox_changed,
                                value=row["id"] in self.selected_rows,
                            )
                        ),
                        ft.DataCell(ft.Text(str(row["id"]))),
                        ft.DataCell(ft.Text(row["name"])),
                        ft.DataCell(ft.Text(str(row["age"]))),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, row=row: self.edit_row(row)),
                                    ft.IconButton(icon=ft.icons.DELETE,
                                                  on_click=lambda e, row=row: self.delete_row(row)),
                                ],
                                spacing=10,
                            )
                        ),
                    ]
                )
            )
        return rows

    def checkbox_changed(self, e):
        """Handle individual checkbox state change."""
        row_id = e.control.value
        if row_id in self.selected_rows:
            self.selected_rows.remove(row_id)
        else:
            self.selected_rows.add(row_id)

        # Update the "Select All" checkbox state
        if len(self.selected_rows) == len(self.get_rows_for_page()):
            self.select_all = True
        else:
            self.select_all = False

        # If no rows are selected, uncheck the "Select All" checkbox
        if not self.selected_rows:
            self.select_all = False

        self.update_table()

    def select_all_changed(self, e):
        """Handle "Select All" checkbox state change."""
        self.select_all = e.control.value
        if self.select_all:
            self.selected_rows = set(row["id"] for row in self.get_rows_for_page())
        else:
            self.selected_rows = set()

        self.update_table()

    def edit_row(self, row):
        print(f"Edit: {row}")

    def delete_row(self, row):
        """Delete a single row."""
        self.data = [r for r in self.data if r["id"] != row["id"]]
        self.selected_rows.discard(row["id"])  # Remove from selection if deleted
        self.update_table()
        self.adjust_page_after_deletion()

    def delete_selected_rows(self, e):
        """Delete all selected rows."""
        self.data = [r for r in self.data if r["id"] not in self.selected_rows]
        self.selected_rows.clear()  # Clear selected rows after deletion
        self.select_all = False  # Uncheck "Select All" when all selected rows are deleted
        self.update_table()
        self.adjust_page_after_deletion()

    def adjust_page_after_deletion(self):
        """Adjust page and re-calculate total pages after deletion."""
        total_pages = self.total_pages()

        # If current page exceeds total pages, go to the last page
        if self.current_page > total_pages:
            self.current_page = total_pages

        self.update_table()

    def go_to_previous_page(self, e):
        """Handle page change to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()

    def go_to_next_page(self, e):
        """Handle page change to the next page."""
        if self.current_page < self.total_pages():
            self.current_page += 1
            self.update_table()

    def total_pages(self):
        """Calculate the total number of pages based on data size."""
        return (len(self.data) + self.rows_per_page - 1) // self.rows_per_page

    def get_rows_for_page(self):
        """Get rows for the current page."""
        start = (self.current_page - 1) * self.rows_per_page
        end = start + self.rows_per_page
        return self.data[start:end]

    def update_table(self):
        """Update the rows after actions like delete or checkbox change."""
        self.data_table.rows = self.get_table_rows()
        self.update()
