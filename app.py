from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__, template_folder='templates')  # Correct: set 'templates' as the directory

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")  # Remove "templates/" here

# Route for handling footprint calculation 
@app.route("/calculate", methods=["POST"])
def calculate_footprint_handler():
    if request.method == "POST":
        try:
            # Access user input from the request 
            data = request.form  #form data in index.html

            # Call the calculate function from calculator.py 
            footprint = calculate_footprint(data)
            recommendations = generate_recommendations(footprint)

             # Store footprint and recommendations in session
            session['carbon_footprint'] = footprint
            session['recommendations'] = recommendations

            return render_template("index.html")
            
        except Exception as e:
            # Handle potential errors (e.g., missing data)
            return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
