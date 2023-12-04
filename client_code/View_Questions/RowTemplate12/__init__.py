from ._anvil_designer import RowTemplate12Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate12(RowTemplate12Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.label_5.text = self.item['question']

    self.label_1.text = self.item['options'][0]['option']
    self.check_box_1.text = "Correct"
    self.check_box_1.checked = self.item['options'][0]['is_correct']
    
    self.label_2.text = self.item['options'][1]['option']
    self.check_box_2.text = "Correct"
    self.check_box_2.checked = self.item['options'][1]['is_correct']
    
    self.label_3.text = self.item['options'][2]['option']
    self.check_box_3.text = "Correct"
    self.check_box_3.checked = self.item['options'][2]['is_correct']
    
    self.label_4.text = self.item['options'][3]['option']
    self.check_box_4.text = "Correct"
    self.check_box_4.checked = self.item['options'][3]['is_correct']



  def save_button_click(self, **event_args):
    """This method is called when the save button is clicked"""

    # Fetch the question record using its uid
    current_question = app_tables.questions.get(uid=self.item['uid'])

    if current_question:
      # Update the options based on the current state of the checkboxes and labels
      updated_options = [
          {'option': self.label_1.text, 'is_correct': self.check_box_1.checked},
          {'option': self.label_2.text, 'is_correct': self.check_box_2.checked},
          {'option': self.label_3.text, 'is_correct': self.check_box_3.checked},
          {'option': self.label_4.text, 'is_correct': self.check_box_4.checked}
      ]

      # Update the question record with new options
      current_question.update(question=self.label_5.text, options=updated_options)

      alert("Saved your edits!")
    else:
        alert("Error: Question not found.")