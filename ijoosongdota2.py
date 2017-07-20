import dota2api
import time
import urllib
import smtplib

#ijoosong's Steam ID
steamID = 17854758
steamID3 = 35709316
steamID64 = 76561197995975044

#Valve API Key
api = dota2api.Initialise("Enter Valve API Key")

while True:
	#Current Time
	current_epoch_time = time.time()
	current_time = time.strftime('%m-%d %H:%M:%S', time.localtime(current_epoch_time))

	#ijoosong's Match History
	match_history = api.get_match_history(account_id=steamID64)

	#Recent Match ID
	match_id = match_history['matches'][0]['match_id']

	#Match Details
	match_details = api.get_match_details(match_id=match_id)

	#Game Start Time, Pre Game Duration, Game Duration, Total Time
	start_time = match_details['start_time']
	pre_game_duration = match_details['pre_game_duration']
	duration = match_details['duration']
	total_epoch_time = start_time + pre_game_duration + duration
	total_local_time = time.strftime('%m-%d %H:%M:%S', time.localtime(total_epoch_time))

	#ijoosong's Details
	for player in match_details['players']:
		if player['account_id'] == steamID3:
			if player['player_slot'] < 100:
				team = 'Radiant'
			else:
				team = 'Dire'
			hero_pick = player['hero_name']
			death_count = player['deaths']

	#Match Results		
	if match_details['radiant_win'] == 1:
		match_result = 'Radiant'
	else:
		match_result = 'Dire'
	
	print 'Current Time: ' + current_time
	print 'Game Finished: ' + total_local_time
	print 'Team: ' + team
	print 'Hero Pick: ' + hero_pick
	print 'Death Count: ' + str(death_count)
	print 'Winner: ' + match_result
	
	#login gmail
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login('Enter Email Address', 'Enter Email Password')

	#Notifications
	if (current_epoch_time - total_epoch_time)/3600 < 0.25:
		#send email to text
		server.sendmail('Enter Email Address', 'Enter Phone Number', '\n' + 'Game finished on: ' + total_local_time + '\n' + 'Joe\'s Team: ' + team + '\n' + 'Joe\'s Hero: ' + hero_pick + '\n' + 'Joe\'s Deathcount: ' + str(death_count) + '\n' + 'Winner: ' + match_result)
	time.sleep(900 - time.time() % 900)
