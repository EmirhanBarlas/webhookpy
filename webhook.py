import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1196524879739113512/pc9SjtfrXU0_82YfITqAXNEWuvEqokowgWueEqbRY_JsGJl2cuIwfstYJKltwnlHS7c8"

def send_webhook_message(message):
    if not message.strip():
        print("Hata: Mesaj boş olamaz.")
        return
    payload = {"content": message}

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Mesaj başarıyla gönderildi.")
        else:
            print("Mesaj gönderme hatası. Yanıt Kodu:", response.status_code)
            print("Hata Detayları:", response.text)

    except Exception as e:
        print("Bir hata oluştu:", str(e))

if __name__ == "__main__":
    message = input("Mesajı girin: ")
    send_webhook_message(message)
