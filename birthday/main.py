from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def birthday():
    return render_template('birthday.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/check_birthday')
def check_birthday():
    pass
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

