from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import httpx
from bs4 import BeautifulSoup


def com_start_btn():
    k1 = KeyboardButton(text='Filial 📍')
    k2 = KeyboardButton(text='Start ✅')
    k3 = KeyboardButton(text='Admin 👨🏻‍💻')
    k4 = KeyboardButton(text='news 🆕')
    design = [
        [k1, k2],
        [k3],
        [k4]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def gender_btn():
    k1 = KeyboardButton(text='Woman 🧍‍♀️')
    k2 = KeyboardButton(text='Men 🧍‍♂️')
    k3 = KeyboardButton(text='🔙 back')
    design = [
        [k1, k2],
        [k3],
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def training_month_btn():
    k1 = KeyboardButton(text='1 oy')
    k2 = KeyboardButton(text='2 oy')
    k3 = KeyboardButton(text='3 oy')
    k4 = KeyboardButton(text='4 oy')
    k5 = KeyboardButton(text='🔙 BACK')

    design = [
        [k1, k2],
        [k3, k4],
        [k5]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)



def training_day_btn():
    k1 = KeyboardButton(text='️Dushanba')
    k2 = KeyboardButton(text='Seshanba')
    k3 = KeyboardButton(text='Chorshanba')
    k4 = KeyboardButton(text='Payshanba')
    k5 = KeyboardButton(text='Juma')
    k6 = KeyboardButton(text='Shanba')
    k7 = KeyboardButton(text='🔙 BACK')
    design = [
        [k1, k2, k3],
        [k4, k5, k6],
        [k7]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def news():
    response = httpx.get('https://www.fitnessblender.com/')
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    new = []
    for i in soup.find_all('div', {"class": "title-card-group"}):
        if i == i.find('h2', {"class": "category"}):
            new.append(i.text)
    return new


