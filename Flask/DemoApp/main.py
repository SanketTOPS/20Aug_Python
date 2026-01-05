from flask import Flask

app=Flask(__name__) #app init.

@app.route('/')
def index():
    return "Hello Flask!"
    
@app.route('/about')
def about():
    return "This is About!"

if __name__=='__main__':
    app.run(debug=True)