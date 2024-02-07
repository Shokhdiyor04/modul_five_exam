from aiogram import Dispatcher
from os import getenv
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher(storage=MemoryStorage())
