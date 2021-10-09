import pytest
from faker import Faker

from wework_testpo.po.app import App
from wework_testpo.po.main_page import MainPage


class TestDeleteMember:

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main= self.app.start().goto_main()

    def teardown(self):
        self.app.back()


    def teardown_class(self):
        pass

    @pytest.mark.parametrize('username',['EEE','eeee','李四'])
    def test_delete_member(self,username):
        result = self.main.goto_addresslist().goto_manageaddress().goto_edit_member(username).delete_member().get_result()
        assert username not in result