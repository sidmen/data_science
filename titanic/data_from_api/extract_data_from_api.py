import requests

url = 'https://api.data.gov/ed/collegescorecard/v1/schools?school.name=boston%20college&api_key=HncIBfzmqVYOY7vYivmV1XEDUPhmKtGZbackX9wl'
# the api_key is got from api.data.gov

result = requests.get(url)

status = result.status_code

result_in_text_format = result.text

result_in_json_format = result.json

print(result_in_json_format)
