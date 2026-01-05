from .models import Category

class CategoryService:
    
    @staticmethod
    def canCreateAndModify(user):
        return user.is_authenticated and user.role == 'Admin'

    @staticmethod
    def categoryList(user):
        categories = Category.objects.all()
        for c in categories:
            c.can_edit = CategoryService.canCreateAndModify(user)
            c.can_delete = c.can_edit
        
        return categories
    
    @staticmethod
    def createCategory(user, category):
        if not CategoryService.canCreateAndModify(user):
            raise PermissionError('Not allowed')
        return Category.objects.create(
            name=category['name']
        )
    
    @staticmethod
    def deleteCategory(user, category):
        if not CategoryService.canCreateAndModify(user):
            raise PermissionError('Not allowed')
        category.delete()