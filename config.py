from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN_KEY")
bot = Bot(token=TOKEN)
dp = Dispatcher()
