from ._anvil_designer import Add_ProjectsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import re
import time

def go_to_admin_page(self, **event_args):
  user = anvil.users.login_with_form()
  if user is not None and user['email']=="admin@admin.com":
    open_form('Admin')

class Add_Projects(Add_ProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def admin_view_click(self, **event_args):
    user = anvil.users.login_with_form()
    if user is not None and user['confirmed_email']:
      open_form('Admin')

  def submit_click(self, **event_args):
    user = anvil.users.get_user()
    email = user['email']
    uploaded_file = self.doc.file
    if self.title_box.text is None or self.title_box.text == "":
      self.markdown.content = "Please Enter a valid Title."
    elif uploaded_file is None:
      self.markdown.content = "Please Upload a Brief (docx)."
    else:
    # if self.name_box.text is not None and self.name_box.text is not None:
      user = anvil.users.get_user()
      api_key = user['api_key']
      processed_data = anvil.server.call('process_project', self.title_box.text,self.instructions_box.text, uploaded_file, api_key)
      # Add the processed data to the 'Candidates' data table
      app_tables.projects.add_row(
        uid=processed_data.get('uid', ''),
        title=processed_data.get('title', ''),
        instructions=processed_data.get('instructions', ''),
        doc = uploaded_file,
        skills=processed_data.get('skills', '[]'),  # Store as a JSON string
        domains=processed_data.get('domains', '[]'),  # Store as a JSON string
        allotted=False,
        owner = email
      )
      print(processed_data)
      
      self.markdown.content = "Submitted!"
      time.sleep(2)
      open_form('Admin')

  def resume_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass
