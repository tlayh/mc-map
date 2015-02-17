import os

# getting environments for stuff that can not be modified
worlds["aoeminecraft"] = os.environ["WORLDS"]
outputdir = os.environ["OUTPUTDIR"]
texturepath = os.environ["TEXTURE"]
# end of environments

def playerIcons(poi):
	if poi['id'] == 'Player':
		poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
		return "Last known location for %s" % poi['EntityId']


def townFilter(poi):
	if poi['id'] == 'Town':
		return poi['name']


renders["normalrenderday"] = {
	"world": "aoeminecraft",
	"title": "Day",
	"rendermode": smooth_lighting,
	"dimension": "overworld",
	"manualpois":[
		{
			'id': 'Town',
			'x': 397,
			'y': 64,
			'z': -478,
			'name': 'Ghost-Town',
		},
		{
			'id': 'Town',
			'x': -157,
			'y': 64,
			'z': 356,
			'name': 'XP-Farm',
		},
		{
			'id': 'Town',
			'x': 2183,
			'z': 64,
			'y': 407,
			'name': 'Yoshi',
		},
		{
			'id': 'Town',
			'x': 1866,
			'z': 64,
			'y': 277,
			'name': 'Squid',
		},
		{
			'id': 'Town',
			'x': 49,
			'z': 64,
			'y': 283,
			'name': 'Flipper',
		},
	],
	"markers": [dict(name="Players", filterFunction=playerIcons, checked=True),
				dict(name="Places", filterFunction=townFilter, checked=True)],
}

renders["normalrendernight"] = {
	"world": "aoeminecraft",
	"title": "Night",
	"rendermode": smooth_night,
	"dimension": "overworld",
	'manualpois':[
		{
			'id': 'Town',
			'x': 397,
			'y': 64,
			'z': -478,
			'name': 'Ghost-Town',
		},
		{
			'id': 'Town',
			'x': -157,
			'y': 64,
			'z': 356,
			'name': 'XP-Farm',
		},
		{
			'id': 'Town',
			'x': 2183,
			'z': 64,
			'y': 407,
			'name': 'Yoshi',
		},
		{
			'id': 'Town',
			'x': 1850,
			'z': 60,
			'y': 230,
			'name': 'Squid',
		},
		{
			'id': 'Town',
			'x': 49,
			'z': 64,
			'y': 283,
			'name': 'Flipper',
		},
	],
	"markers": [dict(name="Players", filterFunction=playerIcons, checked=True),
				dict(name="Places", filterFunction=townFilter, checked=True)],
}

renders['spawnover'] = {
    'world': 'exmaple',
    'rendermode': [ClearBase(), SpawnOverlay()],
    'title': "Spawn Overlay",
    'overlay': ['normalrenderday', 'normalrendernight']
}
