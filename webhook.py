import requests
def send_webhook_message(webhook_url, message, embed_title, embed_description, embed_color):
    if not message.strip() and not embed_title.strip() and not embed_description.strip():
        print("Hata: Mesaj veya embed boş olamaz.")
        return
    payload = {
        "content": message,
        "embeds": [
            {
                "title": embed_title,
                "description": embed_description,
                "color": int(embed_color, 16) if embed_color else 16711680
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("Mesaj ve embed başarıyla gönderildi.")
        else:
            print("Mesaj ve embed gönderme hatası. Yanıt Kodu:", response.status_code)
            print("Hata Detayları:", response.text)

    except Exception as e:
        print("Bir hata oluştu:", str(e))

if __name__ == "__main__":
    webhook_url = input("Discord Webhook URL'sini girin: ")
    message = input("Mesajı girin: ")
    embed_title = input("Embed başlığını girin: ")
    embed_description = input("Embed açıklamasını girin: ")
    embed_color = input("Embed rengini altı hane hexadecimal olarak girin (örnek: FF0000): ")

    send_webhook_message(webhook_url, message, embed_title, embed_description, embed_color)