from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class MainUserManager(BaseUserManager):
    def create_user(self,full_name,username=None,password=None):
        user = self.model(username=username, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

class MainUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=555, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True, blank=False,null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=50, blank=True,null=True)
    phone = models.CharField(max_length=50, blank=True,null=True)
    objects = MainUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return '{} {}'.format(self.username, self.full_name)

    def save(self, *args, **kwargs):
         super(MainUser, self).save(*args, **kwargs)

    def update(self, **kwargs):
        for i in ['full_name', 'username', 'is_active']:
            if kwargs.get(i):
                setattr(self, i, kwargs[i])
        self.save()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'