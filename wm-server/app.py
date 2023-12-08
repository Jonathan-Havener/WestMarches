from flask import Flask, request

# Create a Flask web server
app = Flask(__name__)


# Define a route and a view function for both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'Hello, Flask!'
    elif request.method == 'POST':
        # Access POST data
        data = request.form.get('data')  # assuming you're sending 'data' in the POST request
        return f'POST request received with data: {data}'
    else:
        return 'Unsupported HTTP method'


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
