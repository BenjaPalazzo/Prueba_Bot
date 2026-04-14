import datetime
import json

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
load_dotenv()

application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

async def message(update, context):
    await update.message.reply_text("📡 Bot de análisis satelital \n Enviá tu ubicación para analizar deformación del terreno")
    return
def calcular_deformacion(lat, lon):
    return lat * 0.1 + lon * 0.05

async def ubication(update,context):
    delta = 0.01
    location = update.message.location
    lat = location.latitude
    lon = location.longitude
    if -90 <= lat <= 90 and -180 <= lon <= 180: 
        north = lat + delta
        south = lat - delta
        west = lon - delta
        east = lon + delta
        start = datetime.datetime.now().strftime("%Y-%m-%d")
        response = {
            "azimuth_looks": None,
            "connections": None,
            "path": None,
            "range_looks": None,
            "sensor": None,
            "workflow": None,
            "east": east,
            "north": north,
            "south": south,
            "west": west,
            "end": "",
            "start": start
            }
        await update.message.reply_text(f"{json.dumps(response)}")
    else:
        await update.message.reply_text("Datos invalidos!")
    return 

async def state(update, context):
    await update.message.reply_text("Procesando")
    return

ubicationHandler = MessageHandler(filters.LOCATION, ubication)
stateHandler = CommandHandler("state", state)
handler = MessageHandler(filters.TEXT, message)


application.add_handler(stateHandler)
application.add_handler(handler)
application.add_handler(ubicationHandler)

application.run_polling()


