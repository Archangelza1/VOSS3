import unittest
import os
import shutil

from create import get_info,make_dir_with_avatar


class GetInfo(unittest.TestCase):
    def test(self):

        initialdata = [
            {
                "id":1,
                "email":"george.bluth@reqres.in",
                "first_name":"George",
                "last_name":"Bluth",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"
            },
            {
                "id":2,
                "email":"janet.weaver@reqres.in",
                "first_name":"Janet",
                "last_name":"Weaver",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
            },
            {
                "id":3,
                "email":"emma.wong@reqres.in",
                "first_name":"Emma",
                "last_name":"Wong",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg"
            },
            {
                "id":4,
                "email":"eve.holt@reqres.in",
                "first_name":"Eve",
                "last_name":"Holt",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"
            },
            {
                "id":5,
                "email":"charles.morris@reqres.in",
                "first_name":"Charles",
                "last_name":"Morris",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg"
            },
            {
                "id":6,
                "email":"tracey.ramos@reqres.in",
                "first_name":"Tracey",
                "last_name":"Ramos",
                "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg"
            }
        ]

        finaldata = [
            "{\"name\": \"1 - George Bluth\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg\"}",
            "{\"name\": \"2 - Janet Weaver\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg\"}",
            "{\"name\": \"3 - Emma Wong\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg\"}",
            "{\"name\": \"4 - Eve Holt\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg\"}",
            "{\"name\": \"5 - Charles Morris\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg\"}",
            "{\"name\": \"6 - Tracey Ramos\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg\"}"
        ]

        self.assertEqual(get_info(initialdata), finaldata)

class CreateAvatarAndFolders(unittest.TestCase):
    def setUp(self):
        if os.path.exists('99 - Test'):
            shutil.rmtree('99 - Test')
    def test(self):

        finaldata = [
            "{\"name\": \"99 - Test\", \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg\"}"
        ]


        make_dir_with_avatar(finaldata)

        self.assertTrue(os.path.exists('99 - Test'))
        self.assertTrue(os.path.isfile('99 - Test/avatar.jpg'))





if __name__ == '__main__':
    unittest.main()
