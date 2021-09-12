from django import forms 

class PostTweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea, max_length=140)
    