from dotenv import load_dotenv
import httpx
import os

load_dotenv()

url = os.environ["BITRIX24_WEBHOOK_KEY"]

response = httpx.post(
    url + "crm.item.add.json",
    json={
        "entityTypeId": 2,
        "fields": {
            "title": "Заявка из Telegram"
        }
    },
    timeout=15
)

response.raise_for_status()
print(response.json())