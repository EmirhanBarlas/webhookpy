import requests
import tkinter as tk

def send_webhook_message(webhook_url, message, embed_title, embed_url, embed_description, embed_color):
    if not message.strip() and not embed_title.strip() and not embed_description.strip():
        print("Hata: Mesaj veya embed boş olamaz.")
        return
    payload = {
        "content": message,
        "embeds": [
            {
                "title": embed_title,
                "url": embed_url,
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

def open_window():
    window = tk.Tk()
    window.title("Webhook Gönderme Uygulaması")

    webhook_url_label = tk.Label(window, text="Discord Webhook URL'sini girin:")
    webhook_url_label.pack()
    webhook_url_entry = tk.Entry(window)
    webhook_url_entry.pack()

    message_label = tk.Label(window, text="Mesajı girin (Boş bırakılabilir):")
    message_label.pack()
    message_entry = tk.Entry(window)
    message_entry.pack()

    embed_title_label = tk.Label(window, text="Embed başlığını girin (Boş bırakılabilir):")
    embed_title_label.pack()
    embed_title_entry = tk.Entry(window)
    embed_title_entry.pack()

    embed_url_label = tk.Label(window, text="Title Kısmında Url Bırakmak İçin (Boş Bırakılabilir):")
    embed_url_label.pack()
    embed_url_entry = tk.Entry(window)
    embed_url_entry.pack()

    embed_description_label = tk.Label(window, text="Embed açıklamasını girin (Boş bırakılabilir):")
    embed_description_label.pack()
    embed_description_entry = tk.Entry(window)
    embed_description_entry.pack()

    embed_color_label = tk.Label(window, text="Embed rengini altı hane hexadecimal olarak girin (örnek: FF0000) (Boş bırakılabilir):")
    embed_color_label.pack()
    embed_color_entry = tk.Entry(window)
    embed_color_entry.pack()

    send_button = tk.Button(window, text="Gönder", command=lambda: send_webhook_message(
        webhook_url_entry.get(),
        message_entry.get(),
        embed_title_entry.get(),
        embed_url_entry.get(),
        embed_description_entry.get(),
        embed_color_entry.get()
    ))
    send_button.pack()

    window.mainloop()

if __name__ == "__main__":
    open_window()
