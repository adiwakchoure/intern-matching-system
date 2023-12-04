from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate7(RowTemplate7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('View_Questions',pid=self.item['uid'])
    pass

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # Confirm before deleting
    if confirm("Are you sure you want to delete this project?"):
      # Fetch the project record using its uid
      project_to_delete = app_tables.projects.get(uid=self.item['uid'])

      if project_to_delete:
        # Delete the project record
        project_to_delete.delete()
  
        alert("Project deleted successfully!")
  
        # Optionally, refresh the data or redirect to another form if needed
        open_form('View_Projects')
      else:
        alert("Error: Project not found.")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('View_Questions',pid=self.item['uid'])
    pass
