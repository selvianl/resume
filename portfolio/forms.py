from django.forms import ModelForm

from portfolio.models import Home, Works , Skills

class HomeForm(ModelForm):

    class Meta:
        model = Home
        fields = ['header', 'name']

    def cleaned_data(self):
        data = self.cleaned_data['name']
        return data
