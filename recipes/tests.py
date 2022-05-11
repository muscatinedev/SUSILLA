from django.test import TestCase
from django.contrib.auth import get_user_model

User= get_user_model()
print (User)
class UserTestCase(TestCase):
    def sepUp(self):
        self.user_a = User.object.createUser('cfe', password='abc123')



    # def test_user_pw(self):
    #     checked = self.user_a.check_password("abc123")
    #     self.assertTrue(checked)



