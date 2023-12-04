from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from ..Quiz import Quiz
import re

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
    # if not user['confirmed_email']:
    #   alert("Please confirm registration via email!")
    # if user is not None and user['confirmed_email']:
    #   open_form('Admin')
    if user is not None:
      open_form('Admin')

  def submit_click(self, **event_args):
    uploaded_file = self.resume.file
    if self.name_box.text is None or self.name_box.text == "":
      self.markdown.content = "Please Enter a valid Name."
    elif self.email_box.text is None or self.email_box.text == "" or not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_box.text):
      self.markdown.content = "Please Enter a valid E-mail."
    elif uploaded_file is None:
      self.markdown.content = "Please Upload your Resume."
    elif self.name_box.text is None and self.name_box.text is None:
      self.markdown.content = "Please Enter your Details."
    else:
    # if self.name_box.text is not None and self.name_box.text is not None:
      processed_data = anvil.server.call('process_candidate', self.name_box.text, self.email_box.text, uploaded_file)
      print(processed_data)
      # Add the processed data to the 'Candidates' data table
      app_tables.candidates.add_row(
        name=self.name_box.text,
        email=self.email_box.text,
        passout=int(processed_data.get('passout', '')),
        uid=processed_data.get('uid', ''),
        university=processed_data.get('university', ''),
        resume = uploaded_file,
        skills=processed_data.get('skills', '[]'),  # Store as a JSON string
        domains=processed_data.get('domains', '[]'),  # Store as a JSON string
        allotted=False
      )
      uploaded = anvil.server.call('upload_candidate', processed_data)
      print(uploaded)
      self.markdown.content = "Submitted!"
      open_form('Quiz',student_id=processed_data["uid"])
      
  
  def resume_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

