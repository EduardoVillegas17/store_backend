from ast import Import
from bson import ObjectId
from flask import Flask, request
from about import me
from data import mock_data
import json
import random
from config import db
from flask_cors import CORS


app= Flask('server')
CORS(app)#ALLOW REQUEST FROM ANY ORIGIN

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
def about_me2():
    return me["first"]+""+me["last"]
    #return f'{me["first"]}{me["last"]}'

#get /api/about
#return first lastname
@app.get("/api/about")
def about_json():
    return json.dumps(me)

#get /api/products
#return mock_data a json string

def fix_mongo_id(obj):
    obj['id'] =str(obj["_id"])
    del obj["_id"]
    return obj


#get /api/products
#return mock_data as a json string
@app.get("/api/products")
def get_products():
    cursor=db.products.find({})
    results=[]
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.post("/api/products")
def save_product():
    product = request.get_json() #get a dictionary or a list
    
    #save the product
    db.products.insert_one(product)
    fix_mongo_id(product)

    return json.dumps(product)



@app.get("/api/products/<id>")
def get_products_by_id(id):
    prod=db.products.find_one({"id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"
    fix_mongo_id(prod)

    return json.dumps(prod)




@app.get("/api/products_category/<category>")
def get_prods_category(category):
    cursor=db.products.find({"category": category})
    result=[]
    for prod in cursor:
        fix_mongo_id(prod)
        result.append(prod)

    return json.dumps(result)


#Get /api/products_cheapest
@app.get("/api/products_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution=cursor[0]
    for prod in cursor:
        if prod["price"]<solution["price"]:
            solution=prod
    return json.dumps(solution)

@app.get("/api/categories")
def get_categories():
    categories=[]
    cursor= db.products.find({})
    for product in cursor:
        cat=product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.get("/api/count_products")
def get_products_count():
    cursor= db.products.find({})

    count =0
    for prod in cursor:
        count+=1
    return json.dumps({"count":count})


#return all prods whose totle contains text
@app.get("/api/seach/<text>")
def search_product(text):
    results=[]

    #do the magic here
    text=text.lower()
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod)


    return json.dumps(results)



#############API ENDPOINTS = COUPON CODES##############



app.run(debug=True)