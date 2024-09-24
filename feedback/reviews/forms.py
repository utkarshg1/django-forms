from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
        "required": "Your Name cannot be empty!",
        "max_length": "Please enter shorter name upto 50 characters!"
    })
