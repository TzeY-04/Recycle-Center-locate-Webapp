from django import forms
from .models import Member

class LoginForm(forms.Form):
    ID = forms.CharField(max_length=4)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def verify_Member(self,MID,Mpassword):
        try:
            member = Member.objects.get(member_ID=MID)
            if member.member_password == Mpassword:
                self.ID = member.member_ID 
                return True
        except Member.DoesNotExist:
            pass
        return False