from users.User import User

class FreeUser(User):

    def addPost(self, user_text):
        # print(self.post_amount)
        if(self.post_amount >= 2):
            return 
        super().addPost(user_text)
