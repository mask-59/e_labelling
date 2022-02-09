import requests
import os
from dotenv import load_dotenv
load_dotenv()
def hcases():
    # print('getting hourly for all lines Labelling')
    # print('---------------')
    url = os.getenv('GET_HCASES_URL') 
    x = requests.get(url)
    # print(x.text)
    # print('---------------')
    return (x.text)

    # return '{"data": [{"hr": 6,"line": "L6","cans": 4551,"cases": 189,"config_id": 2208}, {"hr": 6,"line": "L6","cans": 4551,"cases": 189,"config_id": 2208}, {"hr": 7,"line": "L6","cans": 6020,"cases": 250,"config_id": 2208}]}'