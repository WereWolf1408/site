from django.forms import ModelForm, TextInput
from forum.models import Forum, ExtendForum



class NewThem(ModelForm):
    class Meta:
        model = Forum
        fields = ['them_name']
        widgets = {
            'them_name': TextInput(attrs={'class': 'new_them_title'}),
        }


class ExtendNewThem(ModelForm):
    class Meta:
        model = ExtendForum
        fields = ['them_name']
        widgets = {
            'them_name': TextInput(attrs={'class': 'new_them_title'}),
        }