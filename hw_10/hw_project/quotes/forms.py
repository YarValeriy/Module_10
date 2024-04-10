from django import forms
from .models import Author, Quote


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'born_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].required = True
        self.fields['born_date'].required = False
        self.fields['born_location'].required = False
        self.fields['description'].required = False

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if Author.objects.filter(fullname=fullname).exists():
            raise forms.ValidationError("An author with this fullname already exists.")
        return fullname


class QuoteForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by comma'}), required=False)

    class Meta:
        model = Quote
        fields = ['quote', 'author']

    def clean_tags(self):
        tags_input = self.cleaned_data.get('tags', '')
        if isinstance(tags_input, str):
            tags = [tag.strip() for tag in tags_input.split(',')]
        elif isinstance(tags_input, list):
            tags = [tag.strip() for tag in tags_input if isinstance(tag, str)]
        else:
            tags = []
        return tags



