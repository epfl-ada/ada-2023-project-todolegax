<div id="top"></div>

<br />
<div align="center">
<h1 align="center">Does size matter?</h1>
  <p align="center">
    Applied Data Analysis (CS-401)
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Abstract">Abstract</a></li>
    <li><a href="#Research-Questions">Research Questions</a></li>
    <li><a href="#Datasets">Datasets</a></li>
    <li><a href="#Metrics-Definition">Metrics Definition</a></li>
    <li><a href="#Methods">Methods</a></li>
    <li><a href="#Authors">Authors</a></li>
    <li><a href="#Organization-within-the-team">Organization within the team</a></li>
    <li><a href="#References">References</a></li>
  </ol>
</details>

## Abstract
Customers rely increasingly on product rating websites for making purchase decisions, and it has been proved that when rating a product, customers may be biased to follow other customers’ previous ratings of the same product (this phenomenon is know as "herding effect", see West et al. [[1]](#References)).

However, it is still an open research question to understand how ratings might be impacted by the scale and the reputation of the vendor. By using data coming from beers' reviews websites, our goal is to analyze the relationship between the vendor size and popularity (breweries in this case), and the perceived quality of their products, determined through sentiment analysis of reviews. 
By quantifying brewery size and popularity using [predefined metrics](#Metrics-Definition) and extracting sentiment from textual reviews, we aim to discern if there exists a correlation between these factors. Additionally, we seek to investigate the behavior of different consumer bases, addressing also the temporal dimension (how these phenomena have evolved through the years, but also through the seasons within the same year) and the spatial dimension (how these relationships differs through states and countries).

## Research Questions
The following questions do not comprise an exhaustive list. They serve to scope, inspire, and guide the analysis.

1) Probe if there exists any relationship between brewery size, beer popularity and the perceived quality of their products.
2) Investigate whether larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products that resonate with a niche audience of enthusiasts.
3) Find if there exists any dynamics between brewery size and popularity, consumer appeal, and product quality within the beer industry.
4) Address the temporal dimension, by trying to understand if there are any evolutions or differences within different seasons and different years.
5) Address the spatial dimension, by investigating if there are disparities between states and countries.

## Datasets
To answer those questions we used the following datasets:
- `BeerAdvocate` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/)
- `RateBeer` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [RateBeer.com](https://www.ratebeer.com/ratebeerbest/)

For milestone 2, our focus lies on `BeerAdvocate` because:
1) The dataset matched between BeerAdvocate and RateBeer almost shared the same properties with BeerAdvocate [[1]](#References). Hence, BeerAdvocate is assumed to contain representative features and statistics for both of the datasets.
2) RateBeer could be used to validate some of our future conclusions and therefore verity the robustness of our models. 

## Metrics Definition
In our analysis, we introduce *two key metrics* to quantitatively assess the characteristics of breweries: Size Metrics and Popularity Metrics.

#### Size Metric
To numerically evaluate the size of a brewery, we built an index based on the following formula:
```math
Size = \alpha N_r + \beta N_b + \gamma N_t
```
With $N_r =$ number of reviews, $N_b =$ number of beers produced, $N_t =$ number of different types of beer produced.

#### Popularity Metric
At the same time, to numerically evaluate the popularity of a brewery, we built an index based on the following formula:
```math
Popularity = \frac{N_r}{N_b}
```
With $N_r =$ number of reviews, $N_b =$ number of beers produced

## Methods
In this section, we will give an overview of the methods that will be used to answer our research questions. Moreover, we will explain the problem-solving process as well as the feasibility of each task.

In this repository, you'll find a notebook where we formulate some preliminar analysis and start to address our research questions.

#### Cleaning and preprocessing
Firstly we needed to clean and preprocess our dataset, by filtering and merging data. We also plotted some relevant distributions, in order to get a first visualization of the data in our possession. In particular, it was necessary to get insight into review length variation, as visualizing the distribution allowed us to understand the range and variability in review lengths. Analyzing review lengths served also as a quality check.

Afterwards, we improved consistency by translating all non-English textual reviews. To this end, we used the language detection module `detect` of the `langdetect` library to initially identify the language of each review. Due to the considerable computation time required for language detection, we decided to keep the language identifier of each review in a separate dataset (`Review_lang`), together with the unique identifiers of the beer and the user. During this first analysis, we had also to address the problem of handling special characters. To solve this problem, we used the html.unescape function to convert the HTML entities and then removed the non-ASCII characters by encoding them in ASCII and decoding them again.

Finally, we constructed the two metrics for our analysis, and visualize the distributions of breweries with respect to this metric size. We then compared the results obtained with both metrics, drawning some first conclusions.

#### Relationship between brewery size, popularity and perceived quality of the products
This section's objective is to analyze the possible relationship between brewery size and popularity and the perceived quality of their products. The idea would be to use both the numerical ratings given by the users and a sentiment analysis of the textual reviews on one hand, and the indices given by the metrics on the other hand, to see if we there exists any correlation or patterns.

The sentiment analysis of the reviews would be exploited through the usage of some natural language processing frameworks, such as !!!!!!!!! PUT SOMETHING !!!!!!!!

#### Geographical Analysis
The goal is to gain insights into the geographical distribution of both breweries and reviewers within the dataset. Ultimately, we aim to calculate the distances between breweries and their respective reviewers. This analysis could potentially unveil distinctions between brewery types, revealing whether certain types of breweries attract predominantly local reviewers or have a more globally dispersed audience.

We initialized our analysis by examining the geographical distribution of breweries in the dataset. To achieve this, we integrated the dataset with a map sourced from Geopandas.
Ensuring alignment between the country names used in the map and those in the brewery dataset is crucial. To address this, we calculated the Hamming distance between them and substituted the brewery location with the closest match. In instances where no match was found, we opted to eliminate the corresponding brewery. For breweries located in the USA, the dataset includes information about the state. Consequently, we extended the same process to the states in the United States of America. 
We then explored the Top 10 countries with the highest number of breweries to gain insights into the global distribution of brewing establishments. Additionally, we visualized the global distribution of breweries to gain a comprehensive understanding of their geographical spread.

After applying a similar analysis to reviewers data, we explored the relative distance between the reviewer and the brewery for each review, aiming to provide insights into how the popularity of a brewery is distributed globally.

#### Temporal Analysis
In this section, our aim is to investigate the temporal evolution of the beer market from the perspective of user ratings and reviews. Aligned with our interest in how brewery size and popularity matter, we pay specific attention to how the ratings and reviews are distributed among breweries.

In the notebook, we sketched out a first draft of the analysis. The final goal would be to see if we can find any dynamic in the indices defined by the metrics, and therefore if there are any patterns or evolutions in popularity and quality perception from users, both through the years but also in different periods of the year.

#### Analysis of specialization of reviewers compared to brewery size and popularity
In this part of the analysis, we aim to inspect whether larger or popular breweries might lean to please a broader and less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products that resonate with a niche audience of enthusiasts.

We plan to tackle this topic through the exploitation of 


## Authors

The `ToDoLeGAx` team is composed of:
- Tom Fahndrich: [@TomFahndrich](https://github.com/tomfahndrich)  
- Dong Chu: [@DongChu](https://github.com/chudonguestc)  
- Leonardo Trentini: [@LeonardoTrentini](https://github.com/leotrentini22)
- Gabriele D'Angeli: [@GabrieleDAngeli](https://github.com/gabrieledangeli)
- Axel Beguelin: [@AxelBeguelin](https://github.com/AxelBegue)

## Organization within the team


|Task                        | Responsibility * |Timeline             |
|----------------------------|------------------|-----------------------------|
|Relationship brewery size - perceived quality | T, A             |  $6^{th}$ December  |
|Analysis of specialization of reviewers compared to brewery size      | D, G                |   $9^{th}$ December  |
|Temporal dimension                           | L, G             |   $9^{th}$ December  |
|Spatial dimension                           | T, A                |    $12^{th}$ December  |
|Website                                            | L, D, T          |    $19^{th}$ December  |
|Data story writing                                 | T, D, L, G, A    |   $22^{th}$ December  |

*T = Tom, D = Dong, L = Leonardo, G = Gabriele, A = Axel


## References

[1] West R. et al.,  "When Sheep Shop: Measuring Herding Effects in Product
Ratings with Natural Experiments", 2020 https://dlab.epfl.ch/people/west/pub/Lederrey-West_WWW-18.pdf
