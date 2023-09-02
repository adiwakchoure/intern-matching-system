from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

def go_to_admin_page(self, **event_args):
        user = anvil.users.login_with_form()
        if user is not None and user['email']=="admin@admin.com":
            open_form('Admin')

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def admin_view_click(self, **event_args):
    user = anvil.users.login_with_form()
    if user is not None and user['confirmed_email']:
      open_form('Admin')

  def submit_click(self, **event_args):
    uploaded_file = self.resume.file
    if self.name_box.text is None or self.name_box.text == "":
      self.markdown.content = "Please Enter your Name."
    elif uploaded_file is None:
      self.markdown.content = "Please Upload your Resume."
    elif self.name_box.text is None and self.name_box.text is None:
      self.markdown.content = "Please Enter your Details."
    else:
    # if self.name_box.text is not None and self.name_box.text is not None:
      anvil.server.call('process_candidate', self.name_box.text, uploaded_file)
      self.markdown.content = "Submitted!"
  
  def resume_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

