from django.db import models

# Create your models here.

Constituency = (
    ("Harare", "Harare"),
    ("MashWest", "MashWest"),
    ("MashEast", "MashEast"),
    ("MashCentral", "MashCentral"),
    ("Manicaland", "Manicaland"),
)


class VotersRoll(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    constituency = models.CharField(choices=Constituency, max_length=300)
    is_registered = models.BooleanField(default=True)
    id_number = models.CharField(max_length=300)

    def __str__(self):
        return self.name
