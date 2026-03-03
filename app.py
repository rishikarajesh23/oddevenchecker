from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return '''
        <h1>Odd or Even Checker</h1>
        <form action="/check" method="post">
            <label>Enter a number:</label>
            <input type="number" name="number" required>
            <button type="submit">Check</button>
        </form>
    '''

# Check route
@app.route('/check', methods=['POST'])
def check():
    number = int(request.form['number'])

    if number % 2 == 0:
        result = f"{number} is Even"
    else:
        result = f"{number} is Odd"

    return f'''
        <h2>{result}</h2>
        <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
