# CountryStatViz
## Video Demo: [CountryStatViz Tutorial](https://youtu.be/JBiPteFPD18)
# Country Stats Visualizer with Python

### This project is a Country Stat Visualizer and it takes user input to display Country Stats in the form of a Bar graph.

## What is the purpose of this project?
1. It can be used to analyze country data.
2. It can be used to automate data summary and data visualization.
3. It can compare multiple countries in terms of different stats such as:
* GDP
* Population
* Internet penetration
* Sex-ratio

## Requirements
* An internet connection
* Python interpreter
* Python Libraries
    * requests library: `pip install requests`
    * matplotlib library: `pip install matplotlib`
* VSCode is preferred but you can use any IDE of your choice (_optional_)
    * [Jupyter notebook extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) you can also install from VS Code by going to the extensions tab.
    * [PDF reader extension](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf)

*  ### API Website
    The website used here is [API Ninja](https://api-ninjas.com/), They have APIs for everything. To get a free API key login into their website Sign up and request an API key by [clicking here](https://api-ninjas.com/profile) after Signing up.


## How to use it?
**First, you'd want to install all pip installable libraries.** (_this project is 100% written in Python_) You can do so by the following commands in the IDE or folder you want to use **CountryStatViz**:

`pip install matplotlib`

`pip install requests`

**I used VS code to make this program. I suggest you too use VS Code to do so. However, other IDEs are fine if you follow along with the instructions given below.**

To run the file in the folder you want to use and get the output, run these bash commands by creating a new bash terminal.

For Example, I am creating a folder named project and a Python file called project.py, You can modify this according to your needs.

`cd project`

`python project.py`





### Here's a demo!
Demo is here: [CountryStatViz Tutorial](https://youtu.be/JBiPteFPD18) You can subscribe to my [Youtube channel](https://www.youtube.com/channel/UCRkH_ce70jVKd8gbbxL_Trg) to see it. My videos aren't the best but I will make this demo as great as possible!


## How it works in `project.py`
 `get_country()`  asks the user number of countries. If an integer isn't given we raise valueError. Else we continue with looping over the input statement asking the user a country. Eg: if the user enters the number of countries as 4 then. we loop an input statement 4 times. If any country is invalid we raise a ValueError. If all countries are valid. We index the country through the API and pick out GDP, sex ratio, internet penetration and population and append it to 4 different lists.

 __________

  `plot_gdp()` and other subsequent functions use matplotlib.pyplot more specifically the use of `plt.subplot`, `figures` and `axes`. Figures are the number of files made and axes are the number of graphs in the file. We used `ax.bar(list_countries, list_gdps, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])` to set x-axis and y-axis data, along with a color attribute to set colors to bars. I set x-axis, y-axis names and gave them a title. Also, I saved it as a pdf. This function takes `list_countries` and `list_gdps`

 __________

 `plot_pops()` it takes paramters of `list_countries` and `list_pops`. I have set the x-axis, y-axis and other details such as title and subplotting. I provided x and y-axis details along with the color of bars with `ax1.bar(list_countries, list_pops, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])`, also I saved it as a pdf.

__________

 `plot_internet()` it takes parameters of `list_countries` and `list_internet`. I set its title, x-axis and y-axis name. I provided x and y-axis data with `ax2.bar(list_countries, list_internet, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])`, also saved it as a pdf.

__________

  `plot_sex_ratio()` it takes parameters of `list_countries` and `list_sex_ratio`. I set its title, x-axis and y-axis name. I provided x and y-axis data with `ax3.bar(list_countries, list_sex_ratio, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])`, also saved it as a pdf.


__________
 I called these functions in the `main()` and gave them parameters from `get_country()` where all the data is returned.


## Limitations and in _CountryStatViz_ and Solutions
Limitation 1: If many countries are given Long country names such as: _The Democratic Republic of Congo (DRC)_ might merge with the country's names on the x-axis.

Solution: I suggest using fewer than 8 countries and not using too many long-named countries.

Limitation 2: I haven't written a textual description of the countries' populations.

Solution: That will come in version 1.1.0, **Coming Soon!**. Meanwhile, my program is returning a list with GDP, Population, Sex ratio and Internet penetration for each country entered by the user.

Limitation 3: The Data isn't the most up to date.

Solution: I will have to use another API for this. The data isn't the most up-to-date. This will most likely be fixed in version 1.1.0, **Coming Soon!**


### Credits!
* _This project was done for CS50P, Harvard University's Course for Python._
* I thank David J Malan for his wonderful teaching.

_Made by Saksham Garv a young Python programmer._
















