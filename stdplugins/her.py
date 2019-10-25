"""
A Torrent Client Plugin Based On Aria2 for Userbot

cmds: Magnet link : .magnet magnetLink
	  Torrent file from local: .tor file_path
	  Show Downloads: .show
	  Remove All Downloads: .ariaRM
	  Resume All Downloads: .ariaResume
	  Pause All Downloads:  .ariaP
	  
By:- @Zero_cool7870	   

"""
import aria2p
from telethon import events
import asyncio
import os

cmd = "aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800  --max-connection-per-server=10 --rpc-max-request-size=1024M --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=10 --daemon=true"

aria2_is_running = os.system(cmd)

aria2 = aria2p.API(
		aria2p.Client(
			host="http://localhost",
			port=6800,
			secret=""
		)
	)


@borg.on(events.NewMessage(pattern=r"\.her", outgoing=True))
async def magnet_download(event):
	if event.fwd_from:
		return
	var = event.text[5:]
	print(var)	
	uris = [var]

	#Add URL Into Queue 
	try:	
		download = aria2.add_uris(uris, options=None, position=None)
	except Exception as e:
		await event.edit("`Error:\n`"+str(e))
		return

	gid = download.gid
	complete = None
	while complete != True:
		file = aria2.get_download(gid)
		complete = file.is_complete
		try:
			msg = "Downloading File: "+str(file.name) +"\nSpeed: "+ str(file.download_speed_string())+"\n"+"Progress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nETA:  "+str(file.eta_string())+"\n\n"  	
			await event.edit(msg)
			await asyncio.sleep(10)
		except Exception as e:
			print(str(e))
			pass	
			
	await event.edit("File Downloaded Successfully...")