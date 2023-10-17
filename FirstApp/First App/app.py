from flask import Flask, jsonify

app = Flask(__name__)

# Route Addition
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

# POST Method
@app.route('/sagar', methods=['POST'])
def sagar():
    if request.method == 'POST':
        
        return "hello sagar"
    else:
        return "Method not allowed"
    
# Json response
@app.route('/varsha')
def varsha():
    name = "Varsha"
    message = f"Hello {name}"
    return jsonify({"name": name, "message": message})

# Query parameter
@app.route('/hello')
def hello():
    name = request.args.get('sagar')
    if name:
        return f"Hello {name}"
    else:
        return "Hello Guest"
    
  # Error handler/ page not found  
@app.errorhandler(404)
def page_not_found(e):
    return "Route not found", 404

# redirect url
@app.route('/redirect')
def redirect_sagar():
    return redirect(url_for('sagars'))

@app.route('/sagars')
def sagar():
    return "Welcome to Sagar's page!"

# Template rendering
@app.route('/sagar')
def sagar():
    return render_template('index.html', message='Hello Sagar')

# Form submission
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greet', name=name))
    return render_template('form.html')
    
if __name__ == '__main__':
    app.run(debug=True)
