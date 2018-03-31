# AAPL-Stock-Prices-Analysis
Tool to extract analytics about Apple stock prices - and to be able to predict future values using machine learning model(s).

**Installing**
```python
pip install -r requirements.txt
```
**Preprocessing**

*Running:*
```python
python "Data Preprocessing/Analytics Generation.py"
```
It will give you some additional columns needed for extracting analytics.
```python
python "Data Preprocessing/Preprocessing.py"
```
It gives you analytics table.

**Visualization**

Jupiter notebook includes visualizations and histograms of data.

***Machine Learning Models***

* **1. Predicting Same Day Strategy:**

    * **Features used:**

        * Same Day Delta; because it's the only moderator for it

    * **Models used:**

        * Gaussian Naive Bayes (GNB) classifier.

    * **Accuracy:**
         * 0.963942307692 Accuracy


* **2. Predicting Next Close Strategy:**

    * **Features used:**

        * 'Open', 'Close', "High", "Low", "Adj Close", "Volume" and "privious_day_next_close_delta"

    * **Models used:**

        * Gaussian Naive Bayes (GNB) classifier.

    * **Accuracy:**
         * 0.514423076923 Accuracy
