from flask import Flask


app= Flask('server')


@app.get("/")
def home():
    return"Hello!!!  :)"


@app.get("/test")
def test():
    return"this is a test"










@app.get("/api/version")
def version():
    return"1.0"


app.run(debug=True)