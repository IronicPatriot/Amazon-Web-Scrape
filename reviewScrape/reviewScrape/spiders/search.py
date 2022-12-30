import webbrowser

userInput = input("Enter search data: ")
userInput.replace(" ", "+")
# replaces user's spaces with + for the url
webbrowser.open('https://www.amazon.co.uk/s?k=' + userInput)
# doesn't need to open link in final version, just for testing


# - https://youtu.be/mTOXVRao3eA?list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv splash

#fetch('http://localhost:8050/render.html?url=

# a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal

# remeber hrefs dont like ::text
