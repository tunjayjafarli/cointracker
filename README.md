# cointracker
Cointracker app that lets you add/remove bitcoin addresses and retrieve address related information such as transactions, balances etc. through REST API endpoints.

## Installation

- Make sure you have `pip` and Python 3.x installed: `python -m pip install --upgrade pip`
- Create a virtual env and activate it.
- Run the following commands inside the virtual env.

Install the app dependencies and packages:
```
pip install Django
pip install djangorestframework
pip install requests
```


## Migrations:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Run the app server:
`python3 manage.py runserver`

Note: port 8000 is used by default; however, it can be changed by specifying any other port e.g. 9000

`python3 manage.py runserver 9000`


## REST API
Once the app server is up and running, our REST API is available at `http://127.0.0.1:8000/api/` 

### Endpoints:
- GET `/api/users/` : returns list of all users created
- GET/PUT/POST/DELETE `/api/users/{id}/` : CRUD operations for the user matching the given id param
- GET `/api/user/{id}/wallet/` : retrieves list of addresses the user has added
- POST `/api/user/1/wallet/`, `data={"addresses" : []}` : adds the specified addresses for the user
- GET/POST/DELETE `/api/user/{id}/wallet/{address}` : get/add/delete the given address
