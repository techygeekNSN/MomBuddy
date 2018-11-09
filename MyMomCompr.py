import json
import os,boto3
def lambda_handler(event, context):
    # TODO implement
    data_input = event['inputTranscript']
    print(event)
    print(context)
    comprehend = boto3.client('comprehend')
    sentiment = comprehend.detect_sentiment(Text = data_input,LanguageCode='en')
    #sentiment = comprehend.detect_sentiment(Text = "Won lottery but had a bad day" , LanguageCode = "en")
   
    print(sentiment)
    
    if sentiment['Sentiment'] == 'MIXED':
        msg = "I think u had okayish day with some happy and unhappy moments "
        
       
    if sentiment['Sentiment'] == 'POSITIVE':
        msg = "Oh I see you are having wonderful day"
        
         
    if sentiment['Sentiment'] == 'NEGATIVE':
        msg = "Oh u had negative moments"
         
    if sentiment['Sentiment'] == 'NEUTRAL':
        msg = "Oh you had okayish day"
         

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
