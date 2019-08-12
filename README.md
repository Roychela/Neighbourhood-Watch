## TITLE
Hood-Watch

## AUTHOR
Roy Chela

## DESCRIPTION
A django application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## DATE
12/08/2019

## BEHAVIOUR DRIVEN DEVELOPMENT(BDD)

| Behaviour | Input                     | Output                    |
| --------- | ------------------------- | ------------------------- |
|Navigate to website and view various neighbourhoods on the homepage|click on join neighbourhood  | joining a neighbourhood and viewing info on that neighbourhood|
|Post a business|Fill in necessary details on a form eg business description|Business is posted on neighbourhood|
|Navigate to search input| Type in a neighbourhood|The searched neighbourhood is displayed if available|


## SETUP
### Requirements
* Django 2.2.4 
### Installation
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* Access the live site using the local host provided

### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)
#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Roychela/Neighbourhood-Watch.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste the following filling where appropriate:
```
SECRET_KEY='your_Secret_key'
DEBUG=True
DB_USER='your_database_username'
DB_PASSWORD='your_database_password'
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## LIVE SITE
Click [Live site](https://roy1hoodwatch.herokuapp.com/) to view the deployed application
## KNOWN BUGS
None

## TECHNOLOGIES
* Python3.6
* Django
* Javascript
* Css
* HTML5


## LICENSE
[MIT](https://github.com/Roychela/Neighbourhood-Watch/blob/master/LICENSE)