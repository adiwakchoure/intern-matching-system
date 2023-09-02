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
    if uploaded_file is not None:
    # Call the server function and pass the uploaded file
      print("Sending")
      self.markdown.content = anvil.server.call('process_pdf', uploaded_file)

  def resume_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

