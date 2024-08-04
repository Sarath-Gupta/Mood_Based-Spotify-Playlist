from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
text = input()
sentiment = analyzer.polarity_scores(text)
def sentiment_to_mood(sentiment_score):
    if sentiment_score['compound'] > 0.3:
        return 'happy'
    elif sentiment_score['compound'] < -0.3:
        return 'sad'
    else:
        return 'neutral'
mood = sentiment_to_mood(sentiment)
print(mood)
