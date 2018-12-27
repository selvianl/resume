from django import forms
from portfolio.works.models import Works


class WorksForm (forms.ModelForm):
    class Meta:
        model = Works
        fields = "__all__"
