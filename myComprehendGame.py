import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    data_input = event['inputTranscript']
    print(event)
    print(context)
    comprehend = boto3.client("comprehend")
    sentiment = comprehend.detect_sentiment(Text = data_input , LanguageCode = "en")
    #sentiment = comprehend.detect_sentiment(Text = "Won lottery but had a bad day" , LanguageCode = "en")
   
    print(sentiment)
    
    if sentiment['Sentiment'] == 'MIXED':
        msg = "Oh so your text shows a diverse set of feelings consisting of an assorted set of emotions."
        
       
    if sentiment['Sentiment'] == 'POSITIVE':
        msg = "Oh I can sense positive vibes from your text."
        
         
    if sentiment['Sentiment'] == 'NEGATIVE':
        msg = "Sentence look negative"
         
    if sentiment['Sentiment'] == 'NEUTRAL':
        msg = "I sense neutral or indifferent feelings from your text"
         

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": msg
            }
        }
    }
       
       
       
    return response