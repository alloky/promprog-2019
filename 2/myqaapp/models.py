from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Question(models.Model):
	shortName = models.CharField(max_length = 20, validators=[MaxLengthValidator(20)])
	text = models.CharField(max_length = 3000, validators=[MaxLengthValidator(3000)])