from django import forms
from . models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
#         "required": "Your Name cannot be empty!",
#         "max_length": "Please enter shorter name upto 50 characters!"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ["owner_comment"]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your Name cannot be empty!",
                "max_name": "Please enter shorter name upto 50 characters!"
            }
        }
