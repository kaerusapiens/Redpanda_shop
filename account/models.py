from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserManager(BaseUserManager):
    def create_user(self, userid, email, password=None):
        if not email:
            raise ValueError('emailは必須です')
        user = self.model(userid=userid, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, email, password=None):
        user = self.create_user(userid, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    EMAIL_FILED = 'email'
    REQUIRED_FIELDS = ['email',"userid"]

    def __str__(self):
        return self.userid
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class Profile(models.Model):
    #1対1の関係性
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(default="user_name",blank=True,max_length=500)
    address = models.CharField(default="shipping_address",blank=True,max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_name


# oneTooneを同時に作成
#post_save ->実行されるタイミング
@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
