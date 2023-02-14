from flask import Flask, render_template, make_response
from commands import register_cli
import json
from json.decoder import JSONDecodeError
import logging
import logger_config
from datetime import datetime
import re

app = Flask(__name__)
register_cli(app)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/personal')
def personal():

  result = {}
  result['fullName'] = ''
  fast_forward_keys = [
    'phone',
    'hobbies',
    'country',
    'dateOfBirth',
    'languages',
    'address'
  ]

  try:
    file = open('data.json')
  except IOError as e:
    app.logger.error(e)
    # Return 404 page or json object
    return make_response({
      'status': 404,
      'message': 'The file you requested was not found.'
    })
    # return render_template('file_issue.html',
    #                        message = 'The file you requested was not found.'), 404
  try:
    data = json.load(file)
  except (AttributeError, JSONDecodeError) as e:
    app.logger.error(e)
    # Return 500 page or json object
    return make_response({
      'status': 500,
      'message': 'The file you requested could not be loaded.'
    })
    # return render_template('file_issue.html',
    #                        message = 'The file could not be loaded.'), 500


  # Discard CVs that do not have a name and surname
  if 'name' not in data and 'surname' not in data:
    # Return 500 page or json object
    return make_response({
      'status': 500,
      'message': 'The CV is incomplete.'
    })
    # return render_template('file_issue.html',
    #                        message = 'The CV is incomplete.'), 500

  if 'name' in data:
    result['fullName'] = f'{data["name"]} '

  if 'surname' in data:
    result['fullName'] = f'{result["fullName"]}{data["surname"]}'
  else:
    result['fullName'] = result['fullName'].strip(' ')

  for key in fast_forward_keys:
    if key in data:
      result[key] = data[key]

  return result

@app.route('/experience')
def experience():

  result = {}

  try:
    file = open('data.json')
  except IOError as e:
    app.logger.error(e)
    # Return 404 response
    return make_response({
      'status': 404,
      'message': 'The file you requested was not found.'
    })

  try:
    data = json.load(file)
  except (AttributeError, JSONDecodeError) as e:
    app.logger.error(e)
    # Return 500 response
    return make_response({
      'status': 500,
      'message': 'The file you requested could not be loaded.'
    })

  if 'skills' in data:
    result['skills'] = data['skills'].split(', ')

  if 'experience' in data:
    result['experience'] = {}
    for company in data['experience']:
      result['experience'][company] = data['experience'][company].splitlines()

  return result

@app.route('/education')
def education():
  result = {}

  try:
    file = open('data.json')
  except IOError as e:
    app.logger.error(e)
    # Return 404 response
    return make_response({
      'status': 404,
      'message': 'The file you requested was not found.'
    })

  try:
    data = json.load(file)
  except (AttributeError, JSONDecodeError) as e:
    app.logger.error(e)
    # Return 500 response
    return make_response({
      'status': 500,
      'message': 'The file you requested could not be loaded.'
    })

  if 'education' in data:
    result['education'] = {}
    for education in data['education']:
      # Search if the graduation date exists
      search_string = re.search(r'([a-zA-z\s]*\d{4})', education)

      if not search_string:
        continue

      date_of_graduation = datetime.strptime(search_string.group(1), "%B %Y")
      formatted_date_of_graduation = date_of_graduation.strftime('%d-%m-%Y')
      institution = re.split(r'([a-zA-z\s]*\d{4})', education)[2].strip()
      result['education'][formatted_date_of_graduation] = institution

  return result


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)