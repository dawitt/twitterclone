from django import forms 

class PostTweetForm(forms.Form):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows':'3', 'col':'9', 'placeholder':'What\'s on your mind... '
    }), max_length=140)
    