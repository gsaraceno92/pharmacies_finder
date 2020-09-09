# Pharmacies Finder

An useful solution to find the pharmacies closest to you

**For now available only for Campania region.**

Step to follow:

- [Installation](#installation)
- [Setup docker project](#setup)
- [Test](#running-tests)
- [Site](#site)

---

## Installation

- Clone the project as follow:

  `git clone git@github.com:gsaraceno92/pharmacies_finder.git`

- Copy [**_.env.example_**](app/.env.example) into **_.env_**

  **Note:** edit [docker .env file](.env) only if build fail; that probably means that your user id (in ubuntu system) is different from this one.
  In this case update with your own id.

---

## Setup

These are the instructions to follow to set up the project on your local environment.

1.  Build the Docker image

        docker-compose up --build -d

2.  Use `docker image ls` and `docker container ls` (or `docker ps`) to see your images and the running containers

3.  Enter the container and run all the next commands inside it

        docker exec -it finder_pharmacies bash

### **Starting and stopping containers**

Once created, the containers can be **started** anytime with the following command:

    `docker-compose -f up -d`

To **stop** the containers, use instead:

    `docker-compose stop`

### ...continue

Sometimes Flask application could not reload automatically the changes (since the binding volume e the work type used to run the app); in this case just restart the container with `docker-compose restart`.

**Note:** the above commands must be used in the same folder of the project.
If you want to use the commands anywhere use **-f** to specify the docker-compose file position, e.g.:

    `docker-compose -f ./docker-compose.yml up -d`

---

## **Running tests**

Run the files inside [tests](app/tests) directory as follow:

    `docker exec -it finder_pharmacies python3 tests/test_pharmacy.py`

---

## Site

The app will run through http://localhost:5000.
In particular you can visit http://localhost:5000/api/browse; here can be used the JSON-RPC method.

Use the method **_SearchNearestPharmacy_** to retrieve the nearest position to the location set by _`latitude`_ and _`longituted`_ in _`currentLocation`_ parameter.

Define the _`range`_ (in meters) in which you want to search and set the result size with the _`limit`_.
