import os
import json
import requests

def get_data(uri):
    if not uri:
        print('Please Provide A URL/Endpoint')
        return

    response = requests.get(uri)

    if response.status_code == 200:
        response = json.loads(response.content)
        return response['data']
    else:
        print(f'URL Is Returning A {response.status_code}')
        return


def make_dir_with_avatar(dirName):
    for items in dirName:
        name = json.loads(items)
        dirName = f"{name['name']}"
        image = requests.get(f"{name['avatar']}").content
        if not dirName:
            print('Please Provide A Directory Name')
        else:
            if os.path.exists(dirName):
                print('User Already Exists Replacing Avatar')
                os.remove(f"{dirName}/avatar.jpg")
            else:
                os.mkdir(dirName)
            with open('avatar.jpg', 'wb') as handler:
                handler.write(image)
            os.rename('avatar.jpg', f'{dirName}/avatar.jpg')
            return True


def get_info(data):
    list = []
    Data = {}
    info = {}
    for item in data:
        firstname = item['first_name']
        lastname = item['last_name']
        id = item['id']

        dirName = f'{id} - {firstname} {lastname}'
        avatar = item['avatar']

        info["name"] = dirName
        info["avatar"] = avatar

        Data = json.dumps(info)

        list.append(Data)

    return list

userData = get_data('https://reqres.in/api/users')

dirName = get_info(userData)

make_dir_with_avatar(dirName)
