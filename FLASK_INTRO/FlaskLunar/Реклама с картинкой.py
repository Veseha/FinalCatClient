from flask import Flask

app = Flask(__name__)


@app.route('/choice/<name>')
def promotion(name):
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
                    <title>варианты выбора</title>
                  </head>
                  <body>
                    <h1>мое предложение: %s</h1>
                    
                    эта планета близка к земле
                    
                    <div class="alert alert-secondary" role="alert">
                      на ней ресурсы
                    </div>
                    
                    <div class="alert alert-success" role="alert">
                      и вода
                    </div>
                    
                    <div class="alert alert-dark" role="alert">
                      и магнетизм
                    </div>
                    
                    <div class="alert alert-warning" role="alert">
                     а еще она красивая
                    </div>
                    
                  </body>
                </html>""" % name


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')