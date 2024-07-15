# session for cart
class Cart():
    def __init__(self,request):
        self.session = request.session
        # Returning user - obtain his/her existing session key
        cart = self.session.get("session_key")


        if "session_key" not in request.session:
            # New user - create new session key
            cart = self.session["session_key"] = {}
    
        self.cart = cart