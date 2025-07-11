clear all
cls

use "/Users/gcrescenzo/Documents/School/LaTeX Documents/Class Notes/Spring 2025/Applied Econometrics/Econ Homework 7/hw7d1.dta"

summarize ln_avg_nfa if underbanked==1 & post_treat==0, meanonly
scalar a = r(mean)

summarize ln_avg_nfa if underbanked==1 & post_treat==1, meanonly
scalar b = r(mean)

summarize ln_avg_nfa if underbanked==0 & post_treat==0, meanonly
scalar c = r(mean)

summarize ln_avg_nfa if underbanked==0 & post_treat==1, meanonly
scalar f = r(mean)

scalar did_uncond = (b - a) - (f - c)
display did_uncond

