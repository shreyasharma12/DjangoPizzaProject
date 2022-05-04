from django import forms 

from .models import Pizza, Topping

class CommentForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['pizza_name']
        labels = {'pizza_name':''}
        widgets = {'pizza_name': forms.Textarea(attrs={'cols':80})}

