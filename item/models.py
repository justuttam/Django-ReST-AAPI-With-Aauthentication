from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify


class Item(models.Model):
    name: str = models.CharField(max_length=100)
    description: str = models.TextField(default='This is item description.', max_length=250)
    price: float = models.FloatField(max_length=5)
    item_slug: str = models.SlugField(max_length=20, null=True, blank=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


@receiver(models.signals.pre_save, sender=Item)
def pre_save_receiver(sender, instance, *args, **kwargs):
    # print(f"inside signal: {instance.item_slug}")
    if not instance.item_slug:
        instance.item_slug = slugify(instance.name.replace(' ', '-'))
