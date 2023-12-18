<div id="top"></div>

<br />
<div align="center">
<h1 align="center">Datastory - Does size matter?</h1>
</div>

## Introduction
Customers are increasingly relying on **product rating** websites to inform their purchasing decisions. It has been demonstrated that when customers rate a product, they often exhibit a **tendency to be influenced by the previous ratings** of other customers, a phenomenon known as the **_herding effect_**.

Despite this, an unresolved research question revolves around comprehending **how ratings might be impacted by the scale and the reputation of the vendor**. Utilizing data sourced from beer reviews websites, our objective is to investigate the **connection** between the **size and fame of vendors** (specifically, breweries) and **the perceived quality** of their products.

Through the quantification of brewery size and popularity using **predefined metrics** and the **extraction of sentiment** from textual reviews, we want to understand if a correlation exists between vendor size and notoriety and perceived product quality. Additionally, we want to **explore the behaviors** of diverse consumer bases, considering **temporal dimensions** (how these phenomena have evolved over the years and seasons within the same year) and **spatial dimensions** (how these relationships differ across states and countries).

The following datasets are used:
- `BeerAdvocate`: beer reviews from all over the world over a period that ranges between 1996 and 2017, collected on the website [BeerAdvocate.com](https://www.beeradvocate.com/)
- `RateBeer` (given to us): beer reviews from all over the world over a period that ranges between 2001 and 2017, collected on the website [RateBeer.com](https://www.ratebeer.com/ratebeerbest/)
- `1:110m Cultural Vectors`: Dataset with a map sourced from Geopandas (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).
- `GEOJSON AND KML DATA FOR THE UNITED STATES` : Geographical data for the United States (https://eric.clst.org/tech/usgeojson/)

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


## Part I: Is there any relationship between brewery size and popularity and the perceived quality of their products ?

## Part II: Do larger breweries tend to please a broader, potentially less sophisticated consumer base, while smaller breweries may craft more specialized, polarizing products, that resonate with a niche audience of enthusiasts ?

## Part III: Are there any evolutions or differences over the years ?

## Part IV: Do popular and/or big breweries tend to please a broader audience (spatial dimension) than less popular and/or smaller ones ?
