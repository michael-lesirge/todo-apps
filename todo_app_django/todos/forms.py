from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    style = 'form-control'

    name = forms.CharField(max_length=24, widget=forms.TextInput({'class': style, 'placeholder': "Todo name"}))
    info = forms.CharField(required=False, widget=forms.Textarea({'class': style, 'rows': 3, 'placeholder': "extra info"}))
    complete_by_days = forms.IntegerField(required=False, min_value=0, max_value=999999999, label="How many days to complete", widget=forms.NumberInput({'class': style}))

    class Meta:
        model = Todo
        fields = ('name', 'info', 'complete_by_days')