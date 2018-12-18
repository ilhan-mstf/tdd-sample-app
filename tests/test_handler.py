import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import handler

def test_hello_endpoint():
  expected_result = {
    "statusCode": 200,
    "body": "{\"message\": \"Hello world!\"}"
  }
  assert handler.hello_endpoint(None, None) == expected_result

def test_sum_endpoint_numbers():
  event = {
    "body": "numbers=1,2"
  }
  expected_result = {
    "statusCode": 200,
    "body": "{\"sum\": 3}"
  }
  assert handler.sum_endpoint(event, None) == expected_result

def test_sum_endpoint_many_numbers():
  event = {
    "body": "numbers=1,2,34"
  }
  expected_result = {
    "statusCode": 200,
    "body": "{\"sum\": 37}"
  }
  assert handler.sum_endpoint(event, None) == expected_result

def test_sum_endpoint_nobody():
  event = {
  }
  expected_result = {
    "statusCode": 200,
    "body": "{\"error\": \"Please provide at least one number e.g. numbers=1,2,3\"}"
  }
  assert handler.sum_endpoint(event, None) == expected_result

def test_sum_endpoint_string():
  event = {
    "body": "numbers=asdas,1,2"
  }
  expected_result = {
    "statusCode": 200,
    "body": "{\"error\": \"Please provide at least one number e.g. numbers=1,2,3\"}"
  }
  assert handler.sum_endpoint(event, None) == expected_result

def test_sum_endpoint_nonumbers():
  event = {
    "body": "nuasdambers=1,2"
  }
  expected_result = {
    "statusCode": 200,
    "body": "{\"error\": \"Please provide at least one number e.g. numbers=1,2,3\"}"
  }
  assert handler.sum_endpoint(event, None) == expected_result