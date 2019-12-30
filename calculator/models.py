from django.db import models

FOOD_CHOICES = (
  ("beef", "Beef"),
  ("lamb", "Lamb"),
  ("cheese", "Cheese"),
  ("farmed salmon", "Farmed Salmon"),
  ("turkey", "Turkey"),
  ("chicken", "Chicken"),
  ("canned tuna", "Canned Tuna"),
  ("eggs", "Eggs"),
  ("potatoes", "Potatoes"),
  ("rice", "Rice"),
  ("peanut butter", "Peanut Butter"),
  ("nuts", "Nuts"),
  ("yogurt", "Yogurt"),
  ("broccoli", "Broccoli"),
  ("tofu", "Tofu"),
  ("dry beans", "Dry Beans"),
  ("milk (2%)", "Milk (2%)"),
  ("tomatoes", "Tomatoes"),
  ("lentils", "Lentils"),
)

# Create your models here.

class food(models.Model):
  name = models.CharField(max_length=200)
  emissons = models.IntegerField(default=0)


class transport(models.Model):
  name = models.CharField(max_length=200)
  emissons = models.IntegerField(default=0)
