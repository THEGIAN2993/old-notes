clear all
cls

use "\\studata\Studata\gcrescenzo\Desktop\hw4data.dta"

rename total_output output
rename tot_wage_final wages
rename avg_nfa capital
rename avg_raw_mat materials

gen ln_output = log(output)
gen ln_wages = log(wages)
gen ln_capital = log(capital)
gen ln_materials = log(materials)
gen age2 = age^2

reg ln_output ln_wages ln_capital ln_materials importer rural listed age age2

local b_age  = _b[age]
local b_age2 = _b[age2]

local diff5_10 = (10-5)*`b_age' + (100 - 25)*`b_age2'
local diff50_55 = (55-50)*`b_age' + (3025 - 2500)*`b_age2'

display `diff5_10'
display `diff50_55'

test (ln_wages + ln_capital + ln_materials = 1)

test age age2