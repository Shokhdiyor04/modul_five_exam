
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from dispatcher import dp
from bot.buttons.reply import *


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    matn = f'''
    Salom {message.from_user.full_name} Quyidagilardan tanlang
    '''
    await message.answer(matn, reply_markup=com_start_btn())

    try:
        query1 = select(User).where(User.chat_id == message.from_user.id)
        if session.execute(query1).fetchone()[0]:
            print("bot")
            await message.answer(matn, reply_markup=com_start_btn())
    except:
        query2 = insert(User).values(chat_id=message.from_user.id, fullname=message.from_user.full_name)
        session.execute(query2)
        session.commit()
        print("yo'q")
        await message.answer(matn, reply_markup=com_start_btn())




@dp.message(lambda msg: msg.text == 'Filial 📍')
async def filial_handler(msg: Message) -> None:
    await msg.answer("Filial lokatsiyasi yuborildi !!!")

@dp.message(lambda msg: msg.text == 'Admin 👨🏻‍💻')
async def admin_handler(msg: Message) -> None:
    await msg.answer("https://t.me/shokhdiyor_f")

@dp.message(lambda msg:msg.text == 'news 🆕')
async def news_handler(msg: Message) -> None:
    await msg.answer("Yangiliklar" , reply_markup = news())

@dp.message(lambda msg: msg.text =='Start ✅')
async def start_handler(msg: Message) -> None:
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=gender_btn())

@dp.message(lambda msg: msg.text=='Woman 🧍‍♀️')
async def woman_handler(msg: Message) -> None:
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=training_month_btn())

@dp.message(lambda msg: msg.text=='Men 🧍‍♂️')
async def men_handler(msg: Message) -> None:
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=training_month_btn())

@dp.message(lambda msg: msg.text in ['1 oy', '2 oy', '3 oy', '4 oy'])
async def message_handler(msg: Message) -> None:
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=training_day_btn())

@dp.message(lambda msg: msg.text in ['️Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba'])
async def days_handler(msg: Message) -> None:
    training_day_btn()
    await msg.answer("Mashqlarni bajaring")


@dp.message(lambda msg: msg.text=="🔙 BACK")
async def back_gender_handler(msg: Message) -> None:
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=com_start_btn())











