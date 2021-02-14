library(tidyverse)

ulta <- read.csv('ulta-cleaned.csv')

ulta = ulta %>%
  mutate(X = NULL, brand = as.factor(brand)) # X: 'row index' column

ggplot(data = ulta) + geom_histogram(aes(x = avg_review), binwidth=.1) 
# add line with median 


top_prods = ulta %>%
  filter(avg_review > mean(avg_review), n_review > mean(n_review))

top_prods %>%
  arrange(avg_review, ascending=FALSE)


summary(top_prods)

by_brand = ulta %>%
  group_by(brand) %>% 
  summarise(num_prods = n(), avg_rating = mean(avg_review)) %>%
  filter(num_prods > 2)

ggplot(data = by_brand) + geom_bar(aes(x = brand, y = avg_rating), stat='identity')

