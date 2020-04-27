from flask import Flask

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def promotion(nickname, level, rating):
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Res отбора</h1>
                    <h2> ретендента на участие в миссии {} </h2>

                    <div class="alert alert-success" role="alert">
                      Your range after {} этапа
                    </div>

                    <div class="alert alert-dark" role="alert">
                      sostovlyaet {}
                    </div>

                    <div class="alert alert-warning" role="alert">
                     goodluck
                    </div>

                    
                  </body>
                </html>""".format(nickname, level, rating)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')