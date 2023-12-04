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
          # Prepare the updated options, using text box values if non-empty, otherwise label text
          updated_options = [
              {'option': self.text_box_1.text if self.text_box_1.text else self.label_1.text, 'is_correct': self.check_box_1.checked},
              {'option': self.text_box_2.text if self.text_box_2.text else self.label_2.text, 'is_correct': self.check_box_2.checked},
              {'option': self.text_box_3.text if self.text_box_3.text else self.label_3.text, 'is_correct': self.check_box_3.checked},
              {'option': self.text_box_4.text if self.text_box_4.text else self.label_4.text, 'is_correct': self.check_box_4.checked}
          ]

          # Update the question text, using text box value if non-empty, otherwise label text
          updated_question = self.text_box_5.text if self.text_box_5.text else self.label_5.text

          # Update the question record with new question text and options
          current_question.update(question=updated_question, options=updated_options)

          # Update UI to reflect changes immediately
          self.label_5.text = updated_question
          for i, option in enumerate(updated_options):
              getattr(self, f'label_{i+1}').text = option['option']
              getattr(self, f'check_box_{i+1}').checked = option['is_correct']

          alert("Saved your edits!")
      else:
          alert("Error: Question not found.")