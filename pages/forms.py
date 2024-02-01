from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' : 'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'email@something.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Messsage'}))