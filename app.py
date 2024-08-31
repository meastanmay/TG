from flask import Flask, request, jsonify, render_template

app = Flask(__name__,template_folder='Template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    if operation == 'add':
        result = int(num1) + int(num2)
    elif operation == 'subtract':
        result = int(num1) - int(num2)
    elif operation == 'multiply':
        result = int(num1) * int(num2)
    elif operation == 'divide':
        result = int(num1) / int(num2)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)