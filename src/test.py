import twitter
import datetime

api = twitter.Api(
        consumer_key        = 'As75jctNvNEcxkcLbCABr0r95',
        consumer_secret     = 'EnBJoahY5s2w7BIv7GGoH9e3Jxip5k20ynk4mPaI4tqXkfOuBi',
        access_token_key    = '900724863760871430-bu5X9SGhy2A3JggSVX5VNxPHtdqEzJK',
        access_token_secret = 'kHz3aJztyxI4yLxLVT6x06Yr8ebmHLSnhIYDFQdo07gH1',
        )

#print (datetime.datetime.today().year)

api.PostUpdate(str(datetime.datetime.today().year) + '/' + str(datetime.datetime.today().month) + '/' + str(datetime.datetime.today().day) )
