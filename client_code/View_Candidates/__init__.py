open_form('Admin')from ._anvil_designer import View_CandidatesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class View_Candidates(View_CandidatesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def admin_view_click(self, **event_args):
    open_form('Admin')open_form('Admin')

