from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


df = pd.read_excel("RK ENGG.xlsx")

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/search', methods=['POST'])
def search():
    name= request.form['name']
    try:
        results=df[df['COMPANY NAME'].str.contains(name, case=False, na=False)]
        data= results.to_dict(orient='records')
    except KeyError:
        data=[]
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
