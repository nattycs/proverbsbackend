from .models import Post
from .logic import random_string_generator, unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)