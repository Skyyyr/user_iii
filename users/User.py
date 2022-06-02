import datetime

# 2. Create two subclasses `PremiumUser` and `FreeUser` that will inherit from `User`.
# 3. Override the `add_post` method for `FreeUser` so that an instance of `FreeUser` is only able to make two posts.
# 4. In the `runner.py` file, import `FreeUser` and `PremiumUser` and create at least one instance of each.
# 5. Add tests.


USER_POST_TITLE = "\t\t All my posts: \n"
ALL_USER_POST_TITLE = "\t\t All user posts: \n"

class User:
    all_user_posts = []

    def __init__(self, user_name, user_email):
        self.name = user_name
        self.email = user_email
        self.posts = []
        self.post_amount = 0

    def __str__(self):
        return f"I'm {self.name} with email: {self.email}. {self.post_amount} and posts: {self.posts}"
    
    def addPost(self, user_text):  
        name = self.name
        email = self.email
        # imported datetime above; set total_time variable
        total_time = datetime.datetime.now()
        # strftime() method to format datetime object; %c parameter
        time = total_time.strftime("%c")
        self.post_amount += 1
        post_id = self.post_amount
        self.posts.append({"name": name, "text":user_text, "time": time, "id": post_id})
        User.all_user_posts.append({"name": name, "text":user_text, "time": time, "id": post_id})
        
    def getUserPosts(self):
        posts_str = USER_POST_TITLE
        for i in range(len(self.posts)):
            name = self.posts[i]["name"]
            text = self.posts[i]["text"]
            time = self.posts[i]["time"]
            id = self.posts[i]["id"]
            posts_str += f"{name} posted at {time}\npost id: {id}:\n{text}\n\n"
        return posts_str

    def getAllUserPosts(self):
        user_posts_str = ALL_USER_POST_TITLE
        for i in range(len(User.all_user_posts)):
            name = User.all_user_posts[i]["name"]
            text = User.all_user_posts[i]["text"]
            time = User.all_user_posts[i]["time"]
            user_posts_str += f"{name} posted at {time}\n{text}\n\n"
        return user_posts_str

    def removeUserPost(self, num):
        for i in range(len(self.posts)):
            if(self.posts[i]["id"] == num):
                del self.posts[i]
                break
        for x in reversed(range(len(User.all_user_posts))):
            post = User.all_user_posts
            if(post[x]["id"] == num and post[x]["name"] == self.name):
                del post[x]
                break




