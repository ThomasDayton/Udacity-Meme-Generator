'''A simple class that turns images and quotes into memes.'''
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    '''A simple class that turns images and quotes into memes.'''
    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        '''
        Creates a simple meme from the given image and quote,
        then saves it to the predefined out_path.

        Attributes:
        img_path: The path to the original image to use.
        text: The body of the quote used.
        author: The author of the quote used.
        width: The width of the image. Defaults to 500px.
        '''
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        
        if text is not None and author is not None:
            message = f'"{text}" - {author}'
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')

        img.save(self.out_path)
        return self.out_path
