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
Customers are increasingly relying on **product rating** websites to inform their purchasing decisions. It has been demonstrated that when customers rate a product, they often exhibit a **tendency to be influenced by the previous ratings** of other customers, a phenomenon known as the **_herding effect_**, (see West et al. [[1]](#References)).

Despite this, an unresolved research question revolves around comprehending **how ratings might be impacted by the scale and the reputation of the vendor**. Utilizing data sourced from beer reviews websites, our objective is to investigate the **connection** between the **size and fame of vendors** (specifically, breweries) and **the perceived quality** of their products.

Through the quantification of brewery size and popularity using **predefined metrics** and the **extraction of sentiment** from textual reviews, our aim is to ascertain whether a correlation exists between vendor size and notoriety and perceived product quality. Additionally, we plan to **explore the behaviors** of diverse consumer bases, considering **temporal dimensions** (how these phenomena have evolved over the years and seasons within the same year) and **spatial dimensions** (how these relationships differ across states and countries).

## Research Questions
1) Is there any relationship between brewery size and popularity and the perceived quality of their products ?
2) Do larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products, that resonate with a niche audience of enthusiasts ?
3) Is there any dynamics between brewery size and popularity, consumer appeal, and product quality within the beer industry ?
4) Are there any evolutions or differences over the years ?
5) Do popular and/or big breweries tend to please a broader audience (spatial dimension) than less popular and/or smaller ones ?

## Datasets
The following datasets are used:
- `BeerAdvocate`: beer reviews from all over the world over a period that ranges between 1996 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/)
- `RateBeer` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [RateBeer.com](https://www.ratebeer.com/ratebeerbest/)
- `1:110m Cultural Vectors`: Dataset with a map sourced from Geopandas (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).
- `GEOJSON AND KML DATA FOR THE UNITED STATES` : Geographical data for the United States (https://eric.clst.org/tech/usgeojson/)

For milestone 2, our focus lies on `BeerAdvocate` because:
1) The dataset matched between BeerAdvocate and RateBeer almost shared the same properties with BeerAdvocate [[1]](#References). Hence, BeerAdvocate is assumed to contain representative features and statistics for both of the datasets.
2) RateBeer could be used to validate some of our future conclusions and therefore verify the robustness of our models. 

## Metrics Definition
We introduce **two key metrics** to quantitatively **assess the characteristics of breweries**: Size Metrics and Popularity Metrics. Since we don't have data about the revenue or number of liter produced by the brewery, we decided to base ourself on variable present in the dataset to construct these metrics. Some verification will be done by hand, by searching information about some breweries on the web to assess the quality of the metrics and to correct the coefficients if needed.

####  **Size Metrics**

$$ \text{Size} = \alpha N_r + \beta N_b + \gamma N_t$$

With:
- $N_r =$ number of reviews normalized by the total number of reviews
- $N_b =$ number of beers produced normalized by the total number of beers
- $N_t =$ number of different types (style) of beer produced normalized by the total number of styles

#### **Popularity Metrics**
$$ \text{Popularity} = \dfrac{N_r}{N_b}$$

With $N_r =$ number of reviews, $N_b =$ number of beers produced


Both metrics are normalized to get a value between 0 and 1.

We are aware that these metrics do not fully represent the size and popularity of a brewery in its entireness, but they do provide an approximation based on available data.

## Methods

#### Cleaning and preprocessing
Initially, we cleaned and preprocessed the dataset by filtering and merging data, creating visualizations to understand review length variation for quality checking. We enhanced consistency by translating non-English reviews using language detection via the `langdetect` library. To manage computation time, we stored language identifiers separately in a dataset (`Review_lang`). Handling special characters involved using html.unescape and encoding non-ASCII characters to ASCII. Lastly, we created two metrics, visualized brewery distributions based on these metrics, and drew initial conclusions from the comparison.

#### Relationship between brewery size, popularity and perceived quality of the products
We aim to analyze the possible relationship between brewery size and popularity and the perceived quality of their products. The idea would be to use both the numerical ratings given by the users and a sentiment analysis of the textual reviews on one hand, and the indices given by the metrics on the other hand, to see if there exists any correlation or patterns.

The sentiment analysis of the reviews would be exploited through the usage of some natural language processing frameworks, such as Python NLTK (natural language toolkit).

#### Geographical and Temporal Analysis
The objective here is to analyze the geographical distribution of breweries and reviewers in the dataset, with a focus on calculating distances between breweries and their respective reviewers. This can reveal distinctions in brewery types, indicating whether certain types attract local or global audiences.

To begin, we integrated the dataset with a map using `Geopandas` to examine the geographical distribution of breweries. Alignment of country names between the map and dataset was ensured by calculating Hamming distances using `difflib` and substituting unmatched brewery locations or eliminating them. For U.S. breweries, a similar process was applied to states.

Top 10 countries with the most breweries were explored to understand global distribution. Visualization further provided insights into the global spread of breweries.

After applying a similar analysis to reviewers data, the goal is to explore the relative distance between the reviewer and the brewery for each review and look for correlation between the distance and the size or popularity.

The notebook includes a preliminary **temporal analysis** draft, aiming to identify patterns or evolutions in popularity and quality perception over the years and different periods.

#### Analysis of specialization of reviewers compared to brewery size and popularity
We will look if there is some correlation between the quality of reviews and the brewery size or popularity. The quality of review will be assesed by text analysis (vocabulary, length, completeness).


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
|Relationship brewery size/popularity - perceived quality | T, A             |  $6^{th}$ December  |
|Analysis of specialization of reviewers compared to brewery size/popularity      | D, G                |   $9^{th}$ December  |
|Temporal dimension                           | L, G             |   $9^{th}$ December  |
|Spatial dimension                           | T, A                |    $12^{th}$ December  |
|Website                                            | L, D, T          |    $19^{th}$ December  |
|Data story writing                                 | T, D, L, G, A    |   $22^{th}$ December  |

*T = Tom, D = Dong, L = Leonardo, G = Gabriele, A = Axel


## References

[1] West R. et al.,  "When Sheep Shop: Measuring Herding Effects in Product
Ratings with Natural Experiments", 2020 https://dlab.epfl.ch/people/west/pub/Lederrey-West_WWW-18.pdf
