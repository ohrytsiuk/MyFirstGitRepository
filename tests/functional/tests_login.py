"""
Functional tests for logging users
"""

import requests

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser, InitUsers, InitInvalidUsers


class Test(ApiTestBase):

    def test_login_positive(self):
        """
        Logging right users (positive test). If got user token test pass
        """
        for user, password in InitUsers.users.items():
            login = self.login(user, password)
            if login.status_code == 200:
                if "ERROR, user not found" in login.text:
                    self.assertFalse(True)
                elif "ERROR, user locked" in login.text:
                    self.assertFalse(True)
                else:
                    self.assertTrue(True)
            else:
                self.assertFalse(True)

    def test_login_negative(self):
        """
        Logging invalid users (negative test). If user not found or user locked test pass
        """
        for user, password in InitInvalidUsers.invalid_users.items():
            login = self.login(user, password)
            if login.status_code == 200:
                if "ERROR, user not found" in login.text:
                    self.assertTrue(True)
                elif "ERROR, user locked" in login.text:
                    self.assertFalse(True)
                else:
                    self.assertFalse(True)
            else:
                self.assertFalse(True)

    def test_login_admins(self):
        """

        """
        pass
        # login = self.login(DefaultUser.user, DefaultUser.password)
        # params = login.json()
        # params["token"] = params.pop("content")
        # req = requests.get("localhost:8080/login/admins?token=" + params.get("token"))
        # print(req.text)

    def test_login_users(self):
        """

        """
        pass

    def test_login_tockens(self):
        """

        """
        pass
