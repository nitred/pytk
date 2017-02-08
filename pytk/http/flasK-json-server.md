## A http server that can accept Json and other kind of requests
```python
import json
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def return_reponse():
  print("data (json/text): {}".format(request.data))
  resp = make_response(request.data)
  return resp
```
