from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.selenium.selenium import visit, press, write_by_id


class Login:
    def __init__(self, context):
        self.context = context
        super().__init__()

    def _log_in(self, login="ba@nemesese.de"):
        Navigation(self.context).visit_site("login")
        write_by_id(self.context, "j_username", login)
        write_by_id(self.context, "j_password", "test1234")
        press(self.context, "login")

    def is_logged_in(self, ):
        Navigation(self.context).visit_site("welcome")
        return "Eingeloggt als" in self.context.driver.page_source

    def log_out(self, ):
        if self.is_logged_in():
            press(self.context, "name")
        pass

    def log_in(self, login=None):
        if self.is_logged_in():
            self.log_out()
        if login:
            self._log_in(login)
        else:
            self._log_in()


