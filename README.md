# Pokécrawl
This is a project to crawl [pokemon.com](https://www.pokemon.com/us/) pages in order to have English-French datasets.

##Install
In this project we are using Pipenv for dependency and virtualenv management. To install dependencies, run:

`pipenv install`

Alternatively, you can install dependencies from the requirements.txt file using:

`pip install -r requirements.txt`

##Usage
To crawl the pages of your choice, use the corresponding spider:

`scrapy crawl spider_name`

For example, to crawl Pokémon TCG card names and output the result to a .json file, use:

`scrapy crawl card_names -O output.json`
