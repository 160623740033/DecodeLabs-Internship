from textblob import TextBlob

print("🧠 AI Text Sentiment Recognition")

text = input("Enter a sentence: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

if polarity > 0.1:
    print("😊 Positive Sentiment Detected")

elif polarity < -0.1:
    print("😔 Negative Sentiment Detected")

else:
    print("😐 Neutral Sentiment Detected")

print("Polarity Score:", polarity)