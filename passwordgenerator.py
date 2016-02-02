from strgen import StringGenerator as SG
SG("[\w\p\d]{20}").render()

import random
import string
password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

from strgen import StringGenerator as SG
SG('[\u\d]{10}').render()
