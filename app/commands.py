import click
from flask import Flask
from json.decoder import JSONDecodeError
import logging
import logger_config
from datetime import datetime
import re
import json


def register_cli(app: Flask):

  @app.cli.command('get-experience')
  def get_experience():

    result = {}

    try:
      file = open('data.json')
    except IOError as e:
      app.logger.error(e)
      # Return 404 response
      print('The file you requested was not found.')

    try:
      data = json.load(file)
    except (AttributeError, JSONDecodeError) as e:
      app.logger.error(e)
      # Return 500 response
      print('The file you requested could not be loaded.')

    if 'skills' in data:
      result['skills'] = data['skills'].split(', ')

    if 'experience' in data:
      result['experience'] = {}
      for company in data['experience']:
        result['experience'][company] = data['experience'][company].splitlines()

    print(result)


  @app.cli.command('get-personal-details')
  def get_personal_details():

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
      print('The file you requested was not found.')

    try:
      data = json.load(file)
    except (AttributeError, JSONDecodeError) as e:
      app.logger.error(e)
      print('The file you requested could not be loaded.')

    # Discard CVs that do not have a name and surname
    if 'name' not in data and 'surname' not in data:
      print('The CV is incomplete.')

    if 'name' in data:
      result['fullName'] = f'{data["name"]} '

    if 'surname' in data:
      result['fullName'] = f'{result["fullName"]}{data["surname"]}'
    else:
      result['fullName'] = result['fullName'].strip(' ')

    for key in fast_forward_keys:
      if key in data:
        result[key] = data[key]

    print(result)


  @app.cli.command('get-education')
  def get_education():
    result = {}

    try:
      file = open('data.json')
    except IOError as e:
      print('The file you requested was not found.')
      app.logger.error(e)

    try:
      data = json.load(file)
    except (AttributeError, JSONDecodeError) as e:
      app.logger.error(e)
      print('The file you requested could not be loaded.')

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

    print(result)

