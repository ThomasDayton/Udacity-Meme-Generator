import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static/meme.jpg')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = [os.path.join(root, name) for root, _, files in os.walk(images_path) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    if not os.path.isdir(meme.out_path.split('/')[1]):
        os.makedirs(meme.out_path.split('/')[1])
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    
    try:
        image_url = request.form.get('image_url')
        r = requests.get(image_url, allow_redirects=True)

        tmp = f'./temp_{random.randint(0, 1000000)}.jpg'

        with open(tmp, 'wb') as img_f:
            img_f.write(r.content)
    
        quote = request.form.get('body')
        author = request.form.get('author')
        print(f'{quote}, {author}')


        path = meme.make_meme(tmp, quote, author)

        return render_template('meme.html', path=path)
    except requests.exceptions.MissingSchema:
        print('No Image URL was supplied')
        return render_template('meme_error.html')
    except requests.exceptions.ConnectionError:
        print('There was a connection error')
        return render_template('meme_error.html')
    except OSError:
        print('A valid Image URL was not supplied- try supplying a JPG')
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run()
