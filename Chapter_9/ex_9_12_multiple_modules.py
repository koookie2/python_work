from ex_9_12_multiple_modules_module2 import Admin

admin = Admin('kavin', 'wesley', '01/03/2008', 15, 5040, 'male', 'can add post', 'can delete post', 'can ban user')
admin.privileges.show_privileges()

import random

print(random.getstate())