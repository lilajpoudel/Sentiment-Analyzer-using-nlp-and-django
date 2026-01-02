from django import forms

class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), label="Enter your opinion")
