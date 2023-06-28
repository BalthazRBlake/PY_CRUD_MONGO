from flask import Flask, render_template, make_response

from src.services.k9ServiceImpl import CrudServiceImpl
from src.models.k9 import K9

app = Flask(__name__, template_folder="../templates")

@app.route('/k9api/<k9name>', methods=['GET'])
def find_k9_by_name(k9name):
  print(f'Hello {k9name}!')
  found_k9 = CrudServiceImpl.find_k9_by_name(k9name)
  
  print(f'Found {found_k9}')
  response = render_template('index.html', k9=found_k9)
  return response

@app.route('/k9api', methods=['GET'])
def find_all_k9s():
  k9s = CrudServiceImpl.find_all_k9s()
  
  response = make_response(f'{k9s}', 200)
  response.headers['Content-Type'] = 'application/json'
  return response