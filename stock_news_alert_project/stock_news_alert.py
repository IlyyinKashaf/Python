import requests 
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 'GGP7G54E2IL2G9RC'
NEWS_API_KEY = '49e9daeee4374272bbf531c577ac93fc'
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"
TWILIO_AUTH_TOKEN = ''
TWILIO_SID =''

stock_parameters = {'function':'TIME_SERIES_DAILY',
              'symbol':STOCK_NAME,
              'apikey':STOCK_API_KEY,
              }

response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data['4. close']
print(yesterday_closing)


before = data_list[1]
before_closing = before['4. close']
print(before_closing)

difference = abs(float(yesterday_closing) - float(before_closing))
print(difference)

percentage = (difference /float(yesterday_closing) * 100)
print(percentage)

if percentage > 5:
    news_parameters = {'qInTitle':COMPANY_NAME,
                   'apiKey': NEWS_API_KEY
                   }
        
    news_response =response.get(NEWS_ENDPOINT,params=news_parameters)
    articles = news_response.json()['articles']
    print(articles)
    three_articles = articles[:3]



formatted_articles = [f"{STOCK_NAME}: {percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)
    #Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
for article in formatted_articles:
    message = client.messages.create(
    body=article,
    from_=VIRTUAL_TWILIO_NUMBER,
    to=VERIFIED_NUMBER
        )