"""
PyBites 19. Write a simple property

Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!
"""



from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expire):
        self.name = name
        self.expire = expire
    
    @property
    def expired(self):
        return self.expire < NOW
        
        
        
