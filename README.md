# Flask template

Just consists of a basic flask directory structure. Made to use the application factory method.

## Included packages
- Flask
- Flask SQLAlchemy
- Flask migrate

## Usage

Clone the repository:
```shell script
git clone https://github.com/arnu515/flask-template flask
cd flask
```

Install packages
```shell script
python3 -m venv venv
source venv/bin/activate
# Windows: venv/Scripts/activate
pip3 install -r requirements.txt
```

Start the app
```shell script
flask db init
flask db migrate
flask db upgrade
flask run
```
