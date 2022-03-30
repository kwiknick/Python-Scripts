from user import User
from post import Post

firstUser = User("nick@willard.com", "Nick Willard", "secretPassword", "BizOps Engineer")
firstUser.get_user_info()

secondUser = User("john@willard.com", "John Willard", "secretPassword", "BizOps Engineer")
secondUser.get_user_info()

new_post = Post("on a secret mission today", secondUser.name)
new_post.get_post_info()
