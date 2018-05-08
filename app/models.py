from django.db import models

# Create your models here.
class Resource(models.Model):
    # id = models.IntegerField()
    user_id = models.CharField(max_length=255)                         
    service_id =  models.CharField(max_length=255)
    instance_id = models.CharField(max_length=255)
    class Meta:
        db_table = 'resource'
