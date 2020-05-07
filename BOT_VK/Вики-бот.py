import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import wikipedia


def main():
    vk_session = vk_api.VkApi(token=input('token plz'))
    lp = VkBotLongPoll(vk_session, input('group id:'))
    vk = vk_session.get_api()
    wikipedia.set_lang('ru')

    for event in lp.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"{str(wikipedia.page(event.obj.message['text']).content[:1000])}")


if __name__ == '__main__':
    main()