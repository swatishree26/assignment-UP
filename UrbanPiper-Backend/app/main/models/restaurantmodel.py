from ..import db

class Category(db.Model):
    __tablename__ = "food_categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
  
    
    
    def __init__(self, name):
        self.name = dct['name']
     
        
    def put(self):
        db.session.add(self)
        db.session.commit()



class Item(db.Model):
    __tablename__ = "food_items"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("food_categories.id"))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.String(100))
    food_type = db.Column(db.String(10))
    
    def __init__(self, name, description, price, food_type):
        self.name = dct['name']
        self.description = dct['description']
        self.price = dct['price']
        self.food_type = dct["food_type"]

    def put(self):
        db.session.add(self)
        d.session(commit())




        # Insert Into food_categories Values('1', 'Chicken and Fish Burger');
        # Insert Into food_categories Values('2', 'King Delight Burger');
        # Insert Into food_categories Values('3', 'Veggie Burger');
        # Insert Into food_categories Values('4', 'Sweets');
        # Insert Into food_categories Values('5', 'Beverages');


        # Insert Into food_items Values('1', '1','Chicken Tikka Burger', 'Burger featured with Chicken Tikka patty topped with juicy tomato', '200', 'NonVeg');
        # Insert Into food_items Values('2', '1','Fish Tikka Burger', 'Burger featured with Fish Tikka patty topped with juicy cherry tomato', '255' , 'NonVeg');
        # Insert Into food_items Values('3', '4','Motichur Laddoo', 'Pure Ghee', '90', 'Veg');
        # Insert Into food_items Values('4', '4','Kaju Katli', 'Made with Pure Ghee and Fresh Kaju', '450', 'Veg');
        
     
   