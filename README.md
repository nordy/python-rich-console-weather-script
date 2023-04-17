# Python Rich Console Weather Script

## About

This is a **colorful command line** or console application that combines the past with the present and shows you the weather report in a different way. The primary purpose here is to teach while learning. The application queries the results according to the parameters you enter via **Open Weather Map** and prints it on the screen in a fancy way. The use of colors and tables is great with the **Rich** library. You keep track of what the application is working on and what it is doing on the screen until you get the results. Some error checks are also available within the app. In this simple application, I used popular and useful libraries such as **_Typer_**, **_Rich_**, **_Requests_** (api) and so on.

![Uygulama Ekran Görüntüsü](https://github.com/nordy/python-rich-console-weather-script/blob/main/screenshots/python_rich_weather_results_screen.jpg?text=Console+Results)

## Installation & Setup

- Install **python** recommended version 3.9.\* from https://www.python.org/
- Install source code via:

```bash
$ git clone https://github.com/nordy/python-rich-console-weather-script.git
$ cd python-rich-console-weather-script
$ chmod +x script.py
```

- Install required packages via:

```bash
$ pip install -r requirements.txt
```

- Generate your own **Open Weather Map _API Key_** for free on https://openweathermap.org/
- Enter your `API_KEY` in the `.ENV` file.

```
API_KEY = your_own_open_weather_map_api_key
URL = https://api.openweathermap.org/data/2.5/weather?
```

## Usage

If you used chmod like "chmod +x script.py"

```bash
$ ./script.py                            # runs for a random city - default unit is celsius.
$ ./script.py "New York"                 # runs for New York City - default unit is celsius.
$ ./script.py Berlin                     # runs for Berlin - default unit is celsius.
$ ./script.py "New York" --unit kelvin   # runs for New York City - unit is kelvin.
$ ./script.py --unit fahrenheit          # runs for a random city - unit is fahrenheit.
$ ./script.py --help                     # help
```

else

```bash
$ python script.py                            # runs for a random city - default unit is celsius.
$ python script.py "New York"                 # runs for New York City - default unit is celsius.
$ python script.py Berlin                     # runs for Berlin - default unit is celsius.
$ python script.py "New York" --unit kelvin   # runs for New York City - unit is kelvin.
$ python script.py --unit fahrenheit          # runs for a random city - unit is fahrenheit.
$ python script.py --help                     # help
```

## Terminal Outputs

Example screenshot for results using by:

```bash
$ python script.py London
```

![Uygulama Ekran Görüntüsü](https://github.com/nordy/python-rich-console-weather-script/blob/main/screenshots/python_rich_weather_results_screen.jpg?text=Console+Results)

## CLI

Get help screen or all available switches by using:

```bash
$ python script.py --help
```

![Uygulama Ekran Görüntüsü](https://github.com/nordy/python-rich-console-weather-script/blob/main/screenshots/python_rich_weather_help_screen.jpg?text=Console+Help+Screen)
