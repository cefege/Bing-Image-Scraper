# Bing Scraper

This Python script is used to scrape images from Bing search engine and remove duplicate URLs. It reads data from a CSV file that contains search queries and stores the scraped image URLs in another column of the same CSV file.

## Installation

This script requires Python 3 to be installed on your machine.

To install the required packages, run the following command:

```sh
pip install pandas
```

## Usage

To use this script, create a CSV file with the following columns:

- `project_name`: the name of the project.
- `query`: the search query for Bing.
- `supporting_seed_keywords`: additional keywords to assist Bing with the search.

Then, execute the script with the path to your CSV file as the only argument:

```sh
python BingScraper.py path/to/your/csv/file.csv
```

The script will read your CSV file and scrape images for each search query in the `query` column. The resulting image URLs will be stored in the `supporting_seed_keywords` column, separated by commas.

Note that this script may take some time to complete, depending on the number of search queries and the number of images to be downloaded per query.
