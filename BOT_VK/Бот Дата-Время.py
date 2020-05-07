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
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message:
                date, time, weekday = dt.strftime('%Y-%m-%d'), dt.strftime('%H:%M:%S'), dt.weekday()
                if "время" in event.obj.message['text'].lower() or "число" in event.obj.message['text'].lower() or \
                        "дата" in event.obj.message['text'].lower() or "день" in event.obj.message['text'].lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Сегодня {date}\n{day[weekday]}\nСейчас {time}")
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='input plz one of thehe are words: время», «число», «дата», «день». ok?')


if __name__ == '__main__':
    main()