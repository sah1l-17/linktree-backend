from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .models import CustomUser, Referral
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):  
    permission_classes = [AllowAny]

def home(request):
    return HttpResponse("<h1>Welcome to Linktree Backend</h1>")

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        referral_count = Referral.objects.filter(referrer=request.user).count()
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "referral_code": request.user.referral_code,
            "referral_count": referral_count
        })

class ReferralListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        referrals = Referral.objects.filter(referrer=request.user).select_related("referred_user")
        data = [{"username": r.referred_user.username, "email": r.referred_user.email, "status": r.status} for r in referrals]
        return Response(data)
