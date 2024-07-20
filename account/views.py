from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #ログインをしていなののであれば、行けないような装置
from .models import Profile
from .forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

#会員登録View
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response

#ログインView
class Login(LoginView):
    template_name = 'signup.html'
    def form_valid(self, form):
        messages.success(self.request, 'ログインしました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'エラーでログインできません。')
        return super().form_invalid(form)
    
#アカウントアップデート
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'account.html'
    fields = ('userid', 'email','password')
    success_url = '/account/'

    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()

#Profileアップデート
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'account.html'
    fields = ('user_name', 'address')
    success_url = '/account/' #これだけでは一般ユーザーもリンクを押せばupdateされてしまうようになる

    def get_object(self):
        self.kwargs['pk'] = self.request.user
        return super().get_object()

