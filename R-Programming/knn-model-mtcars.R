library(tidyverse)
library(caret)
library(mlbench)

# Split Data
split_data <- function(data){
  set.seed(42)
  n <- nrow(data)
  id <- sample(1:n, size=0.7*n)
  train_df <- data[id, ]
  test_df <- data[-id, ]
  return(list(train=train_df, test=test_df))
}
prep_df <- split_data(mtcars)

# k-fold cross validation
ctrl <- trainControl(method="boot",
                     number=25)
set.seed(42)
knn <- train(mpg~.,
             data=prep_df$train,
             method="knn",
             metric="RMSE",
             trControl=ctrl)





