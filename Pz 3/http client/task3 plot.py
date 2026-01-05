import matplotlib.pyplot as plt
from task2_requests import get_last_week_rates


def plot_rates(currency="USD"):
    data = get_last_week_rates(currency)

    dates = [item["date"] for item in data]
    rates = [item["rate"] for item in data]

    plt.figure()
    plt.plot(dates, rates)
    plt.title(f"Курс {currency} за останній тиждень")
    plt.xlabel("Дата")
    plt.ylabel("Курс")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_rates("USD")
