import praw

import seaborn as sns
import matplotlib.pyplot as plt

from collections import defaultdict

#Providing secret values to establish connection with Reddit
reddit = praw.Reddit(client_id='Client_ID', client_secret='Client_Secret', user_agent='AppName')

#Initializing a list of redditors fow whom we are trying to find data.
redditors = [reddit.redditor('GallowBoob'),
            reddit.redditor('mvea'),
            reddit.redditor('TooShiftyForYou'),
            reddit.redditor('BunyipPouch'),
            reddit.redditor('KevlarYarmulke')]


#Start data extraction & graphical representation
fig, ax = plt.subplots(5, 2, figsize=(60, 60))

for i, redditor in enumerate(redditors):
    print("getting data for", redditor)
    subreddit_count = defaultdict(int)
    comment_count = defaultdict(int)
    for submission in redditor.submissions.new(limit=None):
        subreddit_count[submission.subreddit_name_prefixed] += 1

    for comment in redditor.comments.new(limit=None):
        comment_count[comment.subreddit_name_prefixed] += 1

    splot = sns.barplot(x=list(subreddit_count.keys()), y=list(subreddit_count.values()), ax=ax[i][0], palette='Blues')
    cplot = sns.barplot(x=list(comment_count.keys()), y=list(comment_count.values()), ax=ax[i][1], palette='Reds')
    ax[i, 0].set_title("u/" + str(redditor) + " Posts", fontsize=25)
    ax[i, 1].set_title("u/" + str(redditor) + " Comments", fontsize=25)
    splot.set_xticklabels(splot.get_xticklabels(), rotation=45, horizontalalignment='right')
    cplot.set_xticklabels(cplot.get_xticklabels(), rotation=45, horizontalalignment='right')
    for p in splot.patches:
        height = p.get_height()
        splot.text(p.get_x() + p.get_width() / 2, height, "{:1.0f}".format(height), ha="center")
    for p in cplot.patches:
        height = p.get_height()
        cplot.text(p.get_x() + p.get_width() / 2, height, "{:1.0f}".format(height), ha="center")

plt.savefig('redrep', dpi=200)




