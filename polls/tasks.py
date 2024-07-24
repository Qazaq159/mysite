import asyncio
from celery import shared_task


@shared_task
def task_one():
    async def func_one():
        print('func one done')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(func_one())
    print('task one done')


@shared_task
def task_two():
    print('task two done')