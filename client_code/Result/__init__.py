from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Result(ResultTemplate):
  def __init__(self, score = 7, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.score = score
    # Any code you write here will run before the form opens.
    result = f"Score: {self.score} out of 12"
    self.result.text = result

