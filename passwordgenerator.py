import random
import string
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(15))
print "Your newly generated password is: " + password

