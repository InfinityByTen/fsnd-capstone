# JWT Getter Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI  is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks

## Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
ionic serve
```

>_tip_: Do not use **ionic serve**  in production. Instead, build Ionic into a build artifact for your desired platforms.

## Steps to get a JWT

| WARNING: You DO NOT want to login from a normal browser window. Please switch to an inconito or private browsing tab. Else, you will be logged in forever and never never never ever be able to login with different credentials. Think of it like [Limbo.]( https://inception.fandom.com/wiki/Limbo ) |
|---|

    > This is not my thing. I just forked it from FSND Coffee Project. It might get fixed later.

1. As instructed, open the page in incognito or private browsing.
2. Login with the credentials provided. You will have them, if you're an intended user.
3. Close and open a new incognito to enter different credentials to get a JWT with different permissions.

