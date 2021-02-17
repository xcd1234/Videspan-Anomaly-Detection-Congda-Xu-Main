# Videspan-Anomaly-Detection-Congda-Xu-Main


For my anomaly detection algorithm, the major machine learning package I used is the KNN detector in the PyOD library. The KNN method computes the distance of an observation, to other observations as the Euclidean distance. And based on this, the anomaly points can be identified as those which are isolated from other neighbors with larger distance.

For our dataset, because it is recorded in a time series order, I therefore believe I should identify anomalies in "periods" instead of at one time identify for the entire dataset. So my algorithm will identify anomaly points for multiple fixed-length time periods of data using KNN in PyOD and then identify those data who got labeld as anomaly at least once in these periods as the final anomaly detection result.

There are three hyperparameters that you can tune:   
contamination: the threshold for decision function in KNN  
n_neighbors: the number of neighbors to compare in KNN  
length: the length of the time period for each KNN model  

The confusion matrix for the six datasets are:

<pre>
exchange-2_cpc_results:  
         Predicted
         0      1    
True 0 | 1494 | 129 |    
     1 | 0    | 1   |    
</pre>

<pre>
exchange-3_cpc_results:  
         Predicted  
         0      1  
True 0 | 1423 | 112 |  
     1 | 1    | 2   |  
</pre>

<pre>
exchange-4_cpc_results:  
         Predicted  
         0      1  
True 0 | 1483 | 157 |  
     1 | 0    | 3   |  
</pre>

<pre>
exchange-2_cpm_results:  
         Predicted  
         0      1  
True 0 | 1468 | 154 |  
     1 | 0    | 2   |  
</pre>

<pre>
exchange-3_cpm_results:  
         Predicted  
         0      1  
True 0 | 1418 | 119 |  
     1 | 0    | 1   |  

</pre>

<pre>
exchange-4_cpm_results:  
         Predicted  
         0      1  
True 0 | 1461 | 178 |  
     1 | 1    | 3   |  
</pre>
