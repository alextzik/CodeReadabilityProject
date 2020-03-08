# Measuring Readability with Clustering Methods

### Abstract
  **This assignment is about measuring the readability of code methods that are included in highly ranked projects on  Github. It aims at providing a way of measuring the readability, given certain characteristics and violations of each method. The approach taken is that of clustering. This study shows that dimensionality reduction can be applied to the original data and leads to the creation of easily distinguishable clusters that represent different levels of readability and simplicity. A couple of dimensionality reduction techniques were applied before clustering, and the results show that the best method is ICA.**

### Keywords
** *mining software repositories; code readability; dimensionality reduction; clustering* **

## Introduction
This assignment concerns the design of a system for measuring code readability. Code readability is an essential characteristic of any project that includes code development. In today’s world, code development has grown to become even more important than in the past. The ever-growing need for software has resulted in an acceleration of the rate at which code is developed. This has led to the development of difficult-to-understand code that is thus more susceptible to errors.

In the last few years there have been significant efforts in providing a quantitative meaning to readability in general, namely [1], [2], [3] and [4]. Despite these efforts, there is still no clear definition of the term readability. However, it is a popular opinion that readability is a crucial aspect of any software project. In many cases, other individuals might need to understand one’s code (code reusability) or the developer might need to remember his own code in order to move forward.

As far as code understanding in this paper is concerned, a distinction can be made between simplicity and readability. We consider readability as the ease of reading and understanding the *code*, whereas simplicity as the measure of how easy the logic of the *algorithm* is to follow.

Both simplicity and readability are a way of ranking the quality of each piece of code. They provide a way of assessing the finished product and giving insight into its quality, maintainability, efficiency and reliability. The measures of readability and simplicity must align with the human perception of these terms, which is also highly subjective. Therefore, even though we think the estimation of these metrics is a regression problem by its nature, we tackle it as a clustering problem.

Taking the above into consideration, a new method of measuring readability and simplicity would be extremely valued in the field of Software Development, if it in fact provides accurate and insightful results for each piece of code.

## Research Overview
The dataset used contains numeric features for approximately 1 million methods from the most famous Github repositories. The data is gathered in files which correspond to repositories, and for each method in every repository we have 78 metrics such as Duplication Metrics, Complexity Metrics and Coupling Metrics and 193 PMDs (features found with the Programming Mistake Detector) such as Brace Rules, Design Rules and Controversial Rules. 

We consider the Metrics’ category to be highly correlated to the human perception of simplicity, because they are more related to the flow of the algorithm rather than the actual language that is used. On the contrary, PMDs are directly associated with the Java language, and how clear a piece of code is, given that we have understood the algorithm’s function.

The primary goal of this assignment is to create lower dimensional spaces for readability and simplicity, where there is a clear separation of the data in different categories based on these metrics.

## System Design
A. *System Overview*<br/>

The structure of the system created is a simple one. The features from the dataset are extracted at first. Then preprocessing follows in order to simplify and make the data easy to visualize. In the end clustering is performed. Traditional clustering and division of the low-dimensional data in a scale due to its linearity can be applied.

B. *Data Preprocessing*<br/>

The large number of objects in the dataset poses a complexity difficulty for the system. Therefore, sampling without substitution is performed to gather approximately 10% of the original data. This quantity of data retains the attributes, characteristics and behaviors of the original data, but also speeds up the application of any algorithm. In addition, any missing values in the dataset were filled in using scikit-learn’s *SimpleImputer* class, followed by scaling the results to ensure a normal distribution. The scaling is necessary to place all features in the same range and to thus avoid having one characteristic impacting the result of clustering the most.

Due to the large number of dimensions in the feature space, using dimensionality reduction techniques appears to be a good solution in order to compress the information given, gain some further insight into the data and reduce the complexity of the application of different algorithms. Dimensionality reduction was applied separately to the Metrics category and to the Violations category of characteristics, as required by the definitions of readability and simplicity used in this paper.

The results gathered show a clearly better performance in separation using Independent Component Analysis (ICA), rather than Principal Components Analysis (PCA), both in the Metrics Dimensionality Reduction and in the Violations Dimensionality Reduction. In Fig. 1 it is evident that the energy of Principal Components scales linearly with the number of components, up until the point where all the dimensions left  correspond to PMDs that have constant values equal to zero. This means that PCA isn’t better than a reordering of the features. On the other hand, the superiority of ICA is due to its tendency to find basis vectors in order to represent the original data as different sub-elements. Therefore, by finding vectors that are independent components of our data, it is easier to end up with a representation that shows clearly separated clusters. ICA is a blind source separation technique. PCA, in the other hand, aims at finding a low-rank representation of the data. In other words, it tries to compress it. This doesn’t always end up with clearly defined clusters in the low-dimension space. In Fig. 3, 4 we can see the 2-dimensional ICA space for Metrics and PMDs.

| ![Fig. 1](/figures/Fig1.png)
|:--:| 
| *Figure 1. Energy of Principal Components of PMDs* |

C. *Model Construction*<br/>

By performing dimensionality reduction in both the Metrics and Violations subspaces, we get the results shown in Fig. 2, 3. It is evident that clear clusters exist in the Metrics case, while there is a linear structure in the case of the Violations.

 It is our belief that the clusters created in the case of the Metrics’ space represent high and low simplicity methods, while the linear structure in the case of the Violations is also a linear scale of readability. This hypothesis is tested as follows. 
 
## Evaluation
A.*Evaluation Methodology*<br/>

From each cluster in the figures, depicted as the blue and orange areas in Fig. 2, 3, samples are taken and their behavior is derived. The mean value for all the characteristics of the samples in each area is calculated and based on these mean values we may conclude if the codes do actually represent methods with similar simplicity and readability properties. The indicative results are shown in Fig. 4, 5.

| ![Fig. 2](/figures/Fig2.png)
|:--:| 
| *Figure 2. Independent Components Representation of Metrics' Feature Space* |

| ![Fig. 3](/figures/Fig3.png)
|:--:| 
| *Figure 3. Independent Components Representation of PMDs' Feature Space* |

From the Metrics’ perspective, it is evident the two clusters shown in Fig. 4 correspond to different types of codes. The codes in Area 1 seem to have higher mean values for the features where higher is better for simplicity. For example, Comment Density (CD) is higher and Clone Logical Line Coverage (CLLC) is lower, for the codes that belong to Area 1. This indicates codes in Area 1 have more comments and less duplicate code than the codes in Area 2, which means they are simpler.

| ![Fig. 4](/figures/Fig4.png)
|:--:| 
| *Figure 4. Comparison of Metrics' Values in the Different Areas of the IC Metrics’ Analysis* |

| ![Fig. 5](/figures/Fig5.png)
|:--:| 
| *Figure 5. Comparison of PMDs' Values in the Different Areas of the IC Analysis of PMDs* |

For PMDs, the lower values indicate higher readability. As we can clearly see in Fig. 4, Area 1 has higher PMD values, in average, for almost all PMD categories. This indicates codes in Area 2 are more readable than codes in Area 1. It is important to note that the two areas of each space mentioned above is independent and doesn’t refer to the same codes.

## Further Works
As a final note, after careful examination of the data, we strongly believe the Metrics’ and PMDs’ dimensionality can be further reduced in a space with good properties regarding readability and simplicity. For this reason, it is proposed to further review more dimensionality reduction techniques and also try the use of a hybrid a model.

The next step to consider is a Neural Network trained on the PMDs, with its first layer representing the new - lower dimension - features. The truth table will be assumed based on this work, and the first layer of the Neural Network will be used as a new feature space, which will hopefully have desired properties.

Although there is no guarantee of success for this method, similar techniques have been used lately in a variety of Machine Learning domains, including word2vec [5].

## Conclusions
Concluding, in this study a clear distinction between simplicity and readability has been made and a simple yet efficient way of measuring these quantities has been derived. Although there is still further research to be done in the validity of the method, the results presented are optimistic. In addition, the low complexity of the method makes it a useful alternative when trying to measure readability and simplicity. 

## References
[1]. H. A. D. P. Posnett Daryl, A Simpler Model of Software Readability, Waikiki, Honolulu, HI, USA: ACM, 2011. <br/>
[2]. W. W. R. Buse Raymond P. L., Learning a Metric for Code Readability, Piscataway, NJ, USA: IEEE Press, 2010.  <br/>
[3]. J. Dorn, A General Software Readability Model.  <br/>
[4].	M. L.-V. D. P. R. O. S. Scalabrinο, Improving code readability models with textual features, 2016.  <br/>
[5].	Mikolov, Tomas & Corrado, G.s & Chen, Kai & Dean, Jeffrey. (2013). Efficient Estimation of Word Representations in Vector Space. 1-12. 

 



