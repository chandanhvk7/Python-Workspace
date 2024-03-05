from flask import Flask,Response,request
from customerdao import get_all_customers,add_new_customer,get_one_customer
from customerdao import Customer
import json

app=Flask('customer-api')

@app.route("/")
def home():
    return """
<h1> Welcome to Customer REST Endpoints</h1>
<hr>
<p>Created by our Greatest Soldier, powered by <em>Flask</em>"""

def create_response(data=None,status=200,mimetype="application/json"):
    return Response(json.dumps(data,cls=Customer.CustomerEncoder),status=status,mimetype=mimetype)


@app.route("/customers",methods=["GET"])
def handle_get_customers():
    customers=get_all_customers()
    return create_response(customers)

@app.route("/customers",methods=["POST"])
def handle_post_customer():
    cust=request.get_json()
    cust=Customer(**cust)
    try:
        cust=add_new_customer(cust)
        return create_response(cust,status=201)
    except Exception as e:
        err=dict(message=f'{e}')
        return create_response(err,status=500)
    
@app.route("/customers/<int:cust_id>",methods=["GET"])
def handle_get_one_customer(cust_id):
    customer=get_one_customer(cust_id)
    return create_response({"Message":"No data found"},status=404) if customer is None else create_response(customer)

app.run(host='0.0.0.0',port=1234,debug=True)