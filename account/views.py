from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #ログインをしていなののであれば、行けないような装置
from .models import Profile
from .forms import UserCreationForm
from django.contrib.auth import get_user_model


#会員登録View
class SignUpView(CreateView):
    from_class = UserCreationForm
    success_url = '/login/'
    template_name = 'signup.html'

    def form_valid(self, form):
        return super().form_valid(form)

#ログインView
class Login(LoginView):
    template_name = 'signup.html'
    def form_invalid(self, form):
        return super().form_invalid(form)#pwのvalidationを入れる予定
    def form_invalid(self, form):
        return super().form_invalid(form)

    
#アカウントアップデート
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'account.html'
    fields = ('username', 'email',)
    success_url = '/account/'

    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()

#Profileアップデート
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile.html'
    fields = ('user_name', 'address')
    success_url = '/profile/' #これだけでは一般ユーザーもリンクを押せばupdateされてしまうようになる

    def get_object(self):
        self.kwargs['pk'] = self.request.user
        return super().get_object()

