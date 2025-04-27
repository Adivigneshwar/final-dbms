from django.db import models
class Cate(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self) :
        return self.name
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

    @property
    def description(self):
        return self.content

    def __str__(self) :
        return self.title
class Cart:
    """
    A cart class to handle shopping cart operations
    """
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get('cart')
        
        # If user is starting a new session
        if not cart:
            cart = self.session['cart'] = {}
            
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 
                'price': str(product.price),
                'name': product.name
            }
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            
        self.save()
    
    def save(self):
        """
        Mark the session as modified to ensure it gets saved
        """
        self.session.modified = True
    
    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database
        """
        product_ids = self.cart.keys()
        
        for product_id in product_ids:
            yield self.cart[product_id]
    
    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Calculate the total cost of items in the cart
        """
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        """
        Clear the cart
        """
        del self.session['cart']
        self.save()