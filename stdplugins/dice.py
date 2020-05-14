#bug fixed by @d3athwarrior

"""@RollADie with dash
Syntax: .dice or .dice 1 to 6 any value 
        .dart or .dart 1 to 6 any value
        .basketball or .basketball 1 to 5 any value
        `you would be in trouble if you input any other value than mentioned.`"""
from telethon.tl.types import InputMediaDice
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="dice ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(''))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(''))
        except:
            pass

@borg.on(admin_cmd(pattern="basketball ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🏀'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🏀'))
        except:
            pass

@borg.on(admin_cmd(pattern="dart ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎯'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎯'))
        except:
            pass
        
