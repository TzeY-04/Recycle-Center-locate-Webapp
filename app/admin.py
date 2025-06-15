from django.contrib import admin
from django import forms
from .models import Member,Slide,RecycleCenter,SlideComment,Region,NewFoundRecycleCenter,Notification
import os
from django.conf import settings
from django.utils.html import format_html
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_ID', 'member_name', 'member_password')
    
@admin.register(SlideComment)
class SlideCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'slide_ID', 'member_ID', 'comment')
    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region', 'region_latitude', 'region_longitude')
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('member_ID', 'not_title', 'not_description')
    


class SlideAdminForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, help_text="Upload new image")
    remove_image = forms.BooleanField(required=False, label="Remove existing image")

    class Meta:
        model = Slide
        fields = '__all__'
        
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    form = SlideAdminForm
    list_display = ('slide_ID', 'slide_title', 'slide_type', 'preview_model')
    readonly_fields = ('preview_model',)

    def save_model(self, request, obj, form, change):
        image = form.cleaned_data.get('upload_image')
        remove = form.cleaned_data.get('remove_image')

        # Two folder file path
        static_folder = os.path.join(settings.BASE_DIR, 'static', 'images')
        staticfiles_folder = os.path.join(settings.BASE_DIR, 'staticfiles', 'images')
        
        static_filepath= os.path.join(static_folder, f"{obj.slide_ID}.png")
        staticfiles_filepath= os.path.join(staticfiles_folder, f"{obj.slide_ID}.png")
        

        # Delete old image if remove checkbox is checked
        if remove:
            for path in [static_filepath, staticfiles_filepath]:
                if os.path.exists(path):
                    os.remove(path)

        super().save_model(request, obj, form, change)
        
        if image:
            #Save image into static/images/
            os.makedirs(static_folder, exist_ok=True)
            os.makedirs(staticfiles_folder, exist_ok=True)
            
            #Read the image
            image_data = image.read()
            
            with open(static_filepath, 'wb') as f1:
                f1.write(image_data)
            
            with open(staticfiles_filepath, 'wb') as f2:
                f2.write(image_data)

    @admin.display(description="Current image")
    def preview_model(self, obj):
        filename = f'{obj.slide_ID}.png'
        file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'images', filename)

        if os.path.exists(file_path):
            #Use version to prevent image still shown after delete because still exist in cache
            version = int(os.path.getmtime(file_path))  # Use file's modified time
            return format_html('<img src="/static/images/{}" width="120"/>', filename, version)
        else:
            return format_html('<span style="color: gray;">No image</span>')



@admin.register(RecycleCenter)
class RecycleCenterAdmin(admin.ModelAdmin):
    list_display = ('rc_ID', 'rc_name', 'rc_region', 'rc_address')

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