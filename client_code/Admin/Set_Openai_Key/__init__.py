from ._anvil_designer import Set_Openai_KeyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Set_Openai_Key(Set_Openai_KeyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.key_text.text = anvil.users.get_user()['api_key']
    # Any code you write here will run before the form opens.

  def setKey_click(self, **event_args):
    """This method is called when the button is clicked"""
      # Retrieve the text from key_text component

    user = anvil.users.get_user()  # Get the current logged-in user
    if user:
        keyText = self.key_text.text
        user.update(api_key=keyText)  # Update the api_key field of the user record
        alert(f"Your key is updated!")
    else:
        alert("No user is currently logged in.", title="Error")



  def button_1_click(self, **event_args):
    open_form('Admin')
