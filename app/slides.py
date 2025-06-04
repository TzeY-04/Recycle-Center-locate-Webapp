from .models import Slide

class SearchSlide:
    def search_slidetype(self,slide_type):
        related_slides = Slide.objects.filter(slide_type=slide_type)
        return related_slides
        
    def search_slidetitle(self,slide_word):
        related_slides = Slide.objects.filter(slide_title__icontains=slide_word)
        return related_slides

    def get_slide(self,slide_ID):
        slide = Slide.objects.get(slide_ID=slide_ID)
        return slide