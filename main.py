import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from app_users.models import *

user1 = User(
    name = 'name1',
    email = 'emailOne@gmail.com',
    role = 'Admin'
)

group1 = Group(
    group_name = "Group1"
)

user1.save()
group1.save()

user = User.objects.get(id=1)
group = Group.objects.get(id=1)

user.group.add(group)