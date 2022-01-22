from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    payload = {
        'strawberry' : int(request.form['strawberry']),
        'raspberry' : int(request.form['raspberry']),
        'blackberry' : int(request.form['blackberry']),
        'apple' : int(request.form['apple']),
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'student_id' : request.form['student_id'],
    }
    payload['customer_name'] = payload['first_name'] + " " + payload['last_name']
    payload['count'] = payload['strawberry'] + payload['raspberry'] + payload['blackberry'] + payload['apple']
    print(payload)
    return render_template("checkout.html", payload=payload)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    