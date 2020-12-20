from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# sender sends info in
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs): # sender is the model
    # print('sender', sender)
    # print('instance', instance)
    if created: 
        Profile.objects.create(user=instance)


# To actually add the person to each other's friend list


# # To add the game to person's list
# @receiver(post_save, sender=Game)
# def post_save_add_game(sender, instance, created, **kwargs):
#     print('sender', sender)
#     print('instance', instance)
#     if created: 
#         Game.objects.create(user=instance)