from django.forms import ModelForm

from portfolio.models import Home, Works , Skills, Blog



class HomeForm(ModelForm):

    class Meta:
        model = Home
        fields = "__all__"

class WorksForm (HomeForm):
    class Meta:
        model = Works
        fields = "__all__"

class SkillsForm(HomeForm):
    class Meta:
        model = Skills
        fields = "__all__"

class BlogForms(HomeForm):
    class Meta:
        model = Blog
        fields = "__all__"


