import requests                            # Import package

result = requests.get(url)                 # Use get function to make GET request

result.status_code                         # Status Code

result.headers                             # Header information

result.text                                # Response text

result.encoding                            # Response encoding
