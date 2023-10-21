# from ._anvil_designer import View_CandidatesTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class View_Candidates(View_CandidatesTemplate):
#   def __init__(self, **properties):
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.

#   def admin_view_click(self, **event_args):
#     open_form('Admin')

from ._anvil_designer import View_ProjectsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class View_Projects(View_ProjectsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Fetch all records from the 'candidates' table
    # candidates_data = app_tables.candidates.search()
    # Set the 'items' property of the Data Grid to the fetched data
    # self.grid.items = anvil.server.call('get_candidates')
    self.griddata.items = anvil.server.call('get_all_projects')

  def admin_view_click(self, **event_args):
    open_form('Admin')
