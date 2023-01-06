from django import forms
from .models import Encoder


class EncoderForm(forms.ModelForm):
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
    custom_bits = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "101010110",
        "disabled": "disabled",

    }), required=True)
    bit_size = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",

    }), required=True)
    scheme_choice = forms.CharField(widget=forms.Select(attrs={
        "class": "form-control",
    },
        choices=SCHEMES))

    class Meta:
        model = Encoder
        fields = ["custom_bits", "custom",
                  "bit_size", "scheme_choice", "pos_logic"]
