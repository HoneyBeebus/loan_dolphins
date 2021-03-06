# Enhancements to Oportun FAIR Tool 
1. [Background About Oportun](#background-about-oportun)
2. [Problem](#problem)
3. [Objectives](#objectives)
4. [Usage Documentation](#usage-documentation)
## Background About Oportun
Since we opened our doors in 2005, we have worked hard every day to serve the approximately 100 million people in the United States who are typically shut out of the financial mainstream because they don’t have a credit score or have limited credit history. Our mission-based, technology-powered approach is designed to be inclusive, affordable, and empowering. By lending money to hardworking, low-to-moderate-income individuals, we help our customers move forward in their lives, demonstrate their creditworthiness, and establish the credit history they need to access new opportunities. And our model is working. We’ve provided more than 3.8 million affordable small-dollar loans that have saved customers an estimated $1.7 billion in interest and fees compared to alternative lenders, according to a study commissioned by Oportun and conducted by the Financial Health Network, a leading nonprofit authority on consumer financial health. In 2020, we were listed in the top 10 most innovative finance companies by Fast Company . In 2019, our personal loans were named best consumer lending product by FinTech Breakthrough . And in 2018, we were recognized for our role in inventing the future as one of Time magazine’s Genius Companies . At Oportun, we’re building a community of employees, partners, and customers who support each other on the path to new opportunities, because we believe that when we work together, we can make life better. 
## Problem
This project will focus on developing front- and back-end functionality for a quantitative, cybersecurity risk analysis tool. At Oportun, we developed a tool in Excel that allows us to perform quantitative, cybersecurity risk analyses based on the Factor Analysis of Information Risk (FAIR) framework. FAIR enables us to utilize data from a variety of sources to estimate loss frequency and magnitude of loss for specific security risks. The tool currently requires manual data input into an Excel workbook and relies on complex derivation formulas (all built in Excel) to calculate the various FAIR metrics. For this project, we are looking to complete multiple objectives: (1) Build a front-end user interface that communicates with the to-be built back-end and provides a rich interface through which a user may input values and receive analysis output in real-time; and (2) a back-end data storage and analysis solution that receives input from the user, calculates FAIR metrics based on custom-built algorithms, and returns the necessary data to the front end for user consumption. The back-end should also be capable of saving risk analyses for future evaluation. Prior to the project starting, Oportun will provide background on FAIR, a detailed presentation of current FAIR tool capabilities, risk calculation algorithms, and sample data for use during development and testing. The chosen solution set will be included in an Open Source version of the FAIR tool that Oportun anticipates releasing in Q4 2020. 
## Objectives
Please see above for objectives.
Success criteria include the following: 
- Enhanced user experience through simple, elegant, responsive front-end development 
- Algorithm development: consistency with existing Excel algorithms 
- Data storage: ability to store and retrieve cyber risk analyses
## Usage Documentation
### Requirements
- Node.js
- Yarn package manager
- Python 3
- Flask python module
### Commands
The commands below are used to work with the React app, and should be run in the react-app directory.
- `yarn install`:
Installs all node dependencies locally. Use on initial setup, and also whenever a new dependency has been added.
- `yarn start`:
Will start the React development server, which will host the application.
- `yarn flask`:
Will start the Flask backend server, which is required for the page to be functional.
- `yarn start-all`:
A combination of `yarn start` and `yarn flask`, so both run in the same terminal.
- `yarn build`:
Builds the react-app to a static folder "build", which can be served without running the development server.
However, choosing to serve from here will stop proxy requests to the Flask server from working.
You will need to set up hosting such that both the static webpage and the backend are hosted at the same location.
