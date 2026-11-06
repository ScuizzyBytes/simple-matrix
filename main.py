import asyncio
import random

import customtkinter as ctk
from rich import print

root = ctk.CTk()

W, H = 600, 600
letters = list("qwertyuiop[asdfghjkl;'zxcvbnm,./1234567890-=]" * 5)


async def shuffle_new_list():
        while True:
            random.shuffle(letters)
            text = " ".join(letters)
            print(f"[green]{text}[/green]" * 5)
            await asyncio.sleep(0.1)

asyncio.run(shuffle_new_list())
