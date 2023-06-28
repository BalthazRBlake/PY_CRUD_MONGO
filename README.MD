# PYTHON MONGO & FLASK

- To create the project we first create the python evn:
  
  ```python -m venv <directory>```

- Then activate the env running one of the following depending on your terminal/OS

  PowerShell
  ```.\Scripts\Activate.ps1```

  cmd
  ```.\Scripts\Activate.bat```

  unix
  ```source /bin/activate```

- After finishing using the project it is recommended to deactivate the env running:
  
  ```deactivate```

- The project uses the following libraries:

  ```python -m pip install "pymongo[srv]”```

  ```pip install python-dateutil```

  ```pip install python-dotenv```

  ```pip install flask```

- Set the env vars to run the FLASK APP

  Once again it will be different depending on the OS

  PowerShell

  ```$env:FLASK_APP = 'src/controllers/k9FlaskApi'```
  ```$env:FLASK_ENV = 'development'```

  Unix

  ```export FLASK_APP = 'src/controllers/k9FlaskApi'```
  ```export FLASK_ENV = 'development'```

- Run the FLASK APP

  ```flask run```

  it will show an output like this:
  
  * Serving Flask app 'src/controllers/k9FlaskApi'
  * Debug mode: off

  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on http://127.0.0.1:5000 
