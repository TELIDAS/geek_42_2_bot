from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession

# pip install aiohttp-socks
PROXY_URL = 'http://proxy.server:3128'
session = AiohttpSession(proxy=PROXY_URL)
storage = MemoryStorage()
TOKEN = config("TOKEN_KEY")
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()
