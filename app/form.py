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

class RegisterForm(forms.Form):
    ID = forms.CharField(max_length=4)
    name=forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    
    def check_Password(self,password,c_password):
        if password == c_password:
            return True
        return False

    def check_ID(self,MID):
        try:
            member = Member.objects.get(member_ID=MID)
            return False
        except Member.DoesNotExist:
            pass
        return True

    def save(self,MID,name,password):
        Member.objects.create(
            member_ID=MID,
            member_name=name,
            member_password=password
        )