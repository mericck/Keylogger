# Keylogger

This code creates a keylogger that monitors keyboard activities and periodically sends the logs via email. I have provided explanations for the functions below:

on_press(key): This function is triggered when a key is pressed on the keyboard. It receives the information of the pressed key through the key parameter. If the key is a character, it adds the key.char value to the log. If the key is a special key, it adds the str(key) value to the log. The key is appended to the log variable.

on_release(key): This function is triggered when a key is released. It receives the information of the released key through the key parameter. If the released key is the ESC key, it calls the save_logs() function and resets the log variable.

save_logs(filename="keylogs.txt"): This function saves the accumulated keystrokes in the log variable to the specified file. By default, it saves the logs to a file named "keylogs.txt".

send_logs(sender_email, sender_password, receiver_email, smtp_server): This function sends the logs as an email. It uses the SMTP protocol for sending the email. The function takes the parameters of the sender email address (sender_email), sender email password (sender_password), receiver email address (receiver_email), and SMTP server (smtp_server). It reads the log file, creates the email content, and sends it.

run_keylogger(sender_email, sender_password, receiver_email, smtp_server, interval): This function starts the keylogger and periodically sends the logs. It takes parameters such as the sender email address, sender email password, receiver email address, SMTP server, and the interval for sending logs (in seconds). First, it starts the keyboard.Listener to listen for keyboard events. Then, it enters an infinite loop where it waits for a certain duration (interval), sends the logs, and saves them.

if __name__ == "__main__": section calls the run_keylogger() function and starts the keylogger when the program is run directly. In this section, you need to specify values such as the sender email address, sender email password, receiver email address, SMTP server, and the interval for sending logs.

These explanations provide a general understanding of the functions in your code. However, please remember that the use of keyloggers is subject to restrictions, and it is important to respect privacy rights. Using keyloggers without the consent of others or for illegal purposes is prohibited.
