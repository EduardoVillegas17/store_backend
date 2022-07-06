from unittest import mock
from flask import Flask
from about import me
import json
from data import mock_data
app= Flask('server')


@app.get("/")
def home():
    return"Hello!!!  :)"


@app.get("/test")
def test():
    return "this is a test"

@app.get("/about")
def about_me():
    return "Eduardo villegas"








@app.get("/api/version")
def version():
    return "1.0"

@app.get("/api/about") 
def about_me():
    return me["first"]+""+me["last"]
    #return f'{me["first"]}{me["last"]}'

#get /api/about
#return first lastname
@app.get("/api/about")
def about_json():
    return json.dumps(me)

#get /api/products
#return mock_data a json string

@app.get("/api/products")
def get_products():
    return json.dumps(mock_data)



@app.get("/api/products/<id>")
def get_products_by_id(id):
    
    
    for prod in mock_data:
        if str(prod["id"])==id:
            return json.dumps(prod)

    return "NOT FOUND"
app.run(debug=True)