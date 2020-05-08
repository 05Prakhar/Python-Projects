import pyshorteners

url = input("Enter URL")
s = pyshorteners.Shortener()
print("Your shortened URL is : ", s.tinyurl.short(url))
