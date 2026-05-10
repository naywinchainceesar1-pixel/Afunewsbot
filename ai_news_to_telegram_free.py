import os
import requests

def send_news():
    # GitHub Secrets ထဲက Token နဲ့ ID ကို လှမ်းယူခြင်း
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if not token or not chat_id:
        print("Error: Token သို့မဟုတ် Chat ID မရှိပါ။ Secrets ကို စစ်ဆေးပါ။")
        return

    message = "📢 မင်္ဂလာပါ! AFUbot မှ အောင်မြင်စွာ စာပို့လိုက်ပါပြီ။"
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    
    response = requests.post(url, data=payload)
    print(response.json())

if __name__ == "__main__":
    send_news()
