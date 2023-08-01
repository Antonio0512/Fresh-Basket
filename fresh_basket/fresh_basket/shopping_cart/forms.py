from django import forms


class AddToCartForms(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    weight = forms.DecimalField(initial=0.0, min_value=0.0, max_digits=10, decimal_places=2, required=False)
