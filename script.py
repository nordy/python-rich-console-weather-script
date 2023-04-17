import requests
import random
import typer
import os

from time import sleep
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

os.system('cls')
console = Console()

tasks = ["Checking params...", "Loading variables...","Loading API data...", "Checking data...", "Preparing table..."]
units = ['standart', 'metric', 'imperial', 'kelvin', 'celsius', 'fahrenheit']


def loading_status(m, t):
    sleep(t)
    console.log(f"{m} [bold green]\tcomplete")


def intro_head():
    print(Panel("..:: [bright_blue]Py[/bright_blue][#ffd700]thon[/#ffd700] [green]Console[/green] [#ffaf00]Open Weather[/#ffaf00] [bright_black]script[/bright_black] using [red]Rich[/red] ::..", width=60))


def random_cities():
    return random.choice(["Berlin", "New York", "Istanbul", "London"])


def load_data(APIKEY, URL, UNITS, CITY):
    url = URL + "units=" + UNITS + "&appid=" + \
        APIKEY + "&q=" + CITY.replace(" ", "%20")
    r = requests.get(url).json()
    return r


def check_data(response):
    if (response['cod'] != 200):
        os.system('cls')
        console.line(count=2)
        print(Panel(f"{response['message'].capitalize()}", width=60))
        exit()


def check_unit(unit, units):
    unit = unit.lower()
    if unit not in units:
        os.system('cls')
        console.line(count=2)
        print(Panel("Type standart for Kelvin, metric for Celsius, imperial for Fahrenheit. Leave empty for default unit  Celsius.", width=60))
        exit()
    elif unit == "kelvin":
        return "standart"
    elif unit == "celsius":
        return "metric"
    elif unit == "fahrenheit":
        return "imperial"
    else:
        return unit


def result_table(city, response, unit):
    console.line(count=2)
    if unit == "standart":
        temp_sign = "K"
        ws_sign = "m/s"
        indicator_sign = "Kelvin"
    elif unit == "metric":
        temp_sign = "°C"
        ws_sign = "m/s"
        indicator_sign = "Celsius"
    else:
        temp_sign = "°F"
        ws_sign = "mi/h"
        indicator_sign = "Fahreheit"

    last_update = datetime.utcfromtimestamp(response['dt']+response['timezone']).strftime('%d %B,%Y %H:%M')

    table = Table(title=f"Results for [link=https://www.google.com/maps/place/{city.title().replace(' ','%20')}][bold red]{city.title()}[/bold red][/link],[#d7ff00]{response['sys']['country']}[/#d7ff00] on [deep_sky_blue1]{last_update}", title_justify="center", width=60)

    table.add_column(f"Indicators in [bright_green]{indicator_sign}[/bright_green]", style="bright_magenta")
    table.add_column("Values", justify="right", style="green")

    table.add_row(f"General Weather in [link=https://www.google.com/maps/place/{city.title().replace(' ','%20')}][bold red italic underline]{city.title()}[/bold red italic underline][/link]",f"{response['weather'][0]['description'].capitalize()}", style="on #1c1c1c")
    table.add_row("Temperature",f"{response['main']['temp']:.0f} [white]{temp_sign}[/white]")
    table.add_row("Feels like",f"{response['main']['feels_like']:.0f} [white]{temp_sign}[/white]", style="on #1c1c1c")
    table.add_row("Min[bright_black]|[/bright_black]Max Temperature",f"{response['main']['temp_min']:.1f}[bright_black]|[/bright_black]{response['main']['temp_max']:.1f} [white]{temp_sign}[/white]")
    table.add_row("[#af00ff]Pressure[/#af00ff]",f"{response['main']['pressure']} [white]hPa[/white]", style="on #1c1c1c")
    table.add_row("[#af00ff]Humidity[/#af00ff]",f"{response['main']['humidity']} [white]%[/white]")
    table.add_row("[#5f5fff]Wind Speed[bright_black]|[/bright_black]Direction[/#5f5fff]",f"{response['wind']['speed']} [white]{ws_sign}[/white] [bright_black]|[/bright_black] {response['wind']['deg']}[white]°[/white]", style="on #1c1c1c")
    table.add_row("[#ffd700]Sunrise[/#ffd700]",f"{datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone']).strftime('%H:%M:%S')}")
    table.add_row("[#ffd700]Sunset[/#ffd700]",f"{datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone']).strftime('%H:%M:%S')}", style="on #1c1c1c")

    console.print(table, justify="left")


def main(city: Optional[str] = typer.Argument(random_cities(), metavar="CITYNAME", help="Type the name of the city or location you want to know the weather forecast for."),
         unit: Optional[str] = typer.Option("metric", metavar="UNITNAME", help="standard for Kelvin, metric for Celsius and imperial for Fahrenheit. Typing Kelvin, Celsius, Fahrenheit will also work.")):
    """
    Enter the name of the city whose weather you want to know. If you leave it blank, a random city
    will be selected. The default unit for values is Celsius. For other units, you can enter kelvin or fahrenheit.
    For more information, visit https://github.com/nordy
    """
    intro_head()

    with console.status(spinner='simpleDotsScrolling', status="[bold green]Working on tasks...", spinner_style="bold red") as status:
        loading_status(tasks[0], 0.5)
        unit = check_unit(unit, units)

        loading_status(tasks[1], 0.5)
        load_dotenv(find_dotenv())
        APIKEY = os.getenv("API_KEY")
        URL = os.getenv("URL")

        loading_status(tasks[2], 0.5)
        response = load_data(APIKEY, URL, unit, city)

        loading_status(tasks[3], 0.5)
        check_data(response)

        loading_status(tasks[4], 0.5)
        result_table(city, response, unit)
        console.line(count=1)


if __name__ == "__main__":
    typer.run(main)
