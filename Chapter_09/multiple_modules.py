from admin import Admin
from users import User
admin = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
admin.describe_user()
admin.privileges.show_privileges()
