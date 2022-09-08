def pretty_name(func_name: str, *args, **kwargs):
    func_name = str(func_name)
    # func_name = func_name[0].upper() + func_name[1:] Сначала сделал так, потом прочитал про метод capitalize
    func_name = func_name.replace(",", " ").capitalize()
    print(func_name, end=" ")
    for name_arg in args:
       print(name_arg, end=" ")
    print()


def open_browser(browser_name):
    pretty_name(browser_name)


def go_to_companyname_homepage(page_url):
    pretty_name(go_to_companyname_homepage.__name__, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    pretty_name(find_registration_button_on_login_page.__name__, page_url, button_text)


open_browser("chrome")

go_to_companyname_homepage("https://qa.guru/pl/teach/control/lesson/view?id=252112288&editMode=0")

find_registration_button_on_login_page("https://qa.guru/python", "Начать обучение")

