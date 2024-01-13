import tkinter as tk
import requests

def send_webhook():
    webhook_url = url_entry.get()
    message = message_entry.get()
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        status_label.config(text="Webhook gönderimi başarılı!", fg="green")
    else:
        status_label.config(text="Webhook gönderimi başarısız! Hata Kodu: " + str(response.status_code), fg="red")

root = tk.Tk()
root.title("Webhook Gönderme Aracı")

url_label = tk.Label(root, text="Webhook URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

message_label = tk.Label(root, text="Göndermek İstediğiniz Mesaj:")
message_label.pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

send_button = tk.Button(root, text="Webhook Gönder", command=send_webhook)
send_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
