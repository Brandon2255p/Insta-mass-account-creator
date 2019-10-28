from modules.account import new_account
from modules.account_persister import store_all
import concurrent.futures
import asyncio

all_accounts = asyncio.Queue()
num_accounts = 20
async def new_account_async():
    acc = new_account()
    await all_accounts.put(acc)

async def make_accounts():
    coros = [new_account_async() for _ in range(num_accounts)]
    await asyncio.gather(*coros)
    acc = []
    while not all_accounts.empty():
        acc.append(await all_accounts.get())
    store_all(acc)
if __name__ == '__main__':
    asyncio.run(make_accounts())