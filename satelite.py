from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
load_dotenv()

application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

async def message(update, context):
    await update.message.reply_text("Como estas?")
    return
def calcular_deformacion(lat, lon):
    return lat * 0.1 + lon * 0.05

async def ubication(update,context):
    location = update.message.location
    lat = location.latitudes
    lon = location.longitude
    deformacion = calcular_deformacion(lat, lon) 
    await update.message.reply_text(f"Lat: {lat}, Lon: {lon}, Def: {deformacion}")
    return


ubicationHandle = MessageHandler(filters.LOCATION, ubication)
handler = MessageHandler(filters.TEXT, message)
application.add_handler(handler)
application.add_handler(ubicationHandle)
application.run_polling()

