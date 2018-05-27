# Twilio Contacts

A 3 hour sprint to integrate twilio with a django 2.x backend.

## Docker

This project will run with docker-compose. If you have docker (and compose)
installed you can painlessly start the app by typing `docker-compose up` in the
root of the project.

### Environment Variables

Due to the nature of the integration, this application depends on 3 variables
defined in your environment in order to run:

* TWILIO_SID
* TWILIO_AUTH
* TWILIO_NUMBER

You can get those details from your own twilio account.


### Features

* User Registration
* User Authentication
* Twilio SMS Integration
* Message Persistence
