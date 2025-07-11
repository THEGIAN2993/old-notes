clear all

use "/Users/gcrescenzo/Documents/School/LaTeX Documents/Class Notes/Spring 2025/Applied Econometrics/Econ Final Project/Final Paper/final_project.dta"
drop if county == "Tehama County"


*generating basic variables
egen sd_temp = sd(temp) ,by (county)
gen temp_dev = (temp - temp_hist)/(sd_temp)

egen sd_precip = sd(precip) ,by (county)
gen precip_dev = (precip - precip_hist)/(sd_precip)

gen county_density = county_pop/sq_mi

gen ln_median_house = ln(median_house)

*gen temp_precip_dev = temp_dev * precip_dev

*reg median_house temp_dev precip_dev county_pop county_density

reg ln_median_house temp_dev precip_dev county_pop county_density

*reg median_house temp_dev precip_dev temp_precip_dev county_pop county_density

*reg ln_median_house temp_dev precip_dev temp_precip_dev county_pop county_density

*reg ln_median_house temp_dev precip_dev county_pop county_density, cluster(county)

*reg ln_median_house temp_dev precip_dev county_pop county_density i.year, cluster(county)

areg ln_median_house temp_dev precip_dev county_pop county_density i.year, absorb(county) cluster(county)
