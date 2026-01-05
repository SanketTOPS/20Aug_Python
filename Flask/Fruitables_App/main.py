from flask import Flask,render_template

app=Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/chackout')
def chackout():
    return render_template('chackout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


if __name__=='__main__':
    app.run(debug=True)