from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=200)
    shipping_address2 = models.CharField(max_length=200, null = True, blank=True )
    shipping_city = models.CharField(max_length=200)
    shipping_state = models.CharField(max_length=200, null = True, blank=True)
    shipping_country = models.CharField(max_length=200)
    shipping_zipcode = models.CharField(max_length=200, null = True, blank=True)

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f"Shipping Address - {str(self.id)}"
    
def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping,sender=User)