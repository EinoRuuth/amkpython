import requests

paikkakunta = input("Anna paikkakunta: ")

apikey = "fa840d80f415d793c8613a5ce85633ed"

lokaatiokysely = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=1&appid={apikey}"
lokaatio = requests.get(lokaatiokysely).json()
koordinaatit = (lokaatio[0]["lon"], lokaatio[0]["lat"])
sääkysely = f"https://api.openweathermap.org/data/2.5/weather?lat={koordinaatit[1]}&lon={koordinaatit[0]}&appid={apikey}&units=metric"
sää = requests.get(sääkysely).json()
temperature = sää["main"]["temp"]
säätila = sää["weather"][0]["main"]
print(f"säätila: {säätila}\nlämpötila: {temperature}C")
