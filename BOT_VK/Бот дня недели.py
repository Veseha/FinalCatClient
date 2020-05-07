import vk_api
import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    vk_session = vk_api.VkApi(token=input('token plz'))
    lp = VkBotLongPoll(vk_session, input('group id:'))
    vk = vk_session.get_api()
    dt = datetime.datetime.now()

    day = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг',
           4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

    for event in lp.listen():
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"{day[datetime.datetime.strptime((event.obj.message['text']), '%Y-%m-%d').weekday()]}")


if __name__ == '__main__':
    main()