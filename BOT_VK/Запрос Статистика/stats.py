import vk_api
from gv import LOGIN, PASSWORD
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/m/<int:id>')
def vk_stat(id):
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    activities = {'likes': 0, 'comments': 0, 'subscribed': 0}
    ages = {'12-18': 0, '18-21': 0, '21-24': 0,
            '24-27': 0, '27-30': 0, '30-35': 0,
            '35-45': 0, '45-100': 0}
    response = vk.stats.get(group_id=id, fields="reach")
    if response:
        for item in response[:10]:
            if 'activity' in item:
                for act in item['activity']:
                    activities[act] += item['activity'][act]
                if 'age' in item['reach']:
                    for age in item['reach']['age']:
                        ages[age['value']] += age['count']
    return render_template('stats.html', activities=activities,
                           ages=ages, title='stats')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
