from django.db import models
SCHEMES = (
    ("Unipolar", 'Unipolar'),
    ("NRZ-L", 'NRZ-L'),
    ("NRZ-I", 'NRZ-I'),
    ("Polar RZ", 'Polar RZ'),
    ("Unipolar RZ", 'Unipolar RZ'),
    ("Manchester", 'Manchester'),
    ("Differential Manchester", 'Differential Manchester'),
    ("AMI", 'AMI'),
)



class Encoder(models.Model):
    custom = models.BooleanField(default=False, blank=True)
    custom_bits = models.CharField(max_length=256, blank=True)
    bit_size = models.IntegerField(blank=True, default=3)
    fixed_sequence = models.BooleanField(default=False, blank=True)
    fixed_size = models.IntegerField(blank=True)
    fixed_freq = models.IntegerField(blank=True)
    pos_logic = models.BooleanField(default=True, blank=True)
    scheme_choice = models.CharField(max_length=50,
                                     choices=SCHEMES,
                                     default="Unipolar")