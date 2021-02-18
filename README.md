# Henry Hub Natural Gas Daily Prices

This repository contains data scraped from the Henry hub website. Data includes the date and prices of natural gas in Dollars per Million Btu. A CSV file containing the data generated is located in the folder [datapackage](https://github.com/DevTotti/Henry-Hub-Daily-Prices/tree/master/datapackage)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required package [BeautifulSoup](https://pypi.org/project/bs4/)

```bash
pip install -r requirements.txt
```

## Usage
To run the program, run
```
python app.py
```
This generates a new CSV file in the [datapackage] folder

The output CSV is displayed in a tabular format on [github](https://github.com/DevTotti/Henry-Hub-Daily-Prices/blob/master/datapackage/Henry%20Hub%20Daily-gas-prices.csv)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[MIT](https://choosealicense.com/licenses/mit/)