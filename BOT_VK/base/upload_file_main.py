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
    photo = upload.photo_wall(['Picture1.png']
                              )

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")
    vk = vk_session.get_api()
    vk.wall.post(message="Test", attachments=[vk_photo_id])


if __name__ == '__main__':
    main()