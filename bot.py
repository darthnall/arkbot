import os
import re
import discord

def get_urls(text: str) -> list[str]:
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, text)
    return [_[0] for _ in url]

class ArkClient(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}.")
    
    async def on_message(self, message) -> None:
        print(f"Message from {message.author}: {message.content}")
        if message.author != self.user:
            urls = get_urls(message.content)
            if urls:
                await message.delete()

if __name__ == "__main__":
    client = ArkClient()
    client.run(os.environ.get("DISCORD_TOKEN", None))