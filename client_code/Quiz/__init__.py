rom ._anvil_designer import QuizTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Quiz(QuizTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # print(project)
    self.question1.text=question

    # Any code you write here will run before the form opens.

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    passpasspass

  def radio_button_1_copy_6_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass


