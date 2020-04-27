from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>


                            <h1>Анкета претендента</h1>
                            <h2>На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="фамилию" name="text">
                                    <input type="text" class="form-control" id="name" placeholder="имя" name="text">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>

                                    <div class="form-group1">
                                        <label for="form-check">выбери профессию</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="par" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Сварщик
                                          </label>
                                        </div>
                                            <div class="form-check">
                                          <input class="form-check-input" type="radio" name="par" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Прогер
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="par" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            пекарь
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="radio" name="par" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            медик
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                            <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">почему ты решил покинуть свою родную планету?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">готов пробыть на марсе всю 
свою жизнь</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')