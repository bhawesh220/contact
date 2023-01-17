from django import forms
class contactform(forms.Form):
    sname=forms.CharField()
    label='Enter your name'
    widget=forms.TextInput(
        attrs={
            'placeholder':'your name',
            'class':'form-control'
        }
    )

    sroll = forms.IntegerField()
    label = 'Enter your rollno'
    widget = forms.NumberInput(
        attrs={
            'placeholder': 'your rollno',
            'class': 'form-control'
        }
    )

    email = forms.EmailField()
    label = 'Enter your name'
    widget = forms.EmailInput(
        attrs={
            'placeholder': 'your emailid',
            'class': 'form-control'
        }
    )