# Category Selection Generator using Stack Overflow Data with Clustering in Python

I am to make an app that generates a category selection of terms related to Python using Web Data using Machine Learning.

## How? and what is that?

When I was at grad school, every time I used search engines for programming queries such as Google, I wish there were some indexes with core description to help me figure out how to find the desired results efficiently. For example, when I was a beginner in Python, I wanted to search how to slice elements in the array of data structure. The fact that I actually didn’t know specific terminology ‘slice’ and ‘element’, I spent quite a time on finding it than it was supposed to be. Of course, most of programmers know those terms already but what if people who are not originally from computer science filed want to get some help with coding but don’t exactly know what to search for. It would be useful if we had an access to a service having a multiple category selection with details, that based on answers and questions by users clustered and classified with categories along with some explanation. Such a service could potentially be useful by cutting searching time short and being focused on the major task.

In order to generate such service, full text of questions and answers from Stack Overflow that are tagged with the python tag will be used with natural language processing and community analysis by clustering a set of answers to questions and generating a list of indexes.

## Data
For my proposal, I use the Stack Overflow data from Kaggle datasets. The dataset contains questions, answers, and tags up to 19 October 2016, where the data size is 700MB in total. In addition to helping its users enhance their work performance, this app may help Stack Overflow maintain the storage of web feed more efficiently by not generating redundant questions.

Full text of questions and answers from Stack Overflow that are tagged with the python tag, useful for natural language processing and community analysis, provided by Stack Overflow on Kaggle Datasets.

## Steps to follow:
Tokenzation and stemmization each user's answer
Transforming the corpus into vector space using tf-idf
Calculating cosine distance between each document as a measure of similarity
Clustering the documents using the k-means algorithm
Using multidimensional scaling to reduce dimensionality within the corpus
Plotting the clustering output using matplotlib and mpld3
Conducting a hierarchical clustering on the corpus using Ward clustering
Collecting questions where each cluster's user ID matches on such questions
Plotting a Ward dendrogram
Topic modeling using Latent Dirichlet Allocation (LDA)
Generating a nested category selection
Wrapping up everything and producing a module (app)

https://category-selection-generator.herokuapp.com/
