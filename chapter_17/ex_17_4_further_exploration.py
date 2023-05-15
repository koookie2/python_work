from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
articles = []
for submission_id in submission_ids[:15]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        article = {
            'name': response_dict['title'],
            'score': response_dict['score']
        }
    except KeyError:
        print(f"Article {submission_id} is a Promotional Post.")
    else:
        # Append that dictionary to the list.
        articles.append(article)

# Sort the articles from most comments to least comments.
articles = sorted(articles, key=itemgetter('score'), reverse=True)

# Store the names and comments of each article (still in order).
names, scores = [], []
for article in articles:
    names.append(article['name'])
    scores.append(article['score'])

# Make visualization.
title = f"Most Highly Scored Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Comments'}
fig = px.bar(x=names, y=scores, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()