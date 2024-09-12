from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # class Meta:
    #     db_table = "users"

    def __str__(self):
        return self.username
    
