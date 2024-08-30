from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    result = "pass" if score >= 50 else "fail"
    return render_template('result.html', result=result, score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result="fail", score=score)

@app.route('/result/<int:marks>')
def result(marks):
    if marks >= 50:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4

        if total_score >= 50:
            return redirect(url_for('success', score=int(total_score)))
        else:
            return redirect(url_for('fail', score=int(total_score)))

if __name__ == '__main__':
    app.run(debug=True)
