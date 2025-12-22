class DatabaseRouter:
    def db_for_write(self , model , **hints):

        if model.__name__=="UserModel":
            return "default"
        
        if model.__name__=="Product_Model":
            return "products_db"
        
        if model.__name__=="OrderModel":
            return "orders_db"
        return None
    def db_for_read(self, model, **hints):
        return self.db_for_write(model)