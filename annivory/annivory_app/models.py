from django.db import models
from django.contrib.auth.models import AbstractUser

"""
postgresql 
server_name: mylee_env / password: admin1234
"""

"""
사용자 정보 User 테이블
"""
class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
메인페이지 토픽 정보 Category 테이블
"""
class Category(models.Model):
    name = models.CharField(max_length=100)
    # blank가 True라는건 무슨 의미인지 서술하시오.
    # 폼 유효성 검사 : 빈 문자열('')이 있어도 유효하다고 간주됨
    # 선택적 입력 : UI에서 이 필드는 선택적 입력이 가능한 필드가 됨
    # 데이터베이스와의 차이 : blank=True는 데이터베이스 수준에서의 NULL허용과는 다름.
    #                     데이터베이스에서 NULL값을 허용하려면 null=True 옵션을 별도로 지정해야함.
    # 문자열 필드의 특수성 : CharField나 TextField 와 같은 문자열 기반 필드의 경우, blank=True 만으로도 빈 문자열을 저장할 수 있음
    # 관리자 인터페이스 : Django 관리자 페이지에서도 이 필드는 선택적 입력 필드로 표시됨
    # === 이 의미는 모든 카테고리가 반드시 설명을 가질 필요는 없다는 비즈니스 로직을 반영함.
    description = models.TextField(blank=True)

"""
글
"""
class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

"""
Media 
"""
# class Media(models.Model):
#     MEDIA_TYPES = (
#         ('image', 'Image'),
#         ('video', 'Video'),
#     )
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
#     # FileField는 뭐하는 필드인지 설명하시오.
#     # 파일업로드, 파일 저장, 파일 경로 관리, upload_to 매개 변수 (파일이 저장될 디렉토리 지정)
#     # 파일 접근, 다양한 파일 타입(이미지/문서/압축 파일 등 모든 종류의 파일을 저장할 수 있음)
#     # 파일 검증(파일 크기, 확장자 등 검증할 수 있는 기능)
#     # 스토리지 백엔드(로컬파일 시스템 뿐만 아니라 클라우드 스토리지 등 다양한 스토리지 백엔드 지원)
#     file_path = models.FileField(upload_to='media/')
#     created_at = models.DateTimeField(auto_now_add=True)

"""
댓글 정보 Comment 테이블
"""
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # 왜 created_at은 auto_now_add 가 True 이고, updated_at은 auto_now가 True인지 설명하시오.
    # auto_now_add=True 는 객체 생성 시 자동으로 현재 시간을 저장하고,
    # auto_now=True 는 객체가 저장될 때마다 시간을 업데이트 함
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
좋아요 정보 Like 테이블
"""
# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

"""
Event 테이블
"""
# class Event(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     start_date = models.DateField()
#     # end_date는 비어도 됨. 그럼 blank를 True로 하는가, Null을 True로 하는가?
#     # blank=True는 폼 유효성 검사 수준에서 작동함. Django 관리자 인터페이스나 사용자 정의 폼에서 이 필드를 비워둘 수 있게 함
#     # null=True는 데이터베이스 수준에서 작동함. 데이터베이스에 NULL값을 저장할 수 있게 함
#     # DateField는 빈 값과 NULL이 구분됨. 빈 문자열('')은 유효한 날짜가 아니므로,
#     # 날짜가 제공되지 않았을 때 NULL로 저장하는 것이 적절함
#     end_date = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

"""
개인 프로필 정보 Profile 테이블
"""
class Profile(models.Model):
    # 왜 user테이블을 one to one필드로 가져왔는지 서술하시오.
    # 일대일 관계 보장 : 각 User 인스턴스는 정확히 하나의 Profile 인스턴스와 연결됨.
    #                 이는 사용자당 하나의 프로필만 존재해야한다는 비즈니스 로직을 반영함.
    # 데이터 분리와 성능 최적화 : 자주 사용되는 User 모델의 기본 정보와 덜 자주 사용되는 Profile 정보를 분리함으로써, 데이터베이스 쿼리 성능을 최적화할 수 있음
    # 유연성, 관리의 용이성...
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
팔로워 정보 Follower 테이블
"""
class Follower(models.Model):
    # related_name으로 역방향 관계 명확히 작성하기
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)