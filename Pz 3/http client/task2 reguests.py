import requests
from datetime import datetime, timedelta

BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_last_week_rates(currency="USD"):
    today = datetime.now()
    start_date = today - timedelta(days=7)

    result = []

    current_date = start_date
    while current_date <= today:
        date_str = current_date.strftime("%Y%m%d")
        url = f"{BASE_URL}?valcode={currency}&date={date_str}&json"

        response = requests.get(url)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            result.append({
                "date": data["exchangedate"],
                "rate": data["rate"]
            })

        current_date += timedelta(days=1)

    return result


if __name__ == "__main__":
    rates = get_last_week_rates("USD")
    for r in rates:
        print(f"{r['date']} : {r['rate']}")
