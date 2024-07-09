from flask import Flask, render_template, request, jsonify


app = Flask(__name__ , template_folder='Web/index.html')


# Route for the main page
@app.route("/")
def index():
    return render_template("Web/index.html")  

# Route for handling footprint calculation 
@app.route("/calculate", methods=["POST"])
def calculate_footprint_handler():
    if request.method == "POST":
        try:
            # Access user input from the request 
            data = request.form  #form data in index.html

            # Call the calculate function from calculator.py 
            footprint = calculate_footprint(data)

            # Return JSON response with the calculated footprint
            return jsonify({"footprint": footprint})
        except Exception as e:
            # Handle potential errors (e.g., missing data)
            return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
