from django.contrib.auth.forms import UserChangeForm,UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    REG_A, REG_B, REG_C, REG_D, REG_E = '서울', '대전', '대구', '부산', '구미'
    REGION_CHOICES = [(REG_A, '서울'), (REG_B, '대전'), (REG_C, '대구'), (REG_D, '부산'), (REG_E, '구미')]
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select(attrs={'class': 'my-region form-control'}))

    GEN1, GEN2, GEN3, GEN4, GEN5, GEN6, GEN7, GEN8, GEN9, GEN10 = '액션', '애니메이션', '코미디', '범죄', '공포', '드라마', '로맨스', 'SF', '가족', '기타'
    GENRE_LIKE = [(GEN1, '액션'), (GEN2, '애니메이션'), (GEN3, '코미디'), (GEN4, '범죄'), (GEN5, '공포'), (GEN6, '드라마'), (GEN7, '로맨스'), (GEN8, 'SF'), (GEN9, '가족'), (GEN10, '기타')]
    GENRE_DISLIKE = [(GEN1, '액션'), (GEN2, '애니메이션'), (GEN3, '코미디'), (GEN4, '범죄'), (GEN5, '공포'), (GEN6, '드라마'), (GEN7, '로맨스'), (GEN8, 'SF'), (GEN9, '가족'), (GEN10, '기타')]
    genre_like = forms.ChoiceField(choices=GENRE_LIKE, widget=forms.Select(attrs={'class': 'my-genrelike form-control'}))
    genre_dislike = forms.ChoiceField(choices=GENRE_DISLIKE, widget=forms.Select(attrs={'class': 'my-genredislike form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'my-username form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'my-email form-control'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'password1 form-control'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'password2 form-control'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'region', 'genre_like', 'genre_dislike')


class CustomUserChangeForm(UserChangeForm):
    REG_A, REG_B, REG_C, REG_D, REG_E = '서울', '대전', '대구', '부산', '구미'
    REGION_CHOICES = [(REG_A, '서울'), (REG_B, '대전'), (REG_C, '대구'), (REG_D, '부산'), (REG_E, '구미')]
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select(attrs={'class': 'my-region form-control'}))

    GEN1, GEN2, GEN3, GEN4, GEN5, GEN6, GEN7, GEN8, GEN9, GEN10 = '액션', '애니메이션', '코미디', '범죄', '공포', '드라마', '로맨스', 'SF', '가족', '기타'
    GENRE_LIKE = [(GEN1, '액션'), (GEN2, '애니메이션'), (GEN3, '코미디'), (GEN4, '범죄'), (GEN5, '공포'), (GEN6, '드라마'), (GEN7, '로맨스'), (GEN8, 'SF'), (GEN9, '가족'), (GEN10, '기타')]
    GENRE_DISLIKE = [(GEN1, '액션'), (GEN2, '애니메이션'), (GEN3, '코미디'), (GEN4, '범죄'), (GEN5, '공포'), (GEN6, '드라마'), (GEN7, '로맨스'), (GEN8, 'SF'), (GEN9, '가족'), (GEN10, '기타')]
    genre_like = forms.ChoiceField(choices=GENRE_LIKE, widget=forms.Select(attrs={'class': 'my-genrelike form-control'}))
    genre_dislike = forms.ChoiceField(choices=GENRE_DISLIKE, widget=forms.Select(attrs={'class': 'my-genredislike form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'my-username form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'my-email form-control'}))


    class Meta:
        model = get_user_model() # User
        fields = ('username', 'email', 'region', 'genre_like', 'genre_dislike')


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'my-old_password form-control'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'my-new_password1 form-control'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'my-new_password2 form-control'}))

    class Meta:
        model = get_user_model() # User
        fields = '__all__'