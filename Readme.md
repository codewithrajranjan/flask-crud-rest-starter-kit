## Git clone the application

## Create a virtual environment inside the application 

```python

    virtualenv -p /usr/bin/python3.4 venv    

    source venv/bin/activate

```

## Install Python modules

```python

   pip3.4 install -r requirements.txt 
    
```


## Run the application using

```python

    python app.py

```


## You will get two REST API

```python

        http://localhost:5000/api/v1.0/task

        http://localhost:5000/api/v1.0/task/id/<taskId>

```
