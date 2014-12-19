Santa Claus API
=========================

It tells you who's been naughty or nice.

#Dependencies

##Python

Make sure you have Python on your computer. The following two commands should work:

```
python --version
pip --version
```


##virtualenv

[Virtualenv](https://virtualenv.readthedocs.org/en/latest/) makes it possible to install multiple Python environments on one computer; including installing a Python environment just for this project. 

[Flask installation with virtualenv notes](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)

### Install

```
pip install virtualenv
pip install virtualenvwrapper
```

# Get It

```
git clone https://github.com/wbushey/santaclaus.git
cd santaclaus
virtualenv env
```

# Update and Run It 

```
cd santaclaus 
git pull
source env/bin/activate
pip install -r requirements.txt
./run.py
```

# See It

Visit <http://localhost:5000/?name=YOURNAME>

Or, see it online at <http://claus.io/?name=YOURNAME>


# Configure a Database

With no configuration, the Santa Claus API will create and use a SQLite 
database in `santa.db`. If you have a Postgres database ready to use, you can 
configure the Santa Claus API to use it by setting the `$DATABASE_URL` to the
URL of the Postgres instance.


#Resources

[The Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
