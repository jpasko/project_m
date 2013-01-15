from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Attach a profile to the User model, and ensure that it's
# created whenever a new user is created.
class UserProfile(models.Model):
    # Required to associate with a unique user.
    user = models.OneToOneField(User)
    # Locate the user.
    latitude = models.DecimalField(default=0, max_digits=7, decimal_places=4)
    longitude = models.DecimalField(default=0, max_digits=7, decimal_places=4)

    def __unicode__(self):
        return u'Profile for %s' % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
