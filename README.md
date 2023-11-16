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
    <li><a href="#Methods">Methods</a></li>
    <li><a href="#Authors">Authors</a></li>
    <li><a href="#Organization-within-the-team">Organization within the team</a></li>
    <li><a href="#References">References</a></li>
  </ol>
</details>

## Abstract
Customers rely increasingly on product rating websites for making purchase decisions, and it has been proved that when rating a product, customers may be biased to follow other customers’ previous ratings of the same product (this phenomenon is know as "herding effect", see West et al. [[1]](#References)).

However, it is still an open research question to understand how ratings are influenced by the size of the vendor. By using data coming from beers' reviews websites, our goal is to analyze the relationship between the vendor size (breweries in this case), and the perceived quality of their products, determined through sentiment analysis of reviews. 
By quantifying brewery size through a [predefined metric](#Size-Index) and extracting sentiment from textual reviews, we aim to discern if there exists a correlation between these factors. Additionally, we seek to investigate the behavior of different consumer bases, addressing also the temporal dimension (how these phenomena have evolved through the years, but also through the seasons within the same year) and the spatial dimension (how these relationships differs through states and countries).

## Research Questions
The following questions do not comprise an exhaustive list. They serve to scope, inspire, and guide the analysis.

1) Probe if there exists any relationship between brewery size, as indicated by the number of beers offered and the volume of reviews received, and the perceived quality of their products, determined through sentiment analysis of reviews.
2) Investigate whether larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products that resonate with a niche audience of enthusiasts.
3) Find if there exists any dynamics between brewery size, consumer appeal, and product quality within the beer industry.
4) Address the temporal dimension, by trying to understand if there are any evolutions or differences within different seasons and different years.
5) Address the spatial dimension, by investigating if there are disparities between states and countries.

## Datasets
To answer those questions we used the following datasets:
- `BeerAdvocate` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/)
- `RateBeer` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [RateBeer.com](https://www.ratebeer.com/ratebeerbest/)

For milestone 2, our focus lies on `BeerAdvocate` because:
1) The dataset matched between BeerAdvocate and RateBeer almost share the same property with BeerAdvocate [[1]](#References). Hence, BeerAdvocate is assumed to contain representative features and statistics for both of the datasets.
2) RateBeer could be utilized to validate some of our future conlusions and therefore verity the robustness of our models.

## Methods
In this section, we will give an overview of the preprocessing, processing, and the data analysis part that had to be done to answer our RQs. Moreover, we will explain the problem-solving process as well as the feasibility of each task. 

#### Size Index
To numerically evaluate the size of a brewery, we built an index based on the following formula:
```math
Size = \alpha N_r + \beta N_b + \gamma N_t
```
With $N_r =$ number of reviews, $N_b =$ number of beers produced, $N_t =$ number of different types of beer produced.
#### Relationship between brewery size and perceived quality of the products
#### Analysis of specialization of reviewers compared to brewery size
#### Temporal dimension
#### Spatial dimension



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
|Analysis of specialization of reviewers compared to brewery size      | D                |   $9^{th}$ December  |
|Temporal dimension                           | L, F             |   $12^{th}$ December  |
|Spatial dimension                           |                  |    $15^{th}$ December  |
|Website                                            | T, L, D          |    $19^{th}$ December  |
|Data story writing                                 | T, D, L, G, A    |   $22^{th}$ December  |

*T = Tom, D = Dong, L = Leonardo, G = Gabriele, A = Axel


## References

[1] West R. et al.,  "When Sheep Shop: Measuring Herding Effects in Product
Ratings with Natural Experiments", 2020 https://dlab.epfl.ch/people/west/pub/Lederrey-West_WWW-18.pdf
