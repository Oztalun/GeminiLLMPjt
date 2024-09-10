from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["author", "like_users", "created_at", "updated_at"]

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ('created_at', 'updated_at', "author",
                   "like_users", "like", "search")
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '상품명을 적어주세요. (50자 이내)',
                'style': 'width: 100%;'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '상품에 대한 설명을 적어주세요.',
                'style': 'width: 100%; height: 200px;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'
            }),
            # 'tags': forms.CharField(attrs={
            #     'placeholder': '상품에 대한 설명을 적어주세요.',
            # })
        }
        labels = {
            'title': "상품명",
            'content': "설명",
            'image': "상품 사진"
        }