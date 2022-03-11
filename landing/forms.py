from django import forms


class ContactForm(forms.Form):

    contact_email = forms.EmailField(
            widget=forms.TextInput(
                attrs={
                    "class": "w3-input w3-padding-16",
                    "type": "email",
                    "placeholder": "Email"
                    }),
            help_text="Nhập để gởi email của bạn tại đây",
            error_messages={
                'invalid': "Email không hợp lệ",
                'required': "Bạn chưa nhập email"
            }
            )

    contact_message = forms.CharField(
        widget=forms.Textarea(
                attrs={
                    'class': 'w3-input w3-padding-16',
                    'rows': '5',
                    "placeholder": "Lời nhắn"
                    }),
        help_text="Nhập lời nhắn của bạn tại đây",
        error_messages={
            'required': "Bạn chưa nhập Tin nhắn để gởi"
        }
            )
    contact_name = forms.CharField(
        widget=forms.TextInput(
                attrs={
                    'class': 'w3-input w3-padding-16',
                    'placeholder': 'Tên'
                    }),
        help_text="Nhập để gởi tên của bạn tại đây",
        error_messages={
            'required': "Bạn chưa nhập Tên"
        }
        )

    contact_phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'w3-input w3-padding-16',
                'placeholder': 'Số điện thoại ( Có thể để trống )'
            }),
        help_text="Nhập số điện thoại tại đây"
    )
