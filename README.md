# Mall-Customer-Segmentation

This repository showcases an end-to-end data science project focused on customer segmentation. The primary business goal is to move beyond generic marketing by identifying distinct, data-driven customer groups within a mall's clientele based on their annual income and spending habits.

The core of the project is an unsupervised learning model built using K-Means clustering. This algorithm was chosen after a comparative analysis with other methods like DBSCAN, proving to be far more effective for this dataset. The model's success is quantitatively validated by a high Silhouette Score of 0.89, indicating that the discovered segments are dense, distinct, and well-separated.

The analysis successfully revealed five commercially relevant customer personas, providing a clear roadmap for tailored business strategies:

- VIP Customers (High Earners, High Spenders): The most valuable segment, ideal for loyalty programs and premium offers.

- Frugal Spenders (High Earners, Low Spenders): Cautious customers who need targeted promotions to increase spending.

- Reckless Spenders (Low Earners, High Spenders): High-risk, high-reward customers likely influenced by trends.

- Regular Customers (Average Earners, Average Spenders): The stable, core customer base.

- Essential Needs Spenders (Low Earners, Low Spenders): Price-sensitive customers focused on necessities.

To demonstrate a practical application, the project also includes functionality to take the data of a new, unseen customer and instantly classify them into one of these five personas, enabling real-time, personalized marketing efforts.
