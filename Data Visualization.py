import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Read in dataset
sentiment_results = pd.read_csv("D:/tweets_visual_larger.csv")

# 1: Data Breakdown by Verification Status
verification_status = sentiment_results["verified"].value_counts()

unverified_num = verification_status[0]
verified_num = verification_status[1]

data_ver = [go.Bar(
    x=verification_status.index,  # index = category name
    y=verification_status.values,  # value = count
)]

fig1 = go.Figure(
    data=data_ver,
    layout_title_text="Users by Verification Status"
)

# 2: Relative Percentage of Sentiment by Verification Status
fig2 = go.Figure(
    layout_title_text="Relative Percentage of Sentiment by Verification Status"
)

unverified_neg_num = len(
    sentiment_results[sentiment_results["verified"] == False][sentiment_results["sentiment"] == 0].index)
verified_neg_num = len(
    sentiment_results[sentiment_results["verified"] == True][sentiment_results["sentiment"] == 0].index)

fig2.add_trace(go.Bar(
    y=['Unverified', 'Verified'],
    x=[unverified_neg_num / unverified_num, verified_neg_num / verified_num],
    name='Negative',
    orientation='h',
    marker=dict(
        color='#EF553B',
        line=dict(color='black', width=1)
    )
))

unverified_neu_num = len(
    sentiment_results[sentiment_results["verified"] == False][sentiment_results["sentiment"] == 1].index)
verified_neu_num = len(
    sentiment_results[sentiment_results["verified"] == True][sentiment_results["sentiment"] == 1].index)

fig2.add_trace(go.Bar(
    y=['Unverified', 'Verified'],
    x=[unverified_neu_num / unverified_num, verified_neu_num / verified_num],
    name='Neutral',
    orientation='h',
    marker=dict(
        color='#636EFA',
        line=dict(color='black', width=1)
    )
))

unverified_pos_num = len(
    sentiment_results[sentiment_results["verified"] == False][sentiment_results["sentiment"] == 2].index)
verified_pos_num = len(
    sentiment_results[sentiment_results["verified"] == True][sentiment_results["sentiment"] == 2].index)

fig2.add_trace(go.Bar(
    y=['Unverified', 'Verified'],
    x=[unverified_pos_num / unverified_num, verified_pos_num / verified_num],
    name='Positive',
    orientation='h',
    marker=dict(
        color='#00CC96',
        line=dict(color='black', width=1)
    )
))

fig2.update_layout(barmode='stack')

# 3: Distribution of Likes by Sentiment (log scale)
# Get rid of "divide by zero encountered in log10" warning
np.seterr(divide='ignore')

neg_likes_init = sentiment_results[sentiment_results["sentiment"] == 0]["likes"]
neu_likes_init = sentiment_results[sentiment_results["sentiment"] == 1]["likes"]
pos_likes_init = sentiment_results[sentiment_results["sentiment"] == 2]["likes"]

neg_likes = np.log10(neg_likes_init)
neu_likes = np.log10(neu_likes_init)
pos_likes = np.log10(pos_likes_init)

for arr in [neg_likes, neu_likes, pos_likes]:
    arr[arr == float("-inf")] = 0

fig3 = go.Figure(
    layout_title_text="Distribution of Likes by Sentiment (log scale)"
)

fig3.add_trace(go.Box(x=neg_likes,
                      name='Negative',
                      marker_color='#EF553B'))
fig3.add_trace(go.Box(x=neu_likes,
                      name='Neutral',
                      marker_color='#636EFA'))
fig3.add_trace(go.Box(x=pos_likes,
                      name='Positive',
                      marker_color='#00CC96'))

fig3.update_layout()

# 4: Histogram of Likes by Sentiment (log scale)
hist_data = [neg_likes, neu_likes, pos_likes]
group_labels = ['Negative', 'Neutral', 'Positive']
colors = ['#EF553B', '#636EFA', '#00CC96']

fig4 = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

fig4.update_layout(title_text='Curve/Rug Plot of Likes by Sentiment (log scale)')

# 5: Distribution of Retweets by Sentiment (log scale)
neg_retweets_init = sentiment_results[sentiment_results["sentiment"] == 0]["retweets"]
neu_retweets_init = sentiment_results[sentiment_results["sentiment"] == 1]["retweets"]
pos_retweets_init = sentiment_results[sentiment_results["sentiment"] == 2]["retweets"]

neg_retweets = np.log10(neg_retweets_init)
neu_retweets = np.log10(neu_retweets_init)
pos_retweets = np.log10(pos_retweets_init)

for arr in [neg_retweets, neu_retweets, pos_retweets]:
    arr[arr == float("-inf")] = 0

fig5 = go.Figure(
    layout_title_text="Distribution of Retweets by Sentiment (log scale)"
)

fig5.add_trace(go.Box(x=neg_retweets,
                      name='Negative',
                      marker_color='#EF553B'))
fig5.add_trace(go.Box(x=neu_retweets,
                      name='Neutral',
                      marker_color='#636EFA'))
fig5.add_trace(go.Box(x=pos_retweets,
                      name='Positive',
                      marker_color='#00CC96'))

fig5.update_layout()

# 6: Histogram of Retweets by Sentiment (log scale)
hist_data = [neg_retweets, neu_retweets, pos_retweets]
group_labels = ['Negative', 'Neutral', 'Positive']
colors = ['#EF553B', '#636EFA', '#00CC96']

fig6 = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

fig6.update_layout(title_text='Curve/Rug Plot of Retweets by Sentiment (log scale)')

# 7: Distribution of Retweets by Sentiment (log scale) (zeroes removed)
neg_retweets_no_0 = neg_retweets[neg_retweets > 0]
neu_retweets_no_0 = neu_retweets[neu_retweets > 0]
pos_retweets_no_0 = pos_retweets[pos_retweets > 0]

fig7 = go.Figure(
    layout_title_text="Distribution of Retweets by Sentiment (log scale) (zeroes removed)"
)

fig7.add_trace(go.Box(x=neg_retweets_no_0,
                      name='Negative',
                      marker_color='#EF553B'))
fig7.add_trace(go.Box(x=neu_retweets_no_0,
                      name='Neutral',
                      marker_color='#636EFA'))
fig7.add_trace(go.Box(x=pos_retweets_no_0,
                      name='Positive',
                      marker_color='#00CC96'))

fig7.update_layout()

# 8: Histogram of Retweets by Sentiment (log scale) (zeroes removed)
hist_data = [neg_retweets_no_0, neu_retweets_no_0, pos_retweets_no_0]
group_labels = ['Negative', 'Neutral', 'Positive']
colors = ['#EF553B', '#636EFA', '#00CC96']

fig8 = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

fig8.update_layout(title_text='Curve/Rug Plot of Retweets by Sentiment (log scale) (zeroes removed)')

# 9: Histogram of Retweets by Sentiment (log scale) (zeroes removed)
fig9 = go.Figure(data=go.Scatter(
    x=sentiment_results["polarity"],
    y=sentiment_results["subjectivity"],
    mode='markers',
    marker=dict(
        size=5,
        color=sentiment_results["sentiment"],  # set color equal to a variable
        colorscale=['#EF553B', '#636EFA', '#00CC96'],  # one of plotly colorscales
        showscale=True
    )
))

# 10: Histogram of Retweets by Sentiment (log scale) (zeroes removed)
mask_web = (sentiment_results['source'] == "Twitter Web App")
mask_and = (sentiment_results['source'] == "Twitter for Android")
mask_ios = ((sentiment_results['source'] == "Twitter for iPhone") | (sentiment_results['source'] == "Twitter for iPad"))

sentiment_results.loc[mask_web, 'source category'] = "Web App"
sentiment_results.loc[mask_and, 'source category'] = "Android"
sentiment_results.loc[mask_ios, 'source category'] = "IOS"
sentiment_results.loc[sentiment_results['source category'].isnull(), 'source category'] = "Other"

fig10 = px.scatter(sentiment_results, x = "polarity", y = "subjectivity", color="source category",
                 title = "Scatterplot of polarity, subjectivity, and source category")

fig10.update_traces(marker=dict(size = 5))

fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()
fig7.show()
fig8.show()
fig9.show()
fig10.show()

