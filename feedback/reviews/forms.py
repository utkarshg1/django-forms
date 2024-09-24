from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
        "required": "Your Name cannot be empty!",
        "max_length": "Please enter shorter name upto 50 characters!"
    })
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
