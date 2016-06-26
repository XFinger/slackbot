from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


#add help responses here
@respond_to('help', re.IGNORECASE)
def help(message):
	message.reply("""
	Here are all of the things that I can help you with: \n
	help - this command \n
	count_rows - counts the number of rows in a dataset \n
	hi - greatings \n
	hello - greetings\n
	hello_formatting - greeting in italic style \n
	reply_webapi - returns an attachment or a table or somthing - it's an example at this point \n
	weather {city} {state} - returns weather information for given city and state. Seperate two word city names with an underscore.\n
	
	""")


@listen_to('I need help')
def help(message):
	# Message is replied to the sender (prefixed with @user)
	message.reply('Yes, I can!')

	# Message is sent on the channel
	message.send('I can help everybody!')