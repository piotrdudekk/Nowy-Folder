# Nowy-Folder
## Stage 1 - extraction of all components for single opinion
1. Extraction of single web page content
2. Analisys of single opinion structure

|Component|CSS Selector|Variable name|Data type|
|---------|------------|-------------|---------|
|Opinion|div.js_product-review|dict|
|Opinion id|["data-entry-id"]|opinion_id|str|
|Author|span.user-post__author-name|author|str|
|Recommendation|span.user-post__author-recomendation > em|recommendation|bool|
|Stars rating|span.user-post__score-count|stars|float|
|Content|div.user-post__text|content|str|
|Advantages|div.review-feature__col:has(> div[class$="positives"]) > div.review-feature__item|pros|list(str)|
|Disadvantages|div.review-feature__col:has(> div[class$="negatives"]) > div.review-feature__item|cons|list(str)|
|Verification|div.rewiev-pz|verified|bool|
|Post date|span.user-post__published > time:nth-child(1)["datetime"]|post_date|str|
|Purchase date|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
|Usefulness count|span[id^="votes-yes"]|usefulness|int|
|Uselessness count|span[id^="votes-no"]|uselessness|int|

3. Extraction of single opinion components
4. Transormation of extrated data to given data types

## Stage 2 - extraction of all opinions for single page
1. Definition of dictionary to store all components of single opinion
2. Definition of list for opinions' dictionaries storing
3. Implementation of loop traversing trough all opinions from single page

## Stage 3 - extraction of all opinions for single product
1. Implementation of loop traversing trough consecutive pages with opinions
2. Loading extracted opinions to .json files
3. Parametrization of product id and reading product id from standard input

## Stage 4 - code refactoring
1. Implementation of component extraction function
2. Using dictionary with components selectors and comprehension for single opinion representation

## Stage 5 - statistical analisys of extracted opinions
1. Displaying list of products for which opinion have been extracted

## Stage 6 - drawing charts based on given data