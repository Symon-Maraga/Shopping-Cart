class Store:
    def __init__(self):
        self.shopping_lists = {}
        self.last_shopping_list_id = 0

    def add_shopping_list(self, shopping_list):
        self.last_shopping_list_id += 1
        self.shopping_list[self.last_shopping_list_id] = shopping_list
        shopping_list._id = self.last_shopping_list_id

    def delete_shopping_list(self, shopping_list_id):
        del self.shopping_list[shopping_list_id]

    def get_shopping_list(self, shopping_list_id):
        return self.shopping_list[shopping_list_id]

    def get_shopping_list(self):
        return self.shopping_list