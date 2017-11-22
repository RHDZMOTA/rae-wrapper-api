# RAE WRAPPER API

Get spanish word's definition by accessing the official RAE 
webpage via Selemiun-PhantomJS.


## Usage

Base url: https://rae-wrapper-api.herokuapp.com

### Word definition

**URL PREFIX:** _/rae/desc/_

This service returns the definition and phonetics of a given word.
To access the service, perform a get or post request replacing _word_
as desired:
* https://rae-wrapper-api.herokuapp.com/rae/desc/word

**EXAMPLE**

This example illustrates how to get the description of the word: hola

* Use your terminal to perform a request:

    ```bash
    curl https://rae-wrapper-api.herokuapp.com/rae/desc/hola
    ```

* Use python
    ```python
    import requests
    desc = requests.get("https://rae-wrapper-api.herokuapp.com/rae/desc/hola").json()
    print(desc)
    ```
    
## Development and deployment

{add content}

## Heroku configuration

### Create

Create a heroku instance as usual. 

```bash
heroku create rae-wrapper-api
```
### Add buildpacks
Add builpacks in order to run python and PhantomJS apps. 
```bash
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 https://github.com/stomita/heroku-buildpack-phantomjs.git
```

## TODO

{add content}
