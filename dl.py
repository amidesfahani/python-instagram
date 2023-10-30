from pathlib import Path
import instaloader
import auth

# Download any instagram post/reel

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()
auth.login(loader)

while True:
	post_url = input("Paste here: ")
	short_code = post_url.split("/")[-2]
	post = instaloader.Post.from_shortcode(loader.context, short_code)
	loader.download_post(post, Path('downloads') / Path(short_code))