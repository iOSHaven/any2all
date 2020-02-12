# Any2All
A file converter project

![Python Build](https://github.com/iOSHaven/any2all/workflows/Python%20application/badge.svg)

# getting started

The read me will cover how to get your environment setup, as well as folder structure and coding practices.

### macos
1. create virtual env. `python3 -m venv env`
2. use virtual env. `source env/bin/activate`
3. install required dependencies (do step 2 first). `pip install -r requirements.txt`
4. run using `python3 manage.py runserver`
5. install ImageMagick `brew install imagemagick`
6. install packages (do step 2 first) `pip install <package-name>`

### windows
1. create virtual env. `py -m venv env`
2. use virtual env. `env\Scripts\activate.bat`
3. install required dependencies (do step 2 first). `pip install -r requirements.txt`
4. run using `py manage.py runserver`
5. install ImageMagick http://legacy.imagemagick.org/script/binary-releases.php#windows
6. install packages (do step 2 first) `pip install <package-name>`

### suggested vscode extentions
1. `autoDocstring` https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
2. `Django` https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django
3. `python` https://marketplace.visualstudio.com/items?itemName=ms-python.python
4. `tailwind intellisense` https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss

### folder structure
```
app.utils - the core logic of the application.
app.templates - the html files
env - the venv folders and files
storage - file storage for development
www - the django settings initialization 
```

