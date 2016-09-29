### Notes

1. Unbalanced dataset
  * If a particular datapoint/column is a boolean value, then check what are the percentages of Trues and Falses.
  * If the percentages are far off then the dataset needs to be made balanced first before training certain models.
  * DOUBT: Not sure exactly how to onvert the balanced dataset to its original unbalanced nature after we have finished using the balanced dataset.
  * DOUBT: Not sure how to relate unbalanced-ness to discreet and continuous data.


1. Dealing with NaN or -999 or Unknown
  1. Could replace the NaN with the most common occuring value for that datapoint. This could make sense if the NaN distribution is purely random and if the most common occuring value for the datapoint occurs a lot more frequently than other values.
