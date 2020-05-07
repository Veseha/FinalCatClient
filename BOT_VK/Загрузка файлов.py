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

    upload = vk_api.VkUpload(vk_session)
    photos = ['static/img/img.png', 'static/img/some_png.png']

    album = input('id album plz')
    group = input('id group plz')
    for i in photos:
        photo = upload.photo(i, album_id=album, group_id=group)
        vk_url = f"https://vk.com/photo{photo[0]['owner_id']}_{photo[0]['id']}"
        vk_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
        vk = vk_session.get_api()
        vk.wall.post(message="yanTestFUNC", attachments=[vk_id])
        print('>> error: 0 ')


if __name__ == '__main__':
    main()