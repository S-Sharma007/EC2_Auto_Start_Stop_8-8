import json
from Start_instance import lambda_handler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load test event
with open('test_event.json', 'r') as f:
    test_event = json.load(f)

# Test the lambda function
response = lambda_handler(test_event, None)
print(json.dumps(response, indent=2))