from .models import Slide

class Slides:
    def createSlide(self):
        pass

class paperSlide(Slides):
    def createSlide(self):
        pass

class plasticSlide(Slides):
    def createSlide(self):
        pass

class canSlide(Slides):
    def createSlide(self):
        pass

class SlideFactory:
    def get_Type(self, slide_type: str):
        if slide_type == "paper":
            return paperSlide()
        elif slide_type == "plastic":
            return plasticSlide()
        elif slide_type == "can":
            return canSlide()
        else:
            return None

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