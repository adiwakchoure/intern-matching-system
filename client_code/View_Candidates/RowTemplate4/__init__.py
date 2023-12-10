from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    try:
      score = app_tables.answers.get(student_id=self.item['uid'])['score']
      self.score_label.text = f"{(score/12)*100:.2f}%"
    except:
      self.score_label.text = "N/A"
    

    # Any code you write here will run before the form opens.

  def resumedownload_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
