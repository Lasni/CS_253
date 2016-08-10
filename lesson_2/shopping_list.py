from jinja_main_handler import *


class ShoppingListHandler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items=items)

