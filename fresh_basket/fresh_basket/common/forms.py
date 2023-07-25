from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'review-textarea', 'placeholder': 'Write your review...'}),
            'rating': forms.NumberInput(attrs={'class': 'review-rating-input', 'min': 1, 'max': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not 1 <= rating <= 5:
            raise forms.ValidationError('Please provide a number between 1 and 5.')
        return rating