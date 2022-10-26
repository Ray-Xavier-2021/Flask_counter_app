# FILE IS A COPY FROM REPLIT COUNTER APP - RUN APP.py ON LOCAL MACHINE

import counter_app
from counter_app import home_page, app, show, db

# root => '/'
# increment path => '/increment'
# decrement path => '/decrement'

# database = {'number': 0}

@app.route('/')
def home():
  return show(page=home_page, number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return show(page=home_page, number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return show(page=home_page, number=db['number'])
  return 'decrement'


app.run(host='0.0.0.0', port=81)