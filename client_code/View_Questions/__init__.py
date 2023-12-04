from ._anvil_designer import View_QuestionsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class View_Questions(View_QuestionsTemplate):
  def __init__(self, pid="06517c81-594b-724c-8000-0bec7b6385db", **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # alert(pid)
    rows_data = app_tables.questions.search(pid=pid)
    self.repeating_panel_1.items = rows_data
    # alert()
    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("View_Projects")
    pass

