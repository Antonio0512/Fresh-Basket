from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'detail-quantity-input'}),
                                  initial=1)
    weight = forms.DecimalField(min_value=0.0,
                                widget=forms.NumberInput(attrs={'class': 'detail-quantity-input', 'step': '0.01'}))
