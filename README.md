# Amazon-Sales-Analysis
Check my Analysis: [![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1zqvqfEf5n10LtoqM4ILcrHzEhcmPhbCp?usp=sharing)

About Project
This project consists of two data-cleaning stages. The first stage was done in Visual Studio Code, where the data was cleaned, formatted, and stripped of unwanted foreign characters. The output from this stage was saved as “clean_data_amazon.” The second stage was performed in Google Colab to further organize and structure the dataset. Colab was used because the data contains a wide variety of elements that require additional grouping and refinement. The results of these processes are discussed below.

---

#Insight

**A. Product Rating Distribution**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Product_Rating_Distribution.png)

- kewness: The distribution is negatively skewed (left-skewed). This means that the majority of the data (the highest Count/Jumlah) is concentrated on the higher end of the rating scale. The tail of the distribution extends towards the lower ratings.
- Mode (Most Frequent Rating): The most frequently occurring or most numerous product rating (mode) is located approximately between 4.25 and 4.5.
- Data Concentration: The vast majority of products (more than 50% of the total count) have ratings within a narrow range, specifically from about 4.0 to 4.5; The highest count (around 600-650) is found in the bin between ratings 4.0 and 4.5.
- Low Ratings: Very few products receive a rating below 3.5; The lowest observed ratings (around 2.0 to 3.0) have a very small count, almost approaching zero.
**Conclusion**: Overall, this distribution indicates that the product quality is generally perceived as very good by users, with most ratings concentrated at the high end of the scale (4.0 and above). Only a minimal number of products receive low ratings.

**B. Correlation Actual Price vs Discounted Price**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Correlation_Actual_VS_Discounted.png)

- Strong Positive Correlation:There is a strong positive correlation between the Original Price and the Discounted Price. The data points largely follow a straight diagonal line from the bottom left to the top right. This means that the higher a product's Original Price is, the higher its Discounted Price will also be.
- Discount Effect (Regression Line):Because the Discounted Price (Y-axis) is always lower than or equal to the Original Price (X-axis), all points lie below or on the hypothetical line $y=x$ (i.e., the line where Original Price = Discounted Price). The vertical distance between each data point and the $y=x$ line represents the amount of discount given (in monetary value).Price Concentration:The majority of products have prices below Rp80,000 (for both Original and Discounted Prices). The densest cluster of points is found in the price range of Rp0 to Rp40,000.
- Significant Outlier:There is one data point that stands out far in the top right (Original Price around Rp140,000 and Discounted Price around Rp80,000). This point indicates the product with the highest price in the dataset.
**Conclusion**: The discounts given appear to be proportional to the product's price. That is, products with a high original price tend to maintain a high discounted price, and vice versa. There are no very cheap products suddenly becoming very expensive, or very expensive products becoming very cheap (which would form a random pattern).

**C. Actual Price vs Rating**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Actual_vs_Rating.png)

- No Strong Correlation: Generally, there is no strong or clear linear correlation between the Original Price and the product Rating. The data points are widely scattered along the Original Price axis. This confirms the very weak correlation (0.13) observed in the previous heatmap.
- Insight: The product's original price does not appear to be a major determinant of the customer's perceived quality (rating).
- Outlier: There is one data point at the far top right (Original Price around Rp140,000 with a Rating around 4.7). This is the most expensive product in the dataset which also received an excellent rating.
**Conclusion**: This graph shows that while price does not directly predict the product rating, there is a trend that higher-priced products tend to have more consistent ratings and rarely receive very low scores. Lower-priced products show a wider spectrum of ratings.

**D. Top 10 Products**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Top_10_product.png)

**Conclusion**: The most popular items in terms of review volume are AmazonBasics HDMI cables and boAt wired earphones. These simple accessories far outpace the volume of reviews for specific smartphone models, indicating their status as high-turnover, widely purchased goods.

**E. Actual Price vs Discounted_price**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Actual_vs_Discounted.png)

- Heavily Right-Skewed Price Distribution: Both boxplots show that the majority of the price data (the box and the lower whisker) are heavily compressed near zero. This means the median value is significantly lower than the mean (average), and most products are low-cost items; Expensive products are a rare minority (indicated by the outliers).
- Comparison Actual Price vs. Discounted Price: Effective Discounting the box (IQR) and whiskers for discounted_price are visibly shorter and slightly lower than those for actual_price. This visually demonstrates that the discounted price distribution is more compressed and shifted downwards—proving that discounts are effectively applied to the main bulk of the products.
- Outlier Discounting: The highest outlier value for the discounted price (around Rp80,000) is much lower than the actual price (around Rp140,000). This indicates that very substantial discounts (converting a high outlier to a lower outlier) are applied to the most expensive products.
**Market Focus: The dataset is predominantly focused on very low-priced goods.**

**F. Distribution of Discounted Price**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/a1b8dc302d195274097c0b1ebf3e6d032d754d79/Actual_vs_Discount_Before_After.png)

- Extreme Right-Skewed Distribution: Both distributions are highly positively skewed (right-skewed). The vast majority of products, with the highest counts (over 1,000), are concentrated near Rp0 to Rp5,000.
- Distribution Comparison:
1. Shape: Both graphs have an almost identical shape. The peak (mode) of both distributions lies in the first (lowest) price bin.
2. Value Difference: Notice the X-axis scales. The Actual Price distribution reaches up to Rp140,000, while the Discounted Price distribution only reaches up to Rp80,000.
- Effect of Discounting: The difference in the maximum X-axis value shows that discounts successfully "trim" the distribution's long tail. The most expensive products (Rp140,000) are brought down to a lower price point (maximum of Rp80,000) after the discount, consistent with the boxplot findings.
**Conclusion**: The product price structure is highly uneven, with the vast majority of products clustering at very low price points. The implemented discounts succeed in reducing the maximum price and slightly compressing the overall price distribution, but the dataset remains heavily characterized by its focus on low-budget items.

**G. Review Content**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Review_Content.png)

**Conclusion**: This Word Cloud analysis of "Review Content" shows that customer feedback is heavily focused on accessories (like CABLE) and mobile devices (PHONE). The most frequently mentioned concepts driving user satisfaction or dissatisfaction are PRICE, QUALITY, BATTERY, and EASY of use. The overall sentiment is largely positive, indicated by the prominence of words like GOOD and BEST, although some reviews mention minor ISSUE's or PROBLEM's, suggesting that while the majority of customers are satisfied, common small flaws exist in the frequently purchased products.

**H. Heatmap of Correlation Between Variables**

![image alt](https://github.com/nataliareta/Amazon-Sales-Analysis/blob/5c4c44de9ff6bd302be7037363358313a9d87ad1/Heatmap_Correlation_Variables.png)

**Conclusion**: The analysis confirms a near-perfect positive correlation (0.96) between actual_price and discounted_price, meaning expensive products remain expensive even after discounts. The most notable weak relationship is the negative correlation (-0.24) between discounted_price and discount_percentage, suggesting that higher-priced items generally receive a lower percentage discount. Crucially, the rating and rating_count variables show very weak correlations (near zero) with pricing and discounting variables, indicating that customer perception of quality and product popularity are largely independent of the pricing strategy used.

---

**Tools & Technologies**
A. Program and Data Analyze (Python Libraries)
- Pandas & NumPy
- Matplotlib

B. Platform :
- Google Colab
- Vs Code
- Github

**Data Source** : https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset (Kaggle)
