from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", row=8,col=8, odd_color="black",even_color="red") 
    
@app.route('/<int:row>')          # The "@" decorator associates this route with the function immediately following
def singe_param(row):
    return render_template("index.html", row=row,col=row,odd_color="black",even_color="red")  # Return the string 'Hello World!' as a response

@app.route('/<int:row>/<int:col>')
def double_param(row,col):
    return render_template("index.html", row=row,col=col, odd_color="black",even_color="red")

@app.route('/<int:row>/<int:col>/<string:odd_color>')
def triple_param(row,col,odd_color):
    return render_template("index.html", row=row,col=col, odd_color=odd_color, even_color="red")

@app.route('/<int:row>/<int:col>/<string:odd_color>/<string:even_color>')
def quad_param(row,col,odd_color,even_color):
    return render_template("index.html", row=row,col=col, odd_color=odd_color, even_color=even_color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.