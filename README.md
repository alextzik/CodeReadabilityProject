# Measuring Readability with Clustering Methods

### Abstract
  This assignment is about measuring the readability of code methods that are included in highly ranked projects on  Github. It aims at providing a way of measuring the readability, given certain characteristics and violations of each method. The approach taken is that of clustering. This study shows that dimensionality reduction can be applied to the original data and leads to the creation of easily distinguishable clusters that represent different levels of readability and simplicity. A couple of dimensionality reduction techniques were applied before clustering, and the results show that the best method is ICA.

### Keywords
mining software repositories; code readability; dimensionality reduction; clustering

## Introduction
This assignment concerns the design of a system for measuring code readability. Code readability is an essential characteristic of any project that includes code development. In today’s world, code development has grown to become even more important than in the past. The ever-growing need for software has resulted in an acceleration of the rate at which code is developed. This has led to the development of difficult-to-understand code that is thus more susceptible to errors.

In the last few years there have been significant efforts in providing a quantitative meaning to readability in general, namely [1], [2], [3] and [4]. Despite these efforts, there is still no clear definition of the term readability. However, it is a popular opinion that readability is a crucial aspect of any software project. In many cases, other individuals might need to understand one’s code (code reusability) or the developer might need to remember his own code in order to move forward.

As far as code understanding in this paper is concerned, a distinction can be made between simplicity and readability. We consider readability as the ease of reading and understanding the code, whereas simplicity as the measure of how easy the logic of the algorithm is to follow.

Both simplicity and readability are a way of ranking the quality of each piece of code. They provide a way of assessing the finished product and giving insight into its quality, maintainability, efficiency and reliability. The measures of readability and simplicity must align with the human perception of these terms, which is also highly subjective. Therefore, even though we think the estimation of these metrics is a regression problem by its nature, we tackle it as a clustering problem.

Taking the above into consideration, a new method of measuring readability and simplicity would be extremely valued in the field of Software Development, if it in fact provides accurate and insightful results for each piece of code.

## Research Overview
The dataset used contains numeric features for approximately 1 million methods from the most famous Github repositories. The data is gathered in files which correspond to repositories, and for each method in every repository we have 78 metrics such as Duplication Metrics, Complexity Metrics and Coupling Metrics and 193 PMDs (features found with the Programming Mistake Detector) such as Brace Rules, Design Rules and Controversial Rules. 

We consider the Metrics’ category to be highly correlated to the human perception of simplicity, because they are more related to the flow of the algorithm rather than the actual language that is used. On the contrary, PMDs are directly associated with the Java language, and how clear a piece of code is, given that we have understood the algorithm’s function.

The primary goal of this assignment is to create lower dimensional spaces for readability and simplicity, where there is a clear separation of the data in different categories based on these metrics.

## System Design
A. *System Overview*<br/>
  + The structure of the system created is a simple one. The features from the dataset are extracted at first. Then preprocessing follows in order to simplify and make the data easy to visualize. In the end clustering is performed. Traditional clustering and division of the low-dimensional data in a scale due to its linearity can be applied.

