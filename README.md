# Netflix Content Analysis

This project provides a comprehensive analysis of Netflix content based on various metrics. It uses data visualizations to explore trends in content over time, genres, ratings, and other characteristics, offering valuable insights into Netflix's content strategy.

## Features

- **Content Growth Over Time**: Visualize how the number of movies and TV shows has grown on Netflix over the years.
- **Genre Distribution**: Explore the distribution of content across different genres.
- **Content Ratings**: Analyze the ratings of content available on Netflix.
- **User Interaction**: Interactive web app to explore various Netflix content statistics.

## Installation

To run the app locally or deploy it to Render, follow these steps.

### 1. Clone the Repository

```bash
git clone https://github.com/axvampire/netflix-content-analysis.git
cd netflix-content-analysis
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
If you're using venv to manage environments:
```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies
Make sure you have the required dependencies installed:
```
pip install -r requirements.txt
```
### 4. Running Locally
To run the app locally:
```
streamlit run app.py
```
This will start a local server, and you can open the app in your browser at http://localhost:8501.

## Technologies Used
Python: The primary programming language.

Streamlit: For building interactive web apps.

Pandas: For data manipulation and analysis.

Matplotlib/Seaborn: For data visualization.

NumPy: For numerical computing.

## Usage
The app allows users to:

Visualize the growth of content on Netflix over time.

Filter content by genre and explore genre distribution.

Analyze content ratings and viewership trends.

Interact with visualizations to gain insights into Netflix's content library.

## Deployment
This app is deployed on Render.com. You can view the live app here:

https://netflix-content-analysis.onrender.com

## Troubleshooting
If you run into issues while deploying or running the app, check the following:

Make sure all dependencies are installed from requirements.txt.

Ensure that your Python version is compatible with the packages.

If you encounter any issues related to Streamlit or Matplotlib, check the app logs for more details.

## Contributing
Contributions are welcome! If you'd like to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes and commit them (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a new Pull Request.
