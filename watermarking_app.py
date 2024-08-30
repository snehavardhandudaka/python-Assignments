from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(watermark_text, font)
    position = (image.width - text_width - 10, image.height - text_height - 10)
    draw.text(position, watermark_text, font=font)
    image.save(output_path)

add_watermark('example.jpg', '© YourName', 'watermarked_example.jpg')
