from .models import SlideComment,Slide,Member

class Comment:
    def get_related_comment(self,slide_ID):
        comments = SlideComment.objects.filter(slide_ID=slide_ID)
        return comments
    
    def save_comment(self,comment,slide_ID,member_ID):
        slide = Slide.objects.get(slide_ID=slide_ID)
        member = Member.objects.get(member_ID=member_ID)
        saving_comment = SlideComment(
            slide_ID = slide,
            member_ID = member,
            comment = comment,
        )
        saving_comment.save()