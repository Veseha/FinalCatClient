from flask import Flask, render_template

site = Flask(__name__)
site.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@site.route('/')
@site.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@site.route('/list_prof/<key>/')
@site.route('/list_prof')
def list_prof(key=None):
    if key in ['ol', 'ul']:
        profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                  'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                  'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                  'штурман', 'пилот дронов']
        return render_template('list.html', title=key, key=key, profs=profs)
    else:
        return render_template('index.html', title=key)




site.run(host='127.0.0.1', port=8080)
