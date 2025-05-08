from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=60, label="Full name")
    email     = forms.EmailField(label="Email")
    address   = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Shipping address"
    )
