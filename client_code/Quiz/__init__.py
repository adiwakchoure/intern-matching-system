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
  def __init__(self, student_id='06517cd7-055a-712e-8000-ac402eeb31af', **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.student_id = student_id
    # candidate_row = app_tables.candidates.get(uid=student_id)
    # print(candidate_row)
    # print(student_id)
    # Any code you write here will run before the form opens.
    total_time = 15
    alert(f"You have a total of {total_time} seconds to answer 3 the questions. There may be multiple right answers each. The quiz will auto-submit in {total_time} seconds")

    skills = dict(app_tables.candidates.get(uid=self.student_id))["skills"]
    pid = anvil.server.call('project_search', "skills", str(skills))
    self.questions_data = app_tables.questions.search(pid=pid)

    self.question1.text = self.questions_data[0]['question']
    self.r11.text = self.questions_data[0]['options'][0]['option']
    self.r12.text = self.questions_data[0]['options'][1]['option']
    self.r13.text = self.questions_data[0]['options'][2]['option']
    self.r14.text = self.questions_data[0]['options'][3]['option']

    self.question2.text = self.questions_data[1]['question']
    self.r21.text = self.questions_data[1]['options'][0]['option']
    self.r22.text = self.questions_data[1]['options'][1]['option']
    self.r23.text = self.questions_data[1]['options'][2]['option']
    self.r24.text = self.questions_data[1]['options'][3]['option']

    self.question3.text = self.questions_data[2]['question']
    self.r31.text = self.questions_data[2]['options'][0]['option']
    self.r32.text = self.questions_data[2]['options'][1]['option']
    self.r33.text = self.questions_data[2]['options'][2]['option']
    self.r34.text = self.questions_data[2]['options'][3]['option']

    self.time_remaining = 20

  def submit_click(self, **event_args):
    score = 0
    # Check answer for question 1
    if self.r11.checked == self.questions_data[0]['options'][0]['is_correct']:
        score += 1
    if self.r12.checked == self.questions_data[0]['options'][1]['is_correct']:
        score += 1
    if self.r13.checked == self.questions_data[0]['options'][2]['is_correct']:
        score += 1
    if self.r14.checked == self.questions_data[0]['options'][3]['is_correct']:
        score += 1

    # Check answer for question 2
    if self.r21.checked == self.questions_data[1]['options'][0]['is_correct']:
        score += 1
    if self.r22.checked == self.questions_data[1]['options'][1]['is_correct']:
        score += 1
    if self.r23.checked == self.questions_data[1]['options'][2]['is_correct']:
        score += 1
    if self.r24.checked == self.questions_data[1]['options'][3]['is_correct']:
        score += 1

    # Check answer for question 3
    if self.r31.checked == self.questions_data[2]['options'][0]['is_correct']:
        score += 1
    if self.r32.checked == self.questions_data[2]['options'][1]['is_correct']:
        score += 1
    if self.r33.checked == self.questions_data[2]['options'][2]['is_correct']:
        score += 1
    if self.r34.checked == self.questions_data[2]['options'][3]['is_correct']:
        score += 1

    response = []

    question1_response = {
        'question_id': self.questions_data[0]['uid'],
        'responses': [
            self.r11.checked,
            self.r12.checked,
            self.r13.checked,
            self.r14.checked
        ]
    }
    response.append(question1_response)

    # Check answer for question 2
    question2_response = {
        'question_id': self.questions_data[1]['uid'],
        'responses': [
            self.r21.checked,
            self.r22.checked,
            self.r23.checked,
            self.r24.checked
        ]
    }
    response.append(question2_response)

    # Check answer for question 3
    question3_response = {
        'question_id': self.questions_data[2]['uid'],
        'responses': [
            self.r31.checked,
            self.r32.checked,
            self.r33.checked,
            self.r34.checked
        ]
    }
    response.append(question3_response)

    app_tables.answers.add_row(
      student_id=self.student_id,
      score = score,
      response = response
      )
     # Stop the timer when manually submitting
    open_form('Result',score=score)

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.time_remaining -= 1
    if self.time_remaining <= 0:
        self.submit_click()  # Submit the quiz when time is up
    pass

  


  



