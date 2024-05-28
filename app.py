from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tutoriel')
def tutoriel():
    return render_template('tutoriel.html')

@app.route('/defi_1', methods=['GET', 'POST'])
def defi_1():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = a + b
        return render_template('defi_1.html', result=result)
    return render_template('defi_1.html', result=None)

@app.route('/defi_2', methods=['GET', 'POST'])
def defi_2():
    if request.method == 'POST':
        n = int(request.form['n'])
        if n % 2 == 0:
            result = f"{n} est un nombre pair."
        else:
            result = f"{n} est un nombre impair."
        return render_template('defi_2.html', result=result)
    return render_template('defi_2.html', result=None)

@app.route('/defi_3', methods=['GET', 'POST'])
def defi_3():
    if request.method == 'POST':
        numbers = list(range(1, 11))
        return render_template('defi_3.html', numbers=numbers)
    return render_template('defi_3.html', numbers=None)

@app.route('/defi_4', methods=['GET', 'POST'])
def defi_4():
    if request.method == 'POST':
        elements = request.form['elements'].split(',')
        return render_template('defi_4.html', elements=elements)
    return render_template('defi_4.html', elements=None)

@app.route('/defi_interactif')
def defi_interactif():
    return render_template('defi_interactif.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/aide')
def aide():
    return render_template('aide.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
