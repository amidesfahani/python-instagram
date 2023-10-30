import instaloader
from persiantools import jdatetime
from datetime import datetime, timedelta
from pathlib import Path
import pprint
import json
import auth

# Let's calculate who's likes and comments are more!
# after calculating the points use winner.py to pick the winner!

loader = instaloader.Instaloader()
auth.login(loader)

points = {}
followers = []

exclude_accounts = ['instagram', 'messi']

short_codes = []

while True:
	post_url = input("Enter Post Url: ").strip()
	if post_url.lower() == "q" or post_url == "":
		break

	short_codes.append(post_url.split("/")[-2])


print('Calculating Points')

for short_code in short_codes:
	post = instaloader.Post.from_shortcode(loader.context, short_code)

	for like in post.get_likes():
		if like.username in exclude_accounts:
			continue
		points[like.username] = points.get(like.username, 0) + 1

	users_ids = []
	for comment in post.get_comments():
		if comment.owner.username in exclude_accounts:
			continue
		if not comment.owner.userid in users_ids:
			points[comment.owner.username] = points.get(comment.owner.username, 0) + 1
		points[comment.owner.username] = points.get(comment.owner.username, 0) + comment.likes_count + sum(1 for dummy in comment.answers)
		users_ids.append(comment.owner.userid)


Path('points.json').write_text(json.dumps(points, indent=4), encoding='utf-8')

# for like in post.get_likes():
	# followers.append({
	# 	'userid': like.userid,
	# 	'username': like.username,
	# })
# for comment in post.get_comments():
	# followers.append({
	# 	# 'id': comment.id,
	# 	'userid': comment.owner.userid,
	# 	'username': comment.owner.username,
	# 	# 'text': comment.text,
	# 	'likes_count': comment.likes_count,
	# 	'created_at_utc': f'{comment.created_at_utc:%Y-%m-%d %H:%M:%S%z}',
	# 	'answers': sum(1 for dummy in comment.answers)
	# })
# Path(short_code + '.json').write_text(json.dumps(followers, indent=4), encoding='utf-8')