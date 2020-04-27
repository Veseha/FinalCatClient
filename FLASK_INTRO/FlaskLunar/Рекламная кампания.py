from flask import Flask

app = Flask(__name__)


@app.route('/promotion')
def promotion():
    return '''<br>Человечество вырастает из детства.</br>
<br>Человечеству мала одна планета.</br>
<br>Мы сделаем обитаемыми безжизненные пока планеты.</br>
<br">И начнем с Марса!</br>
<br">Присоединяйся!</br>'''


@app.route('/image_mars')
def image_mars():
    return """<br>Жди нас, Марс!</br>
<img src=https://svs.gsfc.nasa.gov/vis/a010000/a012200/a012266/Mars_Wet_LPI_16x9.jpg width=1250 height=720>
<br>вот она, планета.</br>
"""


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
