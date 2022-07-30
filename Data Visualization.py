import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Read in dataset
sentiment_results = pd.read_csv("D:/tweets_visual.csv")

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

fig1.show()

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
        line=dict(color='black', width=2)
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
        line=dict(color='black', width=2)
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
        line=dict(color='black', width=2)
    )
))

fig2.update_layout(barmode='stack')
fig2.show()

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
    arr[arr == -np.inf] = 0
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
fig3.show()

# 4: Histogram of Likes by Sentiment (log scale)
hist_data = [neg_likes, neu_likes, pos_likes]
group_labels = ['Negative', 'Neutral', 'Positive']
colors = ['#EF553B', '#636EFA', '#00CC96']

fig4 = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

fig4.update_layout(title_text='Curve/Rug Plot of Likes by Sentiment (log scale)')
fig4.show()

# 5: Distribution of Retweets by Sentiment (log scale)
neg_retweets_init = sentiment_results[sentiment_results["sentiment"] == 0]["retweets"]
neu_retweets_init = sentiment_results[sentiment_results["sentiment"] == 1]["retweets"]
pos_retweets_init = sentiment_results[sentiment_results["sentiment"] == 2]["retweets"]

neg_retweets = np.log10(neg_retweets_init)
neu_retweets = np.log10(neu_retweets_init)
pos_retweets = np.log10(pos_retweets_init)

for arr in [neg_retweets, neu_retweets, pos_retweets]:
    arr[arr == -np.inf] = 0
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
fig5.show()

# 6: Histogram of Retweets by Sentiment (log scale)
hist_data = [neg_retweets, neu_retweets, pos_retweets]
group_labels = ['Negative', 'Neutral', 'Positive']
colors = ['#EF553B', '#636EFA', '#00CC96']

fig6 = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

fig6.update_layout(title_text='Curve/Rug Plot of Retweets by Sentiment (log scale)')
fig6.show()
