class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session cart if it exists
        cart = self.session.get('session_key')

        # If no cart in session, create a new empty one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available across all views/pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
