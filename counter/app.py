from flask import Flask, render_template_string

app = Flask(__name__)

# root => '/'
# counter app path => '/counter'
# increment path => '/increment'
# decrement path => '/decrement'

db = {'number': 0}

if 'number' not in db:
  db['number'] = 0

# HTML & CSS IN PYTHON:
html = '''
<div style='display: flex'>
  <div style='margin: auto; text-align: center'>
    <h1>{{ title }}</h1>
    <input type='text' placeholder='Enter your name' />
    <input type='submit' />
    <p>Welcome to my counter app!</p>
    <form action='/counter' >
      <button>Take me to app!</button>
    </form>
  </div>
</div>
'''
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


@app.route('/')
def home():
  return render_template_string(html, title='Flask Counter App')

@app.route('/counter')
def counter():
  return render_template_string(home_page, number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return render_template_string(home_page, number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return render_template_string(home_page, number=db['number'])

# Replit port
# app.run(host='0.0.0.0', port=81)

# Local laptop
app.run(debug=True)