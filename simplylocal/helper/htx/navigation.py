from simplylocal.environment import config_map

from simplylocal.helper.selenium.selenium import visit, visit_no_wait


def parameters(parameter):
    site = ""
    if parameter:
        site += "?"
    for param in parameter:
        site += param
        site += "="
        site += parameter[param]
        site += "&"
    return site
    pass


class Navigation:
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.sites = {
            'onlineFFO': 'internal/onlineFulfillment.xhtml',
            'welcome': 'index.xhtml',
            'retailerEdit': 'slretailershop/retaileredit.xhtml',
            'productedit': 'product/productedit.xhtml',
            'login': 'login.xhtml'
        }

    def visit_site(self, site, parameter=None, wait=True):
        site_ = config_map()['url']
        if site not in self.sites:
            print("can't find " + site)
        site_ += self.sites[site]
        if parameter:
            site_ += parameters(parameter)
        if wait:
            visit(self.context, site_)
        else:
            visit_no_wait(self.context, site_)
