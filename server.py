from flask import Flask, request
from about import me
from data import mock_data
import json
import random
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

@app.post("/api/products")
def save_product():
    product = request.get_json()

    mock_data.append(product)
    product["id"] = random.randint(1, 893214789)
    return json.dumps(product)

@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"])==id:
            return json.dumps(prod)

    return "NOT FOUND"


@app.get("/api/products_category/<category>")
def get_prods_category(category):
    print("your category: ", category)
    result=[]
    category=category.lower()
    for prod in mock_data:
        if prod["category"].lower() == category:
            result.append(prod)

    return json.dumps(result)


#Get /api/products_cheapest
@app.get("/api/products_cheapest")
def get_cheapest():
    solution=mock_data[0]
    for prod in mock_data[0]:
        if prod["price"]<solution["price"]:
            solution=prod
    return json.dumps(solution)

@app.get("/api/categories")
def get_categories():
    categories=[]
    for product in mock_data:
        cat=product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.get("/api/count_products")
def get_products_count():
    count = len(mock_data)

    return json.dumps({"count":count})


#return all prods whose totle contains text
@app.get("/api/seach/<text>")
def seach_product(text):
    results=[]

    #do the magic here
    text=text.lower()
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod)


    return json.dumps(results)

app.run(debug=True)