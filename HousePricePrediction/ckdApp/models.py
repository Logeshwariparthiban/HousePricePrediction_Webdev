from django.db import models

# Create your models here.
class ckdModel(models.Model):
    area = models.FloatField()  # Numeric field for area
    bedrooms = models.FloatField()  # Numeric field for number of bedrooms
    bathrooms = models.FloatField()  # Numeric field for number of bathrooms
    stories = models.FloatField()  # Numeric field for number of stories
    parking = models.FloatField()  # Numeric field for parking space
    mainroad_yes = models.BooleanField(default=False)  # Default value False for presence of main road
    guestroom_yes = models.BooleanField(default=False)  # Default value False for presence of guestroom
    basement_yes = models.BooleanField(default=False)  # Default value False for presence of basement
    hotwaterheating_yes = models.BooleanField(default=False)  # Default value False for hot water heating
    airconditioning_yes = models.BooleanField(default=False)  # Default value False for air conditioning
    prefarea_yes = models.BooleanField(default=False)  # Default value False for preferred area
    furnishingstatus_semi_furnished = models.BooleanField(default=False)  # Default value False for semi-furnished status
    furnishingstatus_unfurnished = models.BooleanField(default=False)  # Default value False for unfurnished status
