from flask import Flask, request, url_for

site = Flask(__name__)


sample = 'static/img.png'


pagetext = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <title>Пример загрузки файла</title>
</head>
<body>
<h2> файл </h2>
<form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                        <img src="{sample}" alt="здесь должна была быть картинка">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
</body>    
"""


@site.route('/sample_file_upload', methods=('POST', 'GET'))
def upload():
    # response.cache_control.max_age
    try:
        global sample
        print(request.method)
        if request.method == 'POST':
            print('one')
            with open(sample, 'wb+') as entry:
                print(request.files)
                print('two')
                entry.write(request.files['file'].read())
                print('three')

        return pagetext.format(sample=sample)
    except Exception as e:
        print(e)
        return 'whoops, your stack trace is: ' + str(e)


site.run(host='127.0.0.1', port=8080)
