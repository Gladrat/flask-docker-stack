# Flask Docker stack

Yet another Flask Docker stack for boostraping projects.

> WARNING : Running in ```Debug mode``` mode, not intended for production
>
> For production deployement, see : [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)

## Base Docker Image

* [python:alpine](https://hub.docker.com/layers/python/library/python/alpine/images/sha256-0546f5e295a9e1b117042c083549bd3ab28998e456d7e1565f7517c6f0546d87?context=explore)

## Starting

* ```docker-compose up```
* Add ```-d``` to run container in the background

## Usage

* Port mapping : 5000:5000
* Live edition in `./src`
* Result : `http://localhost:5000`

## Project skeleton (./src)

### Architecture

```ascii
├── app.py
├── static
│   ├── assets
│   │   └── main.css
│   ├── favicon.ico
│   └── images
└── templates
    ├── common
    │   └── base.html.jinja
    └── index.html.jinja
```

### Description

* ```app.py``` : Main Flask app
* ```static``` : Static content
  * ```assets``` : For css, js, etc.
  * ```assets/main.css``` : Already included in default layout template
* ```templates``` : Jinja2 templates
  * ```index.html.jinja``` : Index of the project (inherit of ```base.html/jinja```)
  * ```common``` : For any inherited content
  * ```common/base.html.jinja``` : default layout with html bootstrap

## Todo

* Add Flask-SQLAlchemy ExtensioN
