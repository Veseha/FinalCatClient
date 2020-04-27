from flask import Flask

app = Flask(__name__)


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                                      <h1>Ждэ нас, марс</h1>

                    <img src="{}" alt="здесь должна была быть картинка, 
                    но не нашлась">
                  </body>
                </html>""".format('/static/img/img.png')
    # return '</br>'.join(['Человечество вырастает из детства.',
    #         'Человечеству мала одна планета.',from FLASK import Flask
    #
    # app = Flask(__name__)
    #
    #
    # @app.route('/promotion')
    # def promotion():
    #     return """<!doctype html>
    #                 <html lang="en">
    #                   <head>
    #                     <meta charset="utf-8">
    #                     <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
    #                     <title>Привет, Яндекс!</title>
    #                   </head>
    #                   <body>
    #                                       <h1>Ждэ нас, марс</h1>
    #
    #                     <img src="{}" alt="здесь должна была быть картинка,
    #                     но не нашлась">
    #                   </body>
    #                 </html>""".format('/static/img/img.png')
    #     # return '</br>'.join(['Человечество вырастает из детства.',
    #     #         'Человечеству мала одна планета.',
    #     #         'Мы сделаем обитаемыми безжизненные пока планеты.',
    #     #         'И начнем с Марса! ',
    #     #         'Присоединяйся!'] + '''
    #     #                     <img src="{}" alt="здесь должна была быть картинка,
    #     # но не нашлась">'''.format('/static/img/img.png'))
    #
    #
    # @app.route('/index')
    # def index():
    #     return "И на Марсе будут яблони цвести!"
    #
    #
    # if __name__ == '__main__':
    #     app.run(port=8080, host='127.0.0.1')
    #         'Мы сделаем обитаемыми безжизненные пока планеты.',
    #         'И начнем с Марса! ',
    #         'Присоединяйся!'] + '''
    #                     <img src="{}" alt="здесь должна была быть картинка,
    # но не нашлась">'''.format('/static/img/img.png'))


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')