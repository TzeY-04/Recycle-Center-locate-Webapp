from django.contrib import admin
from django import forms
from .models import Member,Slide,RecycleCenter,SlideComment,Region,NewFoundRecycleCenter,Notification

# Register your models here.

admin.site.register(Member)
admin.site.register(SlideComment)
admin.site.register(Region)
admin.site.register(Notification)

@admin.register(Slide)
class Slide(admin.ModelAdmin):
    list_display = ('slide_ID', 'slide_title', 'slide_type')

@admin.register(RecycleCenter)
class RecycleCenterAdmin(admin.ModelAdmin):
    list_display = ('rc_name', 'rc_region', 'rc_address')

class NewFoundRecycleCenterAdminForm(forms.ModelForm):
    rc_ID = forms.CharField(max_length=4, required=True, help_text="Enter a 4-character ID for the new center")

    class Meta:
        model = NewFoundRecycleCenter
        fields = '__all__'

@admin.register(NewFoundRecycleCenter)
class NewFoundRecycleCenterAdmin(admin.ModelAdmin):
    form = NewFoundRecycleCenterAdminForm
    list_display = ('rc_name', 'rc_region', 'rc_submitby')

    def save_model(self, request, obj, form, change):
        # Get the rc_ID that admin entered
        rc_ID = form.cleaned_data.get("rc_ID")

        # Create new record in RecycleCenter
        RecycleCenter.objects.create(
            rc_ID=rc_ID,
            rc_latitude=obj.rc_latitude,
            rc_longitude=obj.rc_longitude,
            rc_address=obj.rc_address,
            rc_name=obj.rc_name,
            rc_region=obj.rc_region
        )

        # Send notification to the user
        Notification.objects.create(
            member_ID=obj.rc_submitby,
            not_title="Recycle Center Approved",
            not_description=f"Your submission '{obj.rc_name}' has been approved and added to the system!"
        )

        # Delete the original suggestion
        obj.delete()

    def delete_model(self, request, obj):
        # Create a notification before deletion
        Notification.objects.create(
            member_ID=obj.rc_submitby,
            not_title="Recycle Center Suggestion Rejected",
            not_description=f"Your submission '{obj.rc_name}' has been rejected by admin and was not approved."
        )

        # Proceed with deletion
        obj.delete()