
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)




# @app.route('/add?a=<int:one>&b=<int:two>')
# def adding(one,two):
#     return add(one,two)


# @app.route('/add?a=<int:one>&b=<int:two>')
# def subtracting(one,two):
#     return sub(one,two)


# @app.route('/add?a=<int:one>&b=<int:two>')
# def multiplying(one,two):
#     return mult(one,two)


# @app.route('/add?a=<int:one>&b=<int:two>')
# def dividing(one,two):
#     return div(one,two)



@app.route("/add")
def to_add():
    """adding a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return result

@app.route("/sub")
def to_sub():
    """subtracting a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return result

@app.route("/mult")
def to_mult():
    """multiplying a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return result

@app.route("/div")
def to_sub():
    """dividing a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return result

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)