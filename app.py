try:
	from flask import Flask, render_template, url_for, request
	from flask_bootstrap import Bootstrap
	from googletrans import Translator
except ImportError:
	from pip._internal import main
	print("Installing dependencies")
	main(['install','-r','requirements.txt'])

app = Flask(__name__)
Bootstrap(app)


translator=Translator()

def paraphrased(in_text):

    par_text = translator.translate(in_text, dest='hi').text
    return par_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        text = request.form['inputText']
        prediction = paraphrased(text)
    return render_template('result.html',prediction=[text,prediction])

# run the app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)




app = Flask(__name__)
Bootstrap(app)