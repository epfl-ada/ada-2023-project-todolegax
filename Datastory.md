<div id="top"></div>

<br />
<div align="center">
<h1 align="center">Datastory - Does size matter?</h1>
</div>

## Introduction
Customers are increasingly relying on **product rating** websites to inform their purchasing decisions. It has been demonstrated that when customers rate a product, they often exhibit a **tendency to be influenced by the previous ratings** of other customers, a phenomenon known as the **_herding effect_**.

Despite this, an unresolved research question revolves around comprehending **how ratings might be impacted by the scale and the reputation of the vendor**. In order to try to answer rapidly to this question, the new Dean at EPFL decided to outsource the task to a brand-new data science spinoff of the University, the ToDoLeGAx SA. Utilizing data sourced from beer reviews websites, ToDoLeGAx's objective is to investigate the **connection** between the **size and fame of vendors** (specifically, breweries) and **the perceived quality** of their products.

Through the quantification of brewery size and popularity using **predefined metrics** and the **extraction of sentiment** from textual reviews, we want to understand if a correlation exists between vendor size and notoriety and perceived product quality. Additionally, we want to **explore the behaviors** of diverse consumer bases, considering **temporal dimensions** (how these phenomena have evolved over the years and seasons within the same year) and **spatial dimensions** (how these relationships differ across states and countries).

## ToDoLeGAx team line-up
In order to accomplish the goal, the Board of Directors at ToDoLeGAx SA. decided to create a new task force, specifically disegned for this project. Here is the line-up of our team:

- Dong Chu: [@DongChu](https://github.com/chudonguestc), Head of the Web Development department
- Leonardo Trentini: [@LeonardoTrentini](https://github.com/leotrentini22), intern in the Web Development department
- Gabriele D'Angeli: [@GabrieleDAngeli](https://github.com/gabrieledangeli), senior engineer of the NLP department
- Tom Fahndrich: [@TomFahndrich](https://github.com/tomfahndrich), senior R&D engineer in the Data analysis department
- Axel Beguelin: [@AxelBeguelin](https://github.com/AxelBegue), junior R&D engineer in the Data analysis departmen

## Dive into our datasets

The first step to dive into our story is to understand our datasets. Our main source of data is the `BeerAdvocate` dataset, that contains beer reviews from all over the world over a period that ranges between 1996 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/).
After the preprocessing, the dataset contains $42'923$ beers, $58'199$ users, $14'158$ breweries and a total of $2'587'598$ reviews.

![cat](./plots/dataset_distrib_by_year.png)

INSERT SOME PLOTS ABOUT DATASET DISTRIBUTIONS

Two other datasets that will be helpful for our analysis, and in particular for the geographical investigation, are:
- `1:110m Cultural Vectors`: dataset with a map sourced from Geopandas (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).
- `GEOJSON AND KML DATA FOR THE UNITED STATES` : geographical data for the United States (https://eric.clst.org/tech/usgeojson/)

## Metrics Definition
To quantitatively **assess the characteristics of breweries**, we introduce a key metric, the **Size Metric**.

####  **Size Metrics**

$$ \text{Size} = \alpha N_r + \beta N_b + \gamma N_t$$

With:
- $N_r =$ number of reviews normalized by the total number of reviews
- $N_b =$ number of beers produced normalized by the total number of beers
- $N_t =$ number of different types (style) of beer produced normalized by the total number of styles

The metric is then normalized to get values between 0 and 1.

![cat](./plots/size_metric_distribution.png)

## What is the relationship between brewery size and the perceived quality of their beers?

![cat](./plots/average_rating_vs_size.png)

<img src="./plots/average_rating_vs_size.png" alt="Cat" width="400" height="250">

We can also perform a regression analysis between the average rating and the size metric.

We now compute the mean and standard deviation of the ratings for each of the 3 brewery size categories (small, medium, big) to see if there is some statistical differencens in terms of ratings.

![cat](./plots/division_small_medium_big_breweries.png)

We perform t-test anlysis at the 0.05 significance level under the hypotesis $H_0$ : *There is no statistically significant difference in average rating between the breweries size categories.* To see if the size category of a brewery impacts the average rate obtained:

T-statistic: -23.2306
P-value: 0.00000000
The difference in avg. rating is statistically significant between small and medium breweries.

T-statistic: -3.4624
P-value: 0.00077318
The difference in avg. rating is statistically significant between medium and big breweries.

We can conclude that there is likely to be a significant (at significance level 0.05) statisticall difference between the small, medium and large breweries in term of rating obtained. Given the plot just on top, being a bigger breweries tend to increase the mean rating obtained and reduce the standard deviation.

## Reviews' length VS breweries' size

We do the same analysis but to see if the brewery size metrics impacts the average review length obtained by the breweries

![cat](./plots/review_length.png)

We perform t-test anlysis at the 0.05 significance level under the hypotesis $H_0$ : *There is no statistically significant difference in average review length between the breweries size categories.* To see if the size category of a brewery impacts the average review length obtained.

T-statistic: -12.7465
P-value: 0.00000000
The difference in avg. review length is statistically significant between small and medium breweries.

T-statistic: -6.4931
P-value: 0.00000000
The difference in avg. review length is statistically significant between medium and big breweries.

## Are there different behaviors in different places?

The goal of this section is to gain insights into the geographical distribution of both breweries and reviewers within the dataset. Ultimately, we aim to calculate the distances between breweries and their respective reviewers. This analysis could potentially unveil distinctions between brewery types, revealing whether certain types of breweries attract predominantly local reviewers or have a more globally dispersed audience.

We initiate our analysis by examining the geographical distribution of breweries in the dataset. To achieve this, we integrate the dataset with a map sourced from Geopandas (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).

Ensuring alignment between the country names used in the map and those in the brewery dataset is crucial. To address this, we calculate the Hamming distance between them and substitute the brewery location with the closest match. In instances where no match is found, we opt to eliminate the corresponding brewery. This scenario applies to 26 breweries out of over 14,000, which is deemed acceptable for this level of analysis. It's worth noting that some removed breweries had HTTP links as their location, explaining the lack of match with the map.

For breweries located in the USA, the dataset includes information about the state. Consequently, we extend the same process to the states in the United States of America. To facilitate this, we introduce a new column, 'state,' in the dataframe. This allows us to split the location of US breweries into 'country' and 'state.' 

The geodataframe for the USA can be accessed here: https://eric.clst.org/tech/usgeojson/

As evident from the data, **there are significantly more breweries in the US** compared to other countries. Due to this notable concentration, we will consider the breweries by states in the next section. To facilitate this, we extend the world geodataframe by incorporating the US state geodataframe in the next section.

Let's look again to the Top 10 countries with the highest number of breweries. However, this time, we'll consider **each US state as a distinct 'country'.** Additionally, we'll **visualize the global distribution of breweries** to gain a comprehensive understanding of their geographical spread.

![cat](./plots/distribution_breweries_world.png)

The revised analysis reveals distinct results. Germany takes the lead, followed by Finland, and several US states are now present in the Top 10. The conclusion of this analysis is that there are many more breweries in the US than anywhere else in the world. Acknowledging this, it becomes essential to consider the US's internal diversity in subsequent analyses. Given the availability of information about individual US states, incorporating them into the analysis could provide valuable insights, offering a more nuanced understanding of the brewing landscape within the country.

Now that we have gained insights into the distribution of breweries worldwide, we can apply a **similar analysis** to the **user data**. The aim of this analysis is to see whether or not a geographical similarity can be observed between the distribution of breweries and the distribution of users who give reviews. Once again, a matching process based on Hamming's distance must be performed to match the names of the different places.

![cat](./plots/distribution_reviewers_world.png)

![cat](./plots/relative_distance_reviewers_breweries.png)

![cat](./plots/distance_vs_size_metric.png)


## Part II: Do larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products, that resonate with a niche audience of enthusiasts ?

## Part III: Are there any evolutions or differences over the years ?

![cat](./plots/average_ratings_by_year.png)

![cat](./plots/trend_percentage_reviews.png)

## Part IV: Do popular and/or big breweries tend to please a broader audience (spatial dimension) than less popular and/or smaller ones ?
