from faker import Faker

from testpo.page.app import App


class TestAddContact:

    def setup_class(self):
        self.fake=Faker('zh_CN')
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)


    def teardown_class(self):
        self.app.quit()

    def test_addcontact(self):
        name =self.fake.name()
        phone = self.fake.phone_number()
        result = self.main.goto_addresslist().goto_addmember().click_addmember_menual().edit_member(name,phone).get_toast_result()