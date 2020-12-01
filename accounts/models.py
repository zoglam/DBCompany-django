from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

        
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default=' ')
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    description = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

#Чек
class Check1(models.Model):
    name = models.CharField(max_length=50)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()
    
    def __str__(self):
        return self.name

#Платежное поручение
class Payment1(models.Model):
    name = models.CharField(max_length=50)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    check_name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    price_nds = models.FloatField(default=0)
    nds = models.FloatField(default=0)

    def __str__(self):
        return self.name

#Завод
class Factory(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Товар
class Good(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    id_factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Транспорт
class Transport(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    id_factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
