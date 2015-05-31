# Pelawak
**Metacognitive Chat Bot**

[![Build Status](https://travis-ci.org/mclumd/pelawak.svg)](https://travis-ci.org/mclumd/pelawak)
[![Coverage Status](https://coveralls.io/repos/mclumd/pelawak/badge.svg)](https://coveralls.io/r/mclumd/pelawak)
[![Stories in Ready](https://badge.waffle.io/mclumd/pelawak.png?label=ready&title=Ready)](https://waffle.io/mclumd/pelawak)

## Getting Started

Ok, so here's (basically) how you get started with this app. If I miss anything, please let me know so that we can figure it out together.

1. Clone the app from Github then checkout the develop branch

        $ git clone https://github.com/mclumd/pelawak
        $ cd pelawak && git checkout origin develop

    Please remember to work in the develop branch - anything pushed to master will be automatically pushed to production on Heroku! Don't do that!

2. Install [Postgres](http://www.postgresql.org/download/) and [Redis](http://redis.io/topics/quickstart) -- the required dependencies. If you're on a Mac I recommend [Postgress.app](http://postgresapp.com/) and [Homebrew Redis](http://www.richardsumilang.com/blog/2014/04/04/how-to-install-redis-on-os-x/) with [Lunchy](https://github.com/eddiezane/lunchy). If you're on Linux you should be able to `apt-get install` all this stuff.

3. Install the Python dependencies

        $ pip install -r requirements.txt

4. Set up the environment variables that are required - you can do this in a `.env` file in your project root (ignored by gitignore) or by adapting your virtualenv, or putting them in your profile or whatever.

        export DJANGO_SETTINGS_MODULE=pelawak.settings
        export WEB_CONCURRENCY=2
        export DATABASE_URL=postgresql+psycopg2://django@localhost/pelawak
        export GOOGLE_OAUTH2_CLIENT_ID=[secret]
        export GOOGLE_OAUTH2_CLIENT_SECRET=[secret]
        export SECRET_KEY=[secret]

   Obviously, secret things are secret ... ask if you can't find them.

5. Ok, everything should be set up to work! Now open up _3 terminals_:

        t1$ python manage.py runserver
        t2$ python server.py
        t3$ python client/chat.py

    If everything is working there should be no errors.

6. Open up a browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) and you should see a "system ready" message, start typing into the chat terminal and into the browser, and you have done chat!

## Dependencies

- This project is uses [SwampDragon](http://swampdragon.net/) for websockets and Django - you should probably check that out to learn more.
