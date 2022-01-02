from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('CircularStd-Book.ttf', 150)
# font = ImageFont.truetype('arial.ttf', 150)

# for letter in []:#list('ĘÓĄŚŁŻŹĆŃ'):
for i in range(65, 91):
    letter = chr(i)
    width = font.font.getsize(letter)[0][0]
    height = sum(font.getmetrics())
    centers = (128 - int(width / 2), 128 - int(height / 2))
    img = Image.new('RGB', (256, 256), color=(255, 87, 74))
    ImageDraw.Draw(img).text(centers, letter, fill=(255, 255, 255), font=font)
    img.save(f'letters/{letter}.png')
