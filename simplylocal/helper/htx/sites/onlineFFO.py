from simplylocal.helper.htx.python.CheckBox import CheckBox
from simplylocal.helper.selenium.selenium import find_all_css, wait, write_by_id, press, select


class OnlineFFO:
    def __init__(self, context):
        self.context = context

    def online_ffo_menu_item(self):
        return find_all_css(self.context, "#form\:offo>tbody>tr>td>label")

    def select_ffo(self, ffo, checked):
        CheckBox("offo", self.context).select(ffo,checked)

    def add_ffo(self, ffo):
        wait(self.context)
        write_by_id(self.context, "addOffo", ffo)
        press(self.context, "add")
        wait(self.context)

    def count_ffo(self, ffo):
        count = 0
        wait(self.context)
        all_css = find_all_css(self.context, "#offo>tbody>tr>td>label")
        for label in all_css:
            if label.text == ffo:
                count += 1
        return count

    def is_checked(self, ffo):
        return CheckBox('offo', self.context).is_selected(ffo)

    def has_ffo(self, ffo):
        wait(self.context)
        all_css = find_all_css(self.context, "#offo>tbody>tr>td>label")
        for label in all_css:
            if label.text == ffo:
                return True

    def find_ffo(self, ffo):
        wait(self.context)
        all_css = find_all_css(self.context, "#offo>tbody>tr>td>label")
        for label in all_css:
            if label.text == ffo:
                return label

    def remove_ffo(self, ffo):
        write_by_id(self.context, "addOffo", ffo)
        press(self.context, "remove")
        wait(self.context)

    def save(self):
        press(self.context, "save")
