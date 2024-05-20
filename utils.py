from pokemon_fetcher import PokemonFetcher
import requests
import io

def create_and_post_tweet(client_v1, client_v2):
    pokemon_fetcher = PokemonFetcher()
    
    caption = pokemon_fetcher.generate_caption()

    image_url = pokemon_fetcher.set_img()
    image_response = requests.get(image_url)
    image_data = image_response.content               
    image_file = io.BytesIO(image_data)
    image_file.name = 'image.jpg' 
    
    # Upload the image file
    media_id = client_v1.media_upload(filename=image_file.name, file=image_file).media_id_string

    # Post the tweet with the image
    client_v2.create_tweet(text=caption, media_ids=[media_id])
    print("Tweeted")
