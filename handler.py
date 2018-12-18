import json
import logging
import re


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello_endpoint(event, context):
  logger.info(event)
  
  body = {
    "message": "Hello world!"
  }

  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }

  return response

def sum_endpoint(event, context):
  logger.info(event)

  # Default response
  body = {
    "error": "Please provide at least one number e.g. numbers=1,2,3"
  }

  if 'body' in event and event['body'] is not None:
    # Regex that matches "numbers=1,2,33"
    r = re.compile("^numbers=([-+]?([1-9]\\d*|0),?)+$")
    # Get numbers from post data
    numbers = list(filter(r.match, event['body'].split('&')))
    if len(numbers) > 0:
      numbers = numbers[0].replace('numbers=', '')
      numbers = numbers.split(',')
      body = {
        "sum": sum(map(int, numbers))
      }

  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }

  return response