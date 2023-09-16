from ._anvil_designer import QuizTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Quiz(QuizTemplate):
  def __init__(self, student_id='0650006c-13ce-7ff8-8000-12500edbb856', **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.student_id = student_id
    # candidate_row = app_tables.candidates.get(uid=student_id)
    # print(candidate_row)
    # print(student_id)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_2.text=dict(app_tables.candidates.get(uid=self.student_id))["skills"]
    pass


