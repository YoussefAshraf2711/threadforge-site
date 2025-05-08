from django import forms

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=20,
        initial=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm",
            "style": "width: 4rem;",
        })
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
