import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


def main():
    vk_session = vk_api.VkApi(token=input('token plz'))
    lp = VkBotLongPoll(vk_session, input('group id:'))
    vk = vk_session.get_api()

    for event in lp.listen():
        if event.obj.message:
            name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']
            city = ''
            try:
                city = vk.users.get(user_id=event.obj.message['from_id'], fields='city')[0]['city']['title']
            except Exception as e:
                print('err: ' + str(e))
            if city:
                vk.messages.send(peer_id=event.obj.message['from_id'], message=f'Привет, {name}! Как поживает {city}?')
            else:
                vk.messages.send(peer_id=event.obj.message['from_id'], message=f'Привет, {name}!')


if __name__ == '__main__':
    main()