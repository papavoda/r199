# utils.py
import os
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from PIL import Image as PILImage, ImageOps, ImageEnhance
from django.conf import settings

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


def apply_watermark(img):
    """Applies watermark from settings with opacity adjustment"""
    try:
        # Get settings with defaults
        watermark_path = settings.IMAGE_PROCESSING.get('WATERMARK_PATH')
        opacity = settings.IMAGE_PROCESSING.get('WATERMARK_OPACITY')
        position = settings.IMAGE_PROCESSING.get('WATERMARK_POSITION', 'SouthEast')
        offset = settings.IMAGE_PROCESSING.get('WATERMARK_OFFSET')

        if not watermark_path or not os.path.exists(watermark_path):
            raise FileNotFoundError("Watermark file not found")

        watermark = PILImage.open(watermark_path).convert('RGBA')

        # Adjust opacity
        if opacity < 1.0:
            alpha = watermark.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
            watermark.putalpha(alpha)

        # Calculate size (20% of image width)
        wm_size = int(img.width * 0.2)
        watermark.thumbnail((wm_size, wm_size), PILImage.LANCZOS)

        # Position calculation
        if position == 'SouthEast':
            x = img.width - watermark.width - offset[0]
            y = img.height - watermark.height - offset[1]
        elif position == 'Center':
            x = (img.width - watermark.width) // 2
            y = (img.height - watermark.height) // 2
        else:  # Default to SouthEast
            x = img.width - watermark.width - offset[0]
            y = img.height - watermark.height - offset[1]
        img.paste(watermark, (x, y), watermark)
        return img

    except Exception as e:
        print(f"Watermark application skipped: {str(e)}")
        return img  # Return original if watermark fails


def convert_to_rgb(img):
    """Конвертирует изображение в RGB режим"""
    if img.mode in ('RGBA', 'P'):
        return img.convert('RGB')
    return img

def resize_image(img, max_size=1280):

    # Сначала применяем EXIF-поворот (если есть)
    img = ImageOps.exif_transpose(img)
    #  Изменяет размер изображения с сохранением пропорций
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

    # Resize
    img = resize_image(img, max_size=max_size)

    # Add Watermark
    img = apply_watermark(img)

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
