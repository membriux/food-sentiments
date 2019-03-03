# Food-Sentiment
Web app that tells you what people are feeling about certain food items from the YelpAPI.

While reading reviews from the business, you might notice that the ratings don't match with the sentiment analysis. That's because an rating number tells one side of the story, but the sentiments of users tell another.

## How it works

Type inputs for the food item and location you want to search and the app will return a table showing the information about each business (specially the sentiment analysis). User can click on the name of the business and it will take them to a page showing the analyzed reviews with the sentiment score of each.

## Video Walkthrough/Example

Coming soon…

## Built With

* [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3) - Used to collect data
* [Flask](http://flask.pocoo.org/) - Web development framework for Python
* [TextBlob](https://textblob.readthedocs.io/en/dev/) - Text processing/Sentiment Analysis

## Authors

* **Guillermo Sanchez** - [Membriux](https://github.com/membriux)
    - Initial deign/planning/prototying
    - MVC Architecture design + implementation
    - Flask framework implementation
    - TextBlob implementation
* **Josh Tavassolikhah** - [JoshTavasso](https://github.com/JoshTavasso)
    - Initial design/planning/prototyping
    - Created Data Models: Business and Reviews class
    - More…

## License

    Copyright 2019 Guillermo Sanchez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
