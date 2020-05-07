import vk_api
from gv import PASSWORD, LOGIN


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """

    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    response = vk.photos.get(album_id=input('plz input id album'), group_id=input('id group'))
    if response['items']:
        for i in response['items']:
            print(i['sizes'][0]['url'],
                  f"{i['sizes'][0]['width']}x{i['sizes'][0]['height']}")


if __name__ == '__main__':
    main()