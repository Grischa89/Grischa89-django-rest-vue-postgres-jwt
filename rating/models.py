from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserAccount


class Rating(models.Model):
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, related_name='userrating',   on_delete=models.CASCADE) # change because jwt
    product = models.ForeignKey('product.Product', related_name='productrating', on_delete=models.CASCADE) 
    text = models.TextField(max_length = 2000, blank=True, default="")
    rate = models.FloatField(blank=True,  default=0)
    
    
    def __str__(self):
        return 'user={0}, product={1}, text={2}, rate={3}'.format(self.user, self.product, self.text, self.rate)

    