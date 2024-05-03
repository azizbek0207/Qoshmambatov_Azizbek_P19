from django.db.models import Model
from django.forms import CharField


# Create your models here.
class InstaUser(Model):
    name = CharField(max_length=255)