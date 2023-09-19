from bot import InternetSpeedTwitterBot


bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
tweet = bot.tweet_at_provider()