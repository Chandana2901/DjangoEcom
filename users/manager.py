from django.contrib.auth.models import BaseUserManager, Group


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, role='Consumer', **extra):
        if not email:
            return ValueError('Email is required')

        email = self.normalize_email(email=email)
        user = self.model(email=email, role=role, **extra)
        user.set_password(password)
        user.save(using=self._db)
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            pass
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, role='Admin', **extra_fields)

