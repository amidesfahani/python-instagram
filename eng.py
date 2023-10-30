from instaloader import Instaloader, Profile
from pprint import pp
from datetime import datetime, timedelta
import auth

# engagement rate calculator

loader = Instaloader()
auth.login(loader)

SINCE = False
# SINCE = datetime(2023, 1, 1)
# SINCE = datetime.now()
# SINCE = SINCE - timedelta(weeks=32)

MAX = 10

def engagement(username):
	# instaloader.exceptions.LoginRequiredException
	profile = Profile.from_username(loader.context, username)

	num_followers = profile.followers
	total_likes = 0
	total_comments = 0
	total_posts = 0

	for post in profile.get_posts():
		if MAX > 0 and total_posts == MAX:
			break

		if SINCE and post.date < SINCE:
			continue

		total_likes += post.likes
		total_comments += post.comments
		total_posts += 1

	result = {
		'followers': profile.followers,
		'likes': total_likes,
		'comments': total_comments,
		'posts': total_posts,
		'avg_likes': total_likes / total_posts,
		'avg_comments': total_comments / total_posts,
	}

	engagement = float(total_likes + total_comments) / (num_followers * total_posts)
	result['engagement'] = round(engagement * 100, 2)

	return result

# pp(engagement('amid.dev'))
# exit()

while True:
	target_profile = input("Enter Profile: ").strip()
	if target_profile.lower() == "q" or target_profile == "":
		break

	pp(engagement(target_profile))