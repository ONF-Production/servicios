from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name=models.CharField(max_length=180)
    first_name = models.CharField(max_length=180)
    state=models.BooleanField(default=True)

    def __str__(self):
        return  '%s %s' % (self.last_name, self.first_name)