from .models import Tag


def extras(request):
    tag_list = Tag.objects.all()
    return {"tag_list": tag_list}
