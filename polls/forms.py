from django import forms
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'surname', 'author', 'body', 'email', 'password', 'student_id', 'header_image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), #, 'placeholder': 'This is Title Placeholder Stuff'
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),

        }

        def clean_name(self, *args, **kwargs):
            name = self.cleaned_data.get('name')
            if  "Darkhan1" in name:
                raise forms.ValidationError("This is not valid title")
            else:
                return name



