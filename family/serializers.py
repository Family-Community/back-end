from rest_framework import serializers
from .models import Group, Member

# 개발자 확인용 시리얼라이저
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


# 그룹의 컬러값을 리턴하기 위한 시리얼라이저
class GroupColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['color']


# family_code -> group_pk를 위한 시리얼라이저
class GroupPkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'family_name', 'color']


# 개발자 확인용 시리얼라이저
class MemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_original = serializers.SerializerMethodField()
    class Meta:
        model = Member

        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def get_image_original(self, obj):
        if obj.image_original:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image_original.url)
        return None

    # def create(self, data):
    #     group = self.context.get('group')
    #     member_id = self.context.get('member_id')
    #     return Member.objects.create(group = group, member_id = member_id, **data)


# 멤버 생성 시리얼라이저
class MemberCreateSerializer(serializers.ModelSerializer):
    image_original = serializers.ImageField(required=False)
    class Meta:
        model = Member
        fields = ['id', 'name', 'image_original']

    # def validate_image(self, value):
    #     img = Image.open(value)
    #     width, height = img.size

    #     min_side = min(width, height)
    #     left = (width - min_side) // 2
    #     top = (height - min_side) // 2
    #     right = (width + min_side) // 2
    #     bottom = (height + min_side) // 2
    #     img = img.crop((left, top, right, bottom))

    #     target_size = (300, 300)  # 원하는 크기로 변경
    #     img.thumbnail(target_size, Image.LANCZOS)

    #     buffer = BytesIO()
    #     img.save(buffer, format='JPEG')
    #     value.file = buffer

    #     return value

class MemberWithoutIDSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields = ['name', 'image']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None

class MemberWithIDSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields = ['id', 'name', 'image']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None


# 멤버 프로필 이미지 원본 시리얼라이저
class MemberImageSerializer(serializers.ModelSerializer):
    image_original = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['image_original']

    def get_image_original(self, obj):
        if obj.image_original:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image_original.url)
        return None
