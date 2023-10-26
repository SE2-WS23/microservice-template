# MICROSERVICE-TEMPLATE

This repository contains the template for a microservice. It is based on the Google Cloud Functions Framework.

## Steps to setup the project:

1. Install python3 and pip3
2. In your terminal run: `python3 -m venv env`
3. In your terminal run: `source env/bin/activate` (Should be done every time you open a new terminal or a new instance)
4. In your terminal run: `python3 -m pip install -r requirements.txt`

## Run the project:

You can run the project in two ways:

1. Run the cloud function -> In your terminal run: `functions-framework --target=http_function`
2. Run the main.py file -> In your terminal run: `python3 main.py`
   The second option is during development more convenient, because you don't have to restart the cloud function every time you change something.
   Please note that you should ONLY run the second option during development, because the environment is a little bit different than the cloud function runtime.
   So if you want to test the cloud function, you should use the first option.

## Further information

If you need further help or information, you can contact Christian
