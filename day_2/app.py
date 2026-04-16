# A simple Flask application that defines a few routes and renders templates.

from flask import Flask, render_template, request
# initialize the Flask application
app = Flask(__name__)

@app.route('/home')                # Define a route for the home page
def home():                        # When the user visits the /home URL, this function will be called
    return render_template('home.html')

@app.route('/about')                # Define a route for the about page
def about():                        # When the user visits the /about URL, this function will be called
    return render_template('about.html')


@app.route('/contact') 
def contact():
    print("Received a GET request to /contact")  # Log the request for debugging purposes
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])  # Define a route for form submission that accepts POST requests
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(f"Name:{name}, Email: {email}, Phone: {phone}, Message: {message}")  # Log the form data for debugging purposes
    return render_template('contact.html')  # Render the contact page with a



if __name__ == '__main__':         # Run the application
    app.run(debug=True)            # Enable debug mode for development purposes
