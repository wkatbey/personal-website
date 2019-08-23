from .models import BlogEntry, Category

def get_blogs_by_category(category):
    
    # Get all related categories
    categories = []
    blogs = BlogEntry.objects.filter(category=category)

    current_category = category
    while current_category:
        categories.append(current_category)
        blogs |= get_child_category_blogs(current_category.children)



def get_child_category_blogs(children):
    for child in children:
        blogs |= BlogEntry.objects.filter(category=child)
        get_child_category_blogs(child.children)

    return blogs