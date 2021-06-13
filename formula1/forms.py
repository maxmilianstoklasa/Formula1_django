from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Driver, Constructor


class DriverModelForm(ModelForm):
    def clean_driver_wins(self):
        data = self.cleaned_data['driver_wins']
        if data < 0 or data > 350:
            raise ValidationError('Incorrect number of victories')
        return data

    def clean_wdc(self):
        data = self.cleaned_data['wdc']
        if data < 0 or data > 20:
            raise ValidationError('Incorrect number of championships')
        return data

    class Meta:
        model = Driver
        fields = ['name', 'poster', 'nationality', 'birth', 'teams', 'driver_wins', 'wdc', 'biography']
        labels = {'poster': 'Driver photo'}