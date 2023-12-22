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

Despite this, an unresolved research question revolves around comprehending **how ratings might be impacted by the scale of the vendor**. Utilizing data sourced from beer reviews websites, our objective is to investigate the **connection** between the **size of vendors** (specifically, breweries) and **the perceived quality** of their products.

Through the quantification of brewery size using **predefined metric** and the **extraction of sentiment** from textual reviews, our aim is to ascertain whether a correlation exists between vendor size and notoriety and perceived product quality. Additionally, we plan to **explore the behaviors** of diverse consumer bases, considering **temporal dimensions** (how these phenomena have evolved over the years and seasons within the same year) and **spatial dimensions** (how these relationships differ across states and countries).

## Research Questions
- Is there any relationship between brewery size and the perceived quality of their products?
- Do larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products, that resonate with a niche audience of enthusiasts?
- Are there any evolutions or differences over the years?
- Do big breweries tend to please a broader audience (spatial dimension) than smaller ones?

## Datasets
The following datasets are used:
- `BeerAdvocate`: beer reviews from all over the world over a period that ranges between 1996 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/)
- `RateBeer` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [RateBeer.com](https://www.ratebeer.com/ratebeerbest/)
- `1:110m Cultural Vectors`: Dataset with a map sourced from Geopandas (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).
- `GEOJSON AND KML DATA FOR THE UNITED STATES` : Geographical data for the United States (https://eric.clst.org/tech/usgeojson/)

Our focus lies on `BeerAdvocate` because:
1) The dataset matched between BeerAdvocate and RateBeer almost shared the same properties with BeerAdvocate [[1]](#References). Hence, BeerAdvocate is assumed to contain representative features and statistics for both of the datasets.
2) `RateBeer` was then used to validate our conclusions and therefore verify the robustness of our models. 

## Metrics Definition
In our analysis, we aim to introduce **two key metrics** to quantitatively assess the characteristics of breweries: 
- **Size Metrics** 
- **Popularity Metrics**

The following cells present and compute these metrics. Given the absence of data regarding brewery revenue or the quantity of liters produced, we have chosen to rely on variables available in the dataset to formulate these metrics.

$\begin{equation}
\begin{aligned}
    \\
    &\text{Size Metrics} = \alpha \log (N_r) + \beta \log (N_b) + \gamma \log (N_t) \\
    \\
    &\text{Popularity Metrics} = \dfrac{\log (N_r)}{N_b} \\
\end{aligned}
\end{equation}$

With:
- $N_r =$ number of reviews received during the year
- $N_b =$ number of different beers that recieved reviews
- $N_t =$ number of different types (style) of beers that recieved reviews

The coefficients $\alpha, \beta, \gamma$ are manually set to 5, 2, and 1, respectively. This way, we put more wheight on the number of reviews, because we expect a bigger brewery to receive more reviews than a smaller one. The metrics are calculated for each brewery annually. 

For each year, the result for each brewery is normalized by dividing it by the maximum value of the year. This normalization process yields a value between 0 and 1 for each brewery, with the largest brewery of the year assigned a size index of 1.

Finally, to assess the size and popularity globally, we define the "macro" metrics as the mean of the metrics over the years. This will allow for general analysis over the entire dataset.

The popularity metric turned out to be significantly skewed in comparison to the size metric. Despite several unsuccessful attempts to adjust it, we have decided to **focus solely on the size metric**. The size metrics exhibits a more natural distribution, enabling a clear distinction between small and large breweries unlike the popularity metric. 

Moreover, our study primarily aims to explore how the **size** influences beer reviews and perceived quality which is better encoded by the size metrics. To validate the quality of the size metric, we compare its values (for selected breweries) with data sourced from the web. This comparison is outlined below:

## Methods

#### Cleaning and preprocessing
Initially, we cleaned and preprocessed the dataset by filtering and merging data, creating visualizations to understand review length variation for quality checking. We enhanced consistency by translating non-English reviews using language detection via the `langdetect` library. To manage computation time, we stored language identifiers separately in a dataset (`Review_lang`). Handling special characters involved using html.unescape and encoding non-ASCII characters to ASCII. Lastly, we created two metrics, visualized brewery distributions based on these metrics, and drew initial conclusions from the comparison.

#### Relationship between brewery size, popularity and perceived quality of the products
The goal was to analyze the possible relationship between brewery size and the perceived quality of their products. The idea was to use both the numerical ratings given by the users and a sentiment analysis of the textual reviews on one hand, and the indices given by the metric on the other hand, to see if there exists any correlation or patterns.

The **Sentiment Analysis** of text reviews also represents an important aspect of our investigation, as we want to **extract information from users feedback, trying to deduce what people think about a product from text only**.

To conduct a Sentiment Analysis, we utilize the [VADER](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and sEntiment Reasoner) library. This tool is a lexicon and rule-based sentiment analysis tool specifically designed to capture sentiments expressed in social media.

#### Geographical and Temporal Analysis
The objective here is to analyze the geographical distribution of breweries and reviewers in the dataset, with a focus on calculating distances between breweries and their respective reviewers. This can reveal distinctions in brewery types, indicating whether certain types attract local or global audiences.

To begin, we integrated the dataset with a map using `Geopandas` to examine the geographical distribution of breweries. Alignment of country names between the map and dataset was ensured by calculating Hamming distances using `difflib` and substituting unmatched brewery locations or eliminating them. For U.S. breweries, a similar process was applied to states.

Top 10 countries with the most breweries were explored to understand global distribution. Visualization further provided insights into the global spread of breweries.

After applying a similar analysis to reviewers data, the goal was to explore the relative distance between the reviewer and the brewery for each review and look for correlation between the distance and the size or popularity.

The notebook includes also a **temporal analysis**, through which we aimed to identify patterns or evolutions in popularity and quality perception over the years and different periods.
Finally, we also identified a particular brewery that experienced a perceivable growth during the period taken into account, in order to see if we could measure any evolution also in ratings and basin of attraction of users during the years.

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
|Temporal dimension                           | T, A             |   $9^{th}$ December  |
|Spatial dimension                           | T, A                |    $12^{th}$ December  |
|Sentiment Analysis                        | G            | $19^{th}$ December  |
|Website                                            | L, D         |    $19^{th}$ December  |
|Data story writing                                 | L, D    |   $22^{th}$ December  |

*T = Tom, D = Dong, L = Leonardo, G = Gabriele, A = Axel


## References

[1] West R. et al.,  "When Sheep Shop: Measuring Herding Effects in Product
Ratings with Natural Experiments", 2020 https://dlab.epfl.ch/people/west/pub/Lederrey-West_WWW-18.pdf
