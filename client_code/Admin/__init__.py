from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_projects_click(self, **event_args):
    open_form('Add_Projects')

  def view_projects_click(self, **event_args):
    open_form('View_Projects')

  def view_candidates_click(self, **event_args):
    open_form('View_Candidates')











