from flask import Flask, Response, render_template_string
import io
import matplotlib.pyplot as plt
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from PythonAnywhere!</h1><p>Visit <a href="/plot">/plot</a> to see a sample plot.</p>'

@app.route('/plot')
def plot():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_data = base64.b64encode(img.getvalue()).decode()
    html = f'<img src="data:image/png;base64,{plot_data}"/>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
