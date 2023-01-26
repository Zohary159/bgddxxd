from pyrogram import Client, filters
from datetime import datetime

app = Client("@PKaaJ - Pyrogram",
api_id=15022546 ,
api_hash="e1b2ae2f067ffc53d5127882e76b5f60",
bot_token="5486499465:AAFMr6GuGu8T8uzC1zOaRM97z_luCPpsMe4")

now = datetime.now()
now = (now.strftime('%I:%M'))
@app.on_message(filters.new_chat_members)
async def welcome(chat,message,already=False):
      chat=message.chat.id
      if not already:
        chat = await app.get_chat(chat)
        members = chat.members_count
        await message.reply_text(f"""● نورت يقمر ♥♡ 
 {message.from_user.first_name}
{chat.title}
●  يجب احترام الادمنية
●  الالتزام بالقوانين في الوصف
●  الاعضاء  {members} 
●  وقت الانضمام  {now}""")



app.run()
print("fuck")
