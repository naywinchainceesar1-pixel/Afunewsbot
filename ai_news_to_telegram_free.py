import requests

def send_news():
    token = "7756127608:AAHny6M_N-H6f_q77-H0pX0U82_N7Uv1fU8"
    chat_id = "-1003935881335"
    message = "📢 ဒီနေ့အတွက် AI နည်းပညာသတင်းများ စတင်ပို့ဆောင်ပေးနေပါပြီ။"
    
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

if __name__ == "__main__":
    send_news()
