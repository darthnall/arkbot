import app
import os
import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()
    token = os.environ['DISCORD_ACCESS_TOKEN']
    app.start(token=token, dev=True)
