from facepy import GraphAPI
from facepy.exceptions import OAuthError


def ite_groups(groups,message,usuarios):
	for group_id in groups:
		print("Posting to " + 'http://www.facebook.com/groups/' + str(group_id))
		postfb(message,usuarios)

def postfb(message,usuarios):
	for (usuario,valores) in usuarios.items():
		try:
			if valores['numeropost'] >=20:
				continue
			api = GraphAPI(valores['token'])
			#api.post(path =str((group_id)+'/photos') + '/feed', message=message)
			print('Done')
			valores['numeropost']=valores['numeropost']+1
			break
		except OAuthError:
			print('user wrong')