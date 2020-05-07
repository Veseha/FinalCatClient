import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import wikipedia
import random
from gv import LOGIN, PASSWORD


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return 1

    vk = vk_session.get_api()
    id_group = input("id_group input: ")
    response = vk.photos.get(album_id=input("id_album input heree: "), group_id=id_group)
    photo_to_send = ''
    if response['items']:
        photo_to_send = random.choice(
            [f"photo{i['owner_id']}_{i['id']}" for i in response['items']]
        )
    lp = VkBotLongPoll(vk_session, id_group)

    for event in lp.listen():
        vk = vk_session.get_api()

        if event.obj.message:
            name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']

            city = None
            try:
                city = vk.users.get(user_id=event.obj.message['from_id'], fields='city')[0]['city']['title']
            except Exception:
                pass
            vk.messages.send(peer_id=event.obj.message['from_id'],
                                 message=f'Привет, {name}!',
                                 attachment=photo_to_send)


if __name__ == '__main__':
    main()