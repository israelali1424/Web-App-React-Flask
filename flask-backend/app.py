from flask import Flask, render_template,g, render_template, flash, redirect, url_for

app = Flask(__name__)                                                                                                                                                                               
                                                                                                                                                                                                    
@app.route('/')                                                                                                                                           
def index():                                                                           
    return render_template("index.html",token="Hello React-Flask")

app.run(debug=True)