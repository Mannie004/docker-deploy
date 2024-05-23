from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Random Dog</title>
    </head>
    <body>
        <h1>Here is a random dog for you!</h1>
        <img src="{{ image_url }}" alt="Random Dog" style="width:500px;">
    </body>
    </html>
    '''
    return render_template_string(html, image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
