from store.models import Category
def categories(request):
    categories = Category.items.all()

    context = {
        'categories': categories
    }

    return context