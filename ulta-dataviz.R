library(tidyverse)

ulta <- read.csv('ulta-cleaned.csv')
ulta = ulta %>%
  mutate(X = NULL, brand = as.factor(brand)) # X: 'row index' column

# price histogram
ggplot(data = ulta) + geom_histogram(aes(x = price_usd), binwidth = 5, fill='blue', color='black') +
  geom_vline(aes(xintercept = median(price_usd)), colour='red') +
  ggtitle('Histogram of Moisturizer by Price') +
  ggsave("price_hist.png")

top_prods = ulta %>% 
  filter(n_review > 100) %>%
  mutate('price_range' = ifelse(price_usd < 25, "Under $25", 
                                ifelse(price_usd < 50, "$25-50", "$50 or more" ))) %>%
  mutate(price_range = as.factor(price_range))


summary(top_prods)

review_plot = ggplot(data = top_prods) + 
  geom_boxplot(aes(x = price_range, y = avg_review, fill = price_range))

review_plot +
  scale_x_discrete(limits = c("Under $25", "$25-50", "$50 or more")) +
  ggtitle("Boxplot of Average Review, by Price Range") +
  ggsave("review-boxplot.png")

ggplot(data = top_prods) + 
  geom_density(aes(x = avg_review, color = price_range)) +
  ggtitle("Density of Average Product Review, by Price Range") + 
  ggsave("review-density.png")

top_prods = top_prods %>% 
  mutate('bestseller_status' = avg_review*n_review)


top_prods %>% slice_max(bestseller_status, n=10) %>% 
  ggplot() + geom_col(aes(x = product, y = n_review, fill = brand)) +
  ggtitle("Number of Reviews of Bestsellers") +
  theme(axis.text.x = element_blank()) +
  ggsave("bar-bestsellerreviews.png")


top_prods %>% slice_max(bestseller_status, n=10) %>% 
  ggplot() + geom_col(aes(x = product, y = price_usd, fill = brand)) +
  ggtitle("Cost of Bestsellers") + 
  theme(axis.text.x = element_blank()) +
  ggsave("bar-bestseller-cost.png")