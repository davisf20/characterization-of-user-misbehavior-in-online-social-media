# Characterization of user misbehavior in online social media
SUPSI - Bachelor's thesis - 2023

Author: Davis Fusco

## Introduction
This project focuses on the exploratory analysis of user data on social media platforms to uncover insights into behavioral dynamics. Leveraging the K-Means clustering algorithm, we categorize users based on their interactions, highlighting distinct behavioral patterns. Additionally, a Random Forest classifier enriched with Explainable AI techniques, specifically SHAP (SHapley Additive exPlanations), provides detailed information on feature importance within each cluster. These methods not only enhance technical validity but also make findings accessible for practical implementation. The results offer valuable indications for crafting effective intervention strategies to improve ethics and correctness in social media interactions.

## Dataset Description

The dataset for this thesis project comprises two main components: a primary set of 4 million tweets and a supplementary dataset with information on over 1 million users. The focus is on characterizing online user behavior related to the early stages of the COVID-19 pandemic, specifically in the Italian language.

### Tweet Dataset
- **Size:** 4 million records
- **Columns:** 36 variables
  - *Key Features:* Includes tweet content, tweet type (original, retweet, quoted text), hashtags, embedded links, and user mentions.
  - *Context:* Captures user sentiments and interactions during the initial phase of the COVID-19 pandemic.

### User Dataset
- **Size:** Over 1 million records
- **Columns:** 15 variables
  - *Key Features:* Encompasses user details such as follower/following counts, likes, and other metrics related to user activity.
  - *Context:* Provides comprehensive information about users engaged in the analyzed tweets.

### Initial Exploratory Analysis
The initial exploration involves understanding the dynamics of user interactions in the context of the COVID-19 pandemic. The analysis performed on this dataset include:
1. **Sentiment and Emotional Dynamics:**
   - Identification and categorization of sentiments, focusing on negative emotions, toxic behaviors, and potential misinformation.
   
2. **User Clustering with K-Means:**
   - Utilization of the K-Means clustering algorithm to categorize users into distinct groups based on their behavioral patterns.
   - Highlighting specific characteristics of each user cluster.

3. **User Characterization with Random Forest:**
   - Implementation of a Random Forest classifier to further characterize users within the identified clusters.
   - Enrichment of the classifier with Explainable AI techniques, specifically using SHAP (SHapley Additive exPlanations).
   - Extraction of detailed information on the importance of individual features in different user clusters.

4. **Technical Validity and Practical Applicability:**
   - Strengthening the technical validity of conclusions through algorithmic approaches.
   - Enhancing accessibility and applicability of interpretations in real-world scenarios.

5. **Insights for Intervention Strategies:**
   - Derivation of valuable insights for the implementation of effective intervention strategies on social media platforms.
   - Focus on improving ethics and correctness in online interactions.

This dataset serves as the foundation for the subsequent analysis conducted in the thesis, providing valuable insights into online user behavior during a critical period of global concern.

## Prerequisites

### General
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [tqdm](https://tqdm.github.io/)

### Text Analysis
- [sentita](https://github.com/NicGian/SentITA)
- [feel_it](https://pypi.org/project/feel_it/)
- [detoxify](https://pypi.org/project/detoxify/)

### Cluster Analysis
- [scikit-learn](https://scikit-learn.org/stable/)
- [hdbscan](https://hdbscan.readthedocs.io/en/latest/)
- [shap](https://shap.readthedocs.io/en/latest/)

### Cluster Characterization
- [scipy](https://www.scipy.org/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [nltk](https://www.nltk.org/)
- [spacy](https://spacy.io/)
- [urlexpander](https://pypi.org/project/urlexpander/)
- [bertopic](https://github.com/MaartenGr/BERTopic)
- [umap](https://umap-learn.readthedocs.io/en/latest/)

### Data Visualization
- [plotly](https://plotly.com/)
- [seaborn](https://seaborn.pydata.org/)
- [wordcloud](https://pypi.org/project/wordcloud/)

Make sure to have the listed libraries installed in your Python environment before running the project. You can install them using the following command:

```bash
pip install -r requirements.txt
```
Note: It's recommended to set up a virtual environment using tools like [virtualenv](https://virtualenv.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/) for better project isolation.
