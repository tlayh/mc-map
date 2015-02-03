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
	'manualpois':[
		{
			'id': 'Town',
			'x': 397,
			'y': 64,
			'z': -478,
			'name': 'Ghost-Town',
			'description': 'Sorry, no villagers left here....'
		}
	],
	"markers": [dict(name="Players", filterFunction=playerIcons, checked=True),
				dict(name="Towns", filterFunction=townFilter, checked=True)],
}

renders["normalrendernight"] = {
	"world": "aoeminecraft",
	"title": "Night",
	"rendermode": smooth_night,
	"dimension": "overworld",
}

renders['biomeover'] = {
    'world': 'aoeminecraft',
    'rendermode': [ClearBase(), BiomeOverlay()],
    'title': "Biomes",
    'overlay': ['normalrenderday'],
	"dimension": "overworld",
}
