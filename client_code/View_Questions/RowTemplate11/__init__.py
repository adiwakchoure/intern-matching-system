from ._anvil_designer import RowTemplate11Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate11(RowTemplate11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Assuming self.item structure is something like:
    # {'question': 'What is ...?', 'options': [{'option': 'Option 1'}, {'option': 'Option 2'}, {'option': 'Option 3'}, {'option': 'Option 4'}]}

    # Bind the question text box to the question
    self.column_1.text = self.item['question']

    # Bind the option text boxes to the respective options
    # self.option_1_text_box.text = self.item['options'][0]['option']
    # self.option_2_text_box.text = self.item['options'][1]['option']
    # self.option_3_text_box.text = self.item['options'][2]['option']
    # self.option_4_text_box.text = self.item['options'][3]['option']
