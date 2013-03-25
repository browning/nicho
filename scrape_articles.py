# downloads and stores articles from RSS feeds

import feedparser
import pickle

posts = []

# Go through each post in our list of RSS feeds and parse the feed
f = open('beer_rss_feeds')
for feed_url in f:
	print("Scraping: %r..." % feed_url)
	feed_data = feedparser.parse(feed_url)
	for post in feed_data.entries:
		posts.append({"url": post.link,
			"title": post.title,
			"description": post.description,
			"date_posted": post.date_parsed if hasattr(post, 'date_parsed') else None})
f.close()

# store all of the data in a file
outfile = open('article_data.dat', 'w+')
pickle.dump(posts, outfile)
outfile.close()


