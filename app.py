from flask import Flask,render_template,request,redirect
app = Flask(__name__)


data = {'1':'bed+OR+beds','2':'icu','3':'oxygen','4':'ventilator+OR+ventilators',
        '5':'test+OR+tests+OR+testing','6':'remdesivir','7':'favipiravir',
        '8':'tocilizumab','9':'plasma','10':'food'}



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        d = request.form['data']
        q = 'https://twitter.com/search?q=verified+indore+'
        x = q + data[d] + '+-"needed"+-"required"&f=live'
        return redirect(x)
    return render_template("IndoreAgainstCovid.html")

if __name__ == '__main__':
    app.run(debug=True)
