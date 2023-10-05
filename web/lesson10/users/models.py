from PIL import Image

from django.contrib.auth.models import User
from django.db import models as m


class Profile(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE)
    avatar = m.ImageField(default='default_avatar.png', upload_to='profile_images')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
