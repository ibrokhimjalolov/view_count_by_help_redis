from rest_framework.generics import RetrieveAPIView

from .models import Post
from .serializers import PostSerializer
from .view_mixins import ViewCountMixin


class PostDetailView(ViewCountMixin, RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
