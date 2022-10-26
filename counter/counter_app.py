from flask import Flask, render_template_string, url_for
# from replit import db

app = Flask(__name__)

# Local dummy database
db = {'number': 0}

if 'number' not in db:
  db['number'] = 0

# HTML in Python File:
home_page = '''
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    
    <span>{{ number }}</span>
    <div>
    <form action="/decrement">
      <button id='increment'>-</button>
    </form>
    <form action="/increment">
      <button id='decrement'>+</button>
    </form>
    </div>
    '''

def show(page=home_page, number=0):
  return render_template_string(home_page, number=number)