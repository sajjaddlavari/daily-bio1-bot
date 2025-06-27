
import logging
import random
import asyncio
from datetime import time, datetime
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.executor import start_polling
from aiocron import crontab

API_TOKEN = '7925800400:AAFcqr57dgPA3XnMwhunWGbsjlzv1sMB2dA'
CHANNEL_ID = '@music_jjavan'

# لیست پست‌ها (بیو/کپشن‌های سبک @BioTels)
POSTS = [
    "ساکت بودن من نشونه‌ی آروم بودنم نیست؛\nدارم با خودم می‌جنگم.\n@BioTels",
    "بزرگ‌ترین اشتباهم؟\nاینه که فکر کردم همه مثل منن.\n@BioTels",
    "هیچکس نفهمید پشت لبخندم چی گذشت...\n@BioTels",
    "خستگیِ روح، با خواب خوب نمیشه...\n@BioTels",
    "بی‌احساس نیستم، فقط دیگه حوصله ندارم.\n@BioTels",
    "یه روزی می‌فهمی کی بودم، ولی اون روز دیگه من نیستم.\n@BioTels",
    "𝑺𝒐𝒎𝒆 𝒑𝒂𝒊𝒏𝒔 𝒅𝒐𝒏’𝒕 𝒉𝒆𝒂𝒍, 𝒕𝒉𝒆𝒚 𝒋𝒖𝒔𝒕 𝒈𝒆𝒕 𝒉𝒊𝒅𝒅𝒆𝒏.\n@BioTels",
    "حرف نزدن، دلیل بر خوب بودن نیست.\n@BioTels",
    "اونی که ساکته، بیشتر فکر می‌کنه…\n@BioTels",
    "𝑰 𝒎𝒐𝒗𝒆𝒅 𝒐𝒏, 𝒃𝒖𝒕 𝒏𝒐𝒕 𝒐𝒗𝒆𝒓.\n@BioTels",
    "بعضیا فقط میان که یادت بندازن تنها شدی.\n@BioTels",
    "آروم بودنم از خستگیه، نه رضایت.\n@BioTels",
    "دلم یه بی‌خیالیِ واقعی می‌خواد...\n@BioTels",
    "𝑴𝒊𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖, 𝒃𝒖𝒕 𝒑𝒓𝒆𝒕𝒆𝒏𝒅𝒊𝒏𝒈 𝒊'𝒎 𝒇𝒊𝒏𝒆.\n@BioTels",
    "من اونیم که حتی \"خوبی؟\" هم برام مهمه.\n@BioTels"
]

# راه‌اندازی لاگ‌گیری
logging.basicConfig(level=logging.INFO)

# تعریف ربات و دیسپچر
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# زمان‌بندی ارسال پست‌ها: هر روز ساعت 8 صبح به‌وقت ایران (۵:۳۰ UTC)
@crontab('30 5 * * *')
async def scheduled_post():
    logging.info("Sending daily posts...")
    selected_posts = random.sample(POSTS, k=15)
    for post in selected_posts:
        await bot.send_message(chat_id=CHANNEL_ID, text=post)
        await asyncio.sleep(2)  # برای جلوگیری از اسپم‌شدن توسط تلگرام

async def main():
    logging.info("Bot is running...")
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
