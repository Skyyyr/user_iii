from User import User

class PremiumUser(User):

    def addPost(self, user_text):
        super().addPost(f"Premium user:\n{user_text}")