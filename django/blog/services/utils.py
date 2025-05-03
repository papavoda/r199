# utils.py
import os
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from PIL import Image as PILImage

def validate_file_extension(value):
    """
    Validator to check if the uploaded file has a valid extension.
    """
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    # Get the file name and extension
    file_name = value.name
    extension = file_name.split('.')[-1].lower()

    # Check if the extension is valid
    if not any(extension in ext for ext in valid_extensions):
        raise ValidationError(
            _('Unsupported file extension. Please upload a valid file.'),
            code='invalid_file_extension'
        )

def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'articles/{instance.author}/{instance.slug}/{filename}'


def image_upload_directory(instance, filename):
    # Сохраняем с расширением .webp
    filename = os.path.splitext(filename)[0]
    return f'articles/{instance.post.author}/{instance.post.slug}/{filename}.webp'

def convert_to_rgb(img):
    """Конвертирует изображение в RGB режим"""
    if img.mode in ('RGBA', 'P'):
        return img.convert('RGB')
    return img

def resize_image(img, max_size=1280):
    """Изменяет размер изображения с сохранением пропорций"""
    width, height = img.size
    if width <= max_size and height <= max_size:
        return img

    if width > height:
        new_width = max_size
        new_height = int(height * (max_size / width))
    else:
        new_height = max_size
        new_width = int(width * (max_size / height))

    return img.resize((new_width, new_height), PILImage.LANCZOS)


def convert_image_to_webp(image_field, quality=85, max_size=1280):
    """Конвертирует изображение в WebP формат"""
    img = PILImage.open(image_field)
    img = convert_to_rgb(img)
    img = resize_image(img, max_size=max_size)

    output = BytesIO()
    img.save(output, format='WEBP', quality=quality)

    original_name = os.path.splitext(image_field.name)[0]
    new_name = f"{original_name}.webp"

    return InMemoryUploadedFile(
        output,
        'ImageField',
        new_name,
        'image/webp',
        sys.getsizeof(output),
        None
    )
