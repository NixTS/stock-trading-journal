# **Stock Trading Journal**

Live Website: [Stock Trading Journal - Not Yet Deployed](https://nixts)

The Stock Trading Journal is a Python application designed to help daytraders manage and analyze their stock trading activities. This terminal-based app integrates with Google Sheets, allowing users to input trading data, view their past trades, and access statistics.

![lucid chart](media/readme-images/lucid-chart.jpeg)

## **Project Goals**

The project's primary goal is to maintain a minimalist and straightforward terminal-based design. It prioritizes simplicity and efficiency in user interactions. This design philosophy ensures that users can quickly and intuitively enter their stock trading data without any unnecessary complexity. Input validation mechanisms are implemented to guarantee data accuracy, minimizing errors and ensuring the integrity of the trading records. Unnecessary elements or features that could clutter the interface are intentionally omitted, keeping the user experience focused and efficient. The ultimate aim is to provide traders with a clean, distraction-free tool that simplifies data management, fostering a seamless and hassle-free experience for users.

## **User Goals**

### **First Time Users Goals**

+ As a first time User, I want to easily navigate my Stock Trading Journal.
+ As a first time User, I want to learn the interface very quick.
+ As a first time User, I want to see my past trades.

### **Frequent User Goals**

+ As a frequent User, I want to see todays and all my past trades.
+ As a frequent User, I want to see my trading statistics.
+ As a frequent User, I want to be as efficient as possible when using the app.

### **All User goals**

+ As a User, I want to input stock trading data without the danger of pushing incorrect data.
+ As a User, I want to access this app from anywhere.
+ As a User, I dont want the app to use a lot of rescources from my machine.

### **Fulfillment**

The terminal-based app is controlled with direct keyboard input with input validation, no incorrect data can be put in.
> As a first time User, I want to easily navigate my Stock Trading Journal.
> As a first time User, I want to learn the interface very quick.

A user-configurable feature has been added, enabling users to specify a desired number of past trades for viewing.
> As a first time User, I want to see my past trades.

A feature has been added, allowing Users to see all their past trades.
> As a frequent User, I want to see todays and all my past trades.

The option to display a certain number of trades, todays or all time trades statistic is implemented. Showing number of trades, profit/loss, number of long/short, number of winning/losing trades and win-loss-ratio.
> As a frequent User, I want to see my trading statistics.

The Terminal based app with direct keyboard input and input validation allows lightning fast controll over the app without having the danger of putting in incorrect data.
> As a frequent User, I want to be as efficient as possible when using the app.

> As a User, I want to input stock trading data without the danger of pushing incorrect data.

This app is deployed to a cloud based service and connected to a google sheet on the google cloud, allowing access from anywhere in the world.
> As a User, I want to access this app from anywhere.

As a cloud-based application featuring a terminal interface, this software 
uses minimal resource, making it exceptionally resource-efficient.
> As a User, I dont want the app to use a lot of rescources from my machine.

## **Structure**

### **Navigation**

+ After starting the Stock Trading Journal the user will be greeted by a short welcoming message.
+ Options are given to navigate the app by pressing buttons on the keyboard with direct input.
+ Each option has a short description of where this navigation leads to.
+ An option to close the application by pressing the ESC button in the main menues.

**Starting Screen**  
![starting screen](media/readme-images/starting-screen.jpg)

**Input Stock Trading Data**  
![input stock trading data](media/readme-images/trading-journal-input.jpg)

**Display Journal Entries**  
![display journal entries](media/readme-images/trading-journal.jpg)

**Display Trading Statistics**  
![display trading statistics](media/readme-images/trading-statistics.jpg)

### **Trading Journal Input**

+ Inputs can only be made with the keyboard.
+ Input is validated wherever an input can be made, so that it fits the google sheet.
+ Input validation testing can be seen in the testing section.

**Input for dates**
+ First, the user can decide if they want to push the current date or enter a date manually.

![enter date option](media/readme-images/trading-journal-input.jpg)

+ When users opt to manually enter a date, the program enforces a specific date format to ensure data consistency. Upon successful entry in the correct format, a green-colored confirmation message will be displayed, indicating that the date input was successful.

![date correct input](media/readme-images/enter-date-correct-input.jpg)

**Input for Stock Ticker Symbol**
+ Input only accepts 1 - 4  letters.
+ Letters will be converted to uppercase after input.  

![stock ticker correct input](media/readme-images/stock-ticker-correct-input.jpg)

**Input for Shares Amount**
+ Input only accepts positive numbers.  

![shares amount correct input](media/readme-images/shares-amount-correct-input.jpg)

**Input Prices**
+ Input only accepts numbers with 2 decimals for both entry and exit price.  

![entry and exit price correct input](media/readme-images/entry-exit-price-correct-input.jpg)

## **Features**

### **Existing Features**

**Program**
+ Terminal based for quick responsiveness
+ Sorting google sheet after every entry if an older date was pushed
+ A close program function when pressing ESC while in main menu
+ Asks to return to menu on button press '1'

**Inputs**
+ This program uses direct keyboard input for quick navigation
+ Data input to fill out a google sheet
+ Input validation for input fields to minimize incorrect data entries

**Display past Trades**
+ Three options to choose from when displaying past trades
+ Specify a number of past trades to show in a table
+ Show todays trades in a table
+ Show all trades in a table

**Get Statistics**
+ Three options to choose from when displaying past trades statistics
+ Specify a number of past trades statistics
+ Show todays trades statistic
+ Show all trades statistics
+ Shows number of trades, profit/loss, number of long/short, number of winning/losing trades and win-loss-ratio.

### **Features left to implement**

+ API connection to brokerage software to automate the process of entering trades.
> Given the relatively low daily trade volume, implementing automation would not yield a cost-effective solution for this scenario.

+ A delete past trades function will be implemented in the future.
> Due to very strict input validation, a delete past trades is not necessary yet.

## **Technologies**

### **Language**

+ [Python](https://www.python.org/)
    - Main programming language used in this project

### **Libraries**

+ [Colorama](https://pypi.org/project/colorama/)
    - Used to color terminal text
+ [Keyboard](https://pypi.org/project/keyboard/)
    - Used for direct keyboard inputs
+ [Tabulate](https://pypi.org/project/tabulate/)
    - Used to create tables in the terminal
+ [GSpread](https://docs.gspread.org/en/v5.10.0/)
    - Python API for google sheets
+ [Time](https://docs.python.org/3/library/time.html)
    - Provides various time-related functions
+ [Datetime](https://docs.python.org/3/library/datetime.html)
    - Used to manipulate times and dates
+ [RegEx](https://docs.python.org/3/library/re.html)
    - Used to further controle and validate inputs

### **Tools**

+ [PIP](https://pypi.org/project/pip/)
    - Package installer for Python
+ [Git](https://git-scm.com/)
    - Version control system
+ [GitHub](https://github.com/)
    - Used to store and manage code
+ [Heroku](https://dashboard.heroku.com/)
    - Used to deploy the project
+ [Visual Studio Code](https://code.visualstudio.com/)
    - Open source code editor
+ [Lucid Charts](https://www.lucidchart.com/pages/)
    - Data and chart visualization
+ [CI Python Linter](https://pep8ci.herokuapp.com)
    - Code quality advisor software for error and mistakes detection

## **Testing**

+ Thorough testing procedures were applied throughout the development lifecycle of the Stock Trading Journal program.
+ Following the implementation of each function, a testing regimen was conducted to assess not only its functionality but also its seamless integration with other program functions.
+ Testing criteria included evaluating the visibility and comprehensibility of user interfaces as well as the overall design integrity of the application.

### **Input Validation**

In this program, there are various methods for inputting data:

+ Using keyboard keys for menu navigation.
+ Utilizing keyboard keys in scenarios where there are two or more predefined options.
+ Entering numerical values or sequences of letters when creating journal entries.

Each input field within the program is safeguarded against errors through one of the following mechanisms:

+ **Restricting input to specific keys, ensuring only permissible characters are accepted.**

![screenshow allowed keys](media/readme-images/allowed_keys.jpg)

![example allowed keys](media/readme-images/example-allowed_keys.jpg)

Imposing constraints on the accepted input format, such as letters, numbers, numbers with decimals, specific dates like today or past dates thereby preventing invalid data entry.

+ **Validate Dates**  
![validate date](media/readme-images/validate-date.jpg)

+ **Validate Letters**  
![validate ticker](media/readme-images/validate-ticker.jpg)

+ **Validate Numbers**  
![validate numbers](media/readme-images/validate-number.jpg)

+ **Validate Numbers with Decimals**  
![validate numbers with decimals](media/readme-images/validate-number-decimal.jpg)

### **Input Validation Testing**

### **Functionality**

### **Unresolved Errors, Issues and Bugs**

## **Deployment**

### **Project Creation**

The project was started by navigating to the [template --- link needed](https://github) and clicking 'Use this template'. Under Repository name I input woodworking-club and checked the 'Include all branches' checkbox. I then navigated to the new [repository --- link needed](). I then clicked the Code drop down and selected HTTPS and copied the link to the clipboard.

Opening [Codeanywhere](https://app.codeanywhere.com/) and clicking 'New Workspace', I then pasted the [repository link --- link needed](https://github) into the URL field and clicked 'Create'. The following commands were used throughout the project:

+ git add filename - This command was used to add files to the staging area before committing.
+ git commit -m *commit message explaining the updates* - This command was used to commit changes to the local repository.
+ git push - This command is used to push all committed changes to the GitHub repository.

### **Run Locally**

### **Deployment**

## **Credits**

### **Content**

### **Acknowledgements**
