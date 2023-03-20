## Minimal POS based on Flask Soft UI Dashboard

## ✨ Manual Build

```bash
$ git clone https://github.com/stxndli/flask-POS.git
$ cd flask-soft-ui-dashboard
```

<br />

### 👉 Set Up 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
// OR
$ flask run --cert=adhoc # For HTTPS server
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />
Create users at http://127.0.0.1:5000/register
Login at http://127.0.0.1:5000/login
environment variables are in env.sample file
