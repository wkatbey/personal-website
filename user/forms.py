from django.contrib.auth import UserCreationForm
from django.contrib.auth import User

class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
