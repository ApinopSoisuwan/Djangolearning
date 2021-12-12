from django.db import models

# Create your models here.

class community_post (models.Model):
    first_bar = models.CharField(max_length=20)
    # formal id
    sec_bar = models.TextField(max_length=20)
    # *** Password 