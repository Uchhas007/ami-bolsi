from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/') # endpoint for the website 
# def hello():
#     return 'Hello, World!'

@app.route('/uchhas') # endpoint for the website 
def uchhas():
    return 'Hello, Uchhas!'



@app.route('/') # endpoint for the website 
def home():
    t = "কালকের চিপা!!!"
    return render_template('index.html', title = t)

@app.route('/about') # endpoint for the website 
def about():
    name = 'Uchhas Saha'
    return render_template('about.html', name1 = name)


# @app.route('/p') # endpoint for the website 
# def p():
#     print('Hello, World!') # can't print anything, Only returns 

if __name__ == '__main__':
    app.run(debug = True) # telling the flask app to run 