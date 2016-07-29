# recast-rest-api [![Build Status](https://travis-ci.org/cbora/recast-rest-api.svg?branch=master)](https://travis-ci.org/cbora/recast-rest-api)
API for the RECAST project live at http://recast-rest-api.herokuapp.com

A RestfulAPI built using EVE. The package is dockerized and has `procfile` for deployement on Heroku, see `docker-compose.yaml` and `dockerfile`

#Instructions


    virtualenv env
    git clone <this-repo>
    cd <this-repo>
    pip install -e . --process-dependency-links
    recast-api server --config /path/to/config/file

