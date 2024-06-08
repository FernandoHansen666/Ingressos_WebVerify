import requests
from bs4 import BeautifulSoup
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import datetime
import pywhatkit as kit

current_time = datetime.datetime.now()

# URL e string alvo
url = 'https://www.h2hc.com.br/'
target_string = 'Em breve anunciaremos o proximo evento'
previous_content = None

# Configuração do WebDriver
options = uc.ChromeOptions()
options.add_argument('--headless')  # Executar o navegador em modo headless
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=options)
print(current_time)

def fetch_site_content(url):
    driver.get(url)
    sleep(5)  # Espera para garantir que a página carregue completamente
    try:
        content = driver.find_element(By.ID, 'countdown')
        div_content = content.text.strip()
        print(f"Conteúdo da div: {div_content}")  # Print do conteúdo da div para debug
        return div_content
    except Exception as e:
        print(f"Erro ao buscar conteúdo: {e}")
        return None

def send_whatsapp_message(phone_number, message):
    now = datetime.datetime.now()
    send_time = now + datetime.timedelta(minutes=1)
    kit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)

def send_discord_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Mensagem enviada com sucesso para o Discord")
    else:
        print(f"Falha ao enviar mensagem para o Discord: {response.status_code}")

phone_number = '+NumeroWhats'
whatsapp_message = 'Ingressos H2HC Liberados'
discord_webhook_url = 'https://discord.com/api/webhooks/1248861708739674134/FTW_PvQhkQrhcjFlonYUZ9z'
discord_webhook_url2 = 'https://discord.com/api/webhooks/1248861708739674134/FTW_PvQhkQrhcjFlonYUZ9'
discord_message = 'Ingressos H2HC Liberados'

send_discord_message(discord_webhook_url2, "Verificador de ingressos Online!")
send_discord_message(discord_webhook_url2, "Verificador de ingressos Online!")

while True:
    current_content = fetch_site_content(url)
    if current_content != previous_content:
        previous_content = current_content
        print(f"Conteúdo da div atualizado: {current_content}")
        send_whatsapp_message(phone_number, whatsapp_message)
        send_discord_message(discord_webhook_url, discord_message)
        send_discord_message(discord_webhook_url2, discord_message)
        sleep(60)  # Espera por 1 minuto
    else:
        print("Conteúdo da div não mudou.")
        print("TIMESTAMP:", current_time)
        sleep(300)  # Espera por 5 minutos
