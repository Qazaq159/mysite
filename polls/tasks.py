import asyncio
from celery import shared_task
from mstools.helpers import time_it_and_log


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


@shared_task
def task_three():

    @time_it_and_log  # but idea, it can not evaluate duration of async func
    async def func_one():
        import time
        time.sleep(15)
        print('func one done')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(func_one())
