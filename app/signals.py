from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comment

#added for update products rating after every coment create
@receiver(post_save, sender=Comment)
def product_ratting_save(sender, instance, **kwargs):
    instance.product.rating_upd()

#if comment deleted, products rating should be changed
@receiver(post_delete, sender=Comment)
def product_rating_delete(sender, instance, **kwargs):
    instance.product.rating_upd()
