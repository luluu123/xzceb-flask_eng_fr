from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    a=translator.english_to_french(textToTranslate)
    return json.dumps(a)
@app.route("/frenchToEnglish")

def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    a=translator.french_to_english(textToTranslate)
    return json.dumps(a)
@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)