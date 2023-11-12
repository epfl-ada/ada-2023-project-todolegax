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
    <li><a href="#Size-Index">Metric</a></li>
    <li><a href="#Datasets-and-Methods">Datasets and Methods</a></li>
    <li><a href="#Authors">Authors</a></li>
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

## Size Index
To numerically evaluate the size of a brewery, we built an index based on the following formula:
```math
Size = \alpha N_r + \beta N_b + \gamma N_t
```
With $N_r =$ number of reviews, $N_b =$ number of beers produced, $N_t =$ number of different types of beer produced.

## Datasets and Methods
- The reviews under analysis come from two different rating sites, `BeerAdvocate` and `RateBeer`, with thousands of reviews that span in a period from 2001 to 2017.


## Authors

The `ToDoLeGAx` team is composed of:
- Tom Fahndrich: [@TomFahndrich](https://github.com/tomfahndrich)  
- Dong Chu: [@DongChu](https://github.com/chudonguestc)  
- Leonardo Trentini: [@LeonardoTrentini](https://github.com/leotrentini22)
- Gabriele D'Angeli: [@GabrieleDAngeli](https://github.com/gabrieledangeli)
- Axel Beguelin: [@AxelBeguelin](https://github.com/AxelBegue)

## References

[1] West R. et al.,  "When Sheep Shop: Measuring Herding Effects in Product
Ratings with Natural Experiments", 2020 https://dlab.epfl.ch/people/west/pub/Lederrey-West_WWW-18.pdf
