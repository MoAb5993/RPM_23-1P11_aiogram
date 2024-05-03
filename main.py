''''Импорты'''
import asyncio
from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="6495085956:AAHNbitT6w1lRBmFhO0X9zpaUhk-aqKoupo")
dp = Dispatcher()


async def main():
    ''''Запуск телеграмм-бота'''
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
