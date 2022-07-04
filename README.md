# Trusted_Intel_Platform_Backend
Core Logic of General Purpose Search Engine for "Trusted" range of PanaBIOS products.

### Setup
## Installation on Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  $ virtualenv --python=python3.8 myvenv
  
  $ source myvenv/bin/activate

  (myvenv) $ pip install -r requirements.txt

  (myvenv) $ python manage.py makemigrations

  (myvenv) $ python manage.py migrate
  
  (myvenv) $ python manage.py load_bookable_services 
  
  (myvenv) $ python manage.py loaddata  booking_manager_api/fixtures/timeslot.json  
  
  ```

## Installation of rpc packages

* Navigate(terminal) to the directory where the setup.py file is located.

* Issue the command
  ```
    pip install -e .

  ```
## Running API Tests

* Issue Command Pytest [path to the test file]
```
 Example: pytest .\intel_api\tests\test_auth_login.py 
 ```
# Note that tests files are contained in a tests folder in every app 