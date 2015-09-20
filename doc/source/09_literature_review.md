# Literature Review

<!--
After the introductory chapter, it seems fairly common to 
include a chapter that reviews the literature and 
introduces methodology used throughout the thesis.
-->

## Introduction

motivation: a system that gathers openly available government data, processes it, does forecasting with state of the art methods, does not exist.

This is the introduction. Duis in neque felis. In hac habitasse platea dictumst. Cras eget rutrum elit. Pellentesque tristique venenatis pellentesque. Cras eu dignissim quam, vel sodales felis. Vestibulum efficitur justo a nibh cursus eleifend. Integer ultrices lorem at nunc efficitur lobortis.

## Time Series Reconstruction

This is the literature review. Nullam quam odio, volutpat ac ornare quis, vestibulum nec nulla. Aenean nec dapibus neque. Mathematical formula can be inserted using Latex:

### Inference and Missing Data
[@rubin-missing]

(@ref_for_eqn1) $f(x) = ax^3 + bx^2 + cx + d$

Nunc eleifend, ex a luctus porttitor, felis ex suscipit tellus, ut sollicitudin sapien purus in libero. Nulla blandit eget urna vel tempus. Praesent fringilla dui sapien, sit amet egestas leo sollicitudin at.

### Multiple Imputation

describe imputation (rubin), describe multiple (bootstrapped) imputation, why it is likely not to work on the given dataset:

> Data from developing countries especially are notoriously incomplete and do not come close to fitting the assumptions of commonly used imputation models [@honaker-TSCS]

show imputation results for bootstrapped imputation and another method.

bootstrapped multiple imputation: observation of one variable is estimated by linear regression from observation of other variables in cross-section. Given dataset is different, values for all our parameters are missing in cross sections containing missing values.

Seasonality of major crops in India:

http://www.gktoday.in/major-crops-of-india/
3 growing seasons (Kharif, Rabi, Zaid)
http://www.yourarticlelibrary.com/notes/notes-on-agricultural-seasons-and-major-crops-in-india/12791/
http://www.arthapedia.in/index.php?title=Cropping_seasons_of_India-_Kharif_%26_Rabi

http://apy.dacnet.nic.in/ has crop production statistics! download manually for full period up to 13-14! full period downloaded

http://lus.dacnet.nic.in/dt_lus.aspx land use statistics up to 14-15

http://www.eaindustry.nic.in/home.asp
retrieve weekly and monthly wholesale price index from selected commodities

data on exports and imports?
http://www.dgciskol.nic.in/data_information.asp
data is priced

FORMS for IMPORT/EXPORT data (ministry of commerce)
http://www.commerce.nic.in/eidb/

fertilizer monitoring system
http://urvarak.co.in/

india population data:
http://www.censusindia.gov.in/2011census/population_enumeration.html
primary census

data from natural horticulture board useful?
http://nhb.gov.in/OnlineClient/MISDailyReport.aspx?enc=3ZOO8K5CzcdC/Yq6HcdIxJ4o5jmAcGG5QGUXX3BlAP4=

check out World Bank data catalog for international prices

Taluka/Tehsil
It is an area of land with a city or town that serves as its administrative centre, with possible additional towns, and usually a number of villages. The terms in India have replaced earlier geographical terms, such as pargana, pergunnah and thannah, used under the Delhi Sultanate and the British Raj.




### Aggregation

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed faucibus pulvinar volutpat. Ut semper fringilla erat non dapibus. Nunc vitae felis eget purus placerat finibus laoreet ut nibh.

### Simulation



## Time Series Forecasting with Machine Learning


## Conclusion

This is the conclusion. Donec pulvinar molestie urna eu faucibus. In tristique ut neque vel eleifend. Morbi ut massa vitae diam gravida iaculis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

