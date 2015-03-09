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
	"markers": [dict(name="Players", filterFunction=playerIcons, checked=True)]
}

renders["normalrendernight"] = {
	"world": "aoeminecraft",
	"title": "Night",
	"rendermode": smooth_night,
	"markers": [dict(name="Players", filterFunction=playerIcons, checked=True)]
}

renders['spawnover'] = {
	'world': 'aoeminecraft',
	'rendermode': [ClearBase(), SpawnOverlay()],
	'title': "Spawn Overlay",
	'overlay': ['normalrenderday']
}

renders['biomeover'] = {
	'world': 'aoeminecraft',
	'rendermode': [ClearBase(), BiomeOverlay()],
	'title': "Biome Overlay",
	'overlay': ['normalrenderday']
}
