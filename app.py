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

            # Redirect to the result page
            return redirect(url_for('result'))
            
        except Exception as e:
            # Handle potential errors (e.g., missing data)
            return jsonify({"error": str(e)})

# Route for displaying results
@app.route("/result")
def result():
    footprint = session.get('carbon_footprint')  # Retrieve from session
    recommendations = session.get('recommendations')

    if footprint is None:
        # No calculation done yet
        message = "No carbon footprint calculation has been done yet."
    else:
        message = None

    return render_template("result.html", data=dict(
        total_carbon_footprint=footprint,
        recommendations=recommendations,
        message=message
    ))


if __name__ == "__main__":
    app.run(debug=True)
