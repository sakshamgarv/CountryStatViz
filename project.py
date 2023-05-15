
import requests
import matplotlib.pyplot as plt

def get_country():
    try:
        numcountry = int(input("Input number of countries you want to compare:"))
    except ValueError:
        print("Give an Integer")

    list_countries = []
    list_gdps = []
    list_sex_ratio = []
    list_pops = []
    list_internet = []

    for i in range(1, numcountry+1):
        get_country = input("Enter the name of the country:")
        answer = requests.get("https://api.api-ninjas.com/v1/country?name="+get_country, headers ={"X-Api-Key": "PUT YOUR API KEY, YOU CAN GET API KEY FROM README.md"})
        if answer.ok == True and len(answer.json())>0:
            list_countries.append(get_country)

            list_pops.append(answer.json()[0]["population"]/1000)
            list_gdps.append(answer.json()[0]["gdp"]/1000)
            list_sex_ratio.append(answer.json()[0]["sex_ratio"])
            list_internet.append(answer.json()[0]["internet_users"])
        else:
            raise ValueError("Invalid Country")

    return list_countries, list_pops, list_gdps, list_sex_ratio, list_internet

def plot_gdp(list_countries, list_gdps):
    try:
        fig, ax = plt.subplots()
        ax.bar(list_countries, list_gdps, color=['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])
        ax.set_title("GDP of country (in Millions)" )
        ax.set_xlabel("Countries")
        ax.set_ylabel("GDP, millions")
        plt.savefig("GDP.pdf")
    except:
        raise ValueError("An Error occurred")
    else:
        return True

def plot_pops(list_countries, list_pops):
    try:
        fig, ax1 = plt.subplots()
        ax1.bar(list_countries, list_pops, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])
        ax1.set_title("Population of countries (IN MILLIONS)")
        ax1.set_xlabel("Countries")
        ax1.set_ylabel("Population in millions")
        plt.savefig("Population.pdf")
    except:
        raise ValueError("An Error occurred")
    return True

def plot_internet(list_countries, list_internet):
    try:
        fig, ax2 = plt.subplots()
        ax2.bar(list_countries, list_internet, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'] )
        ax2.set_title("Percentage of Country's Population which has access to Internet")
        ax2.set_xlabel("Countries")
        ax2.set_ylabel("Percentage of population (out of 100%)")
        plt.savefig("Internet.pdf")
    except:
        raise ValueError("An Error occurred")
    else:
        return True


def plot_sex_ratio(list_countries, list_sex_ratio):
    try:
        fig, ax3 = plt.subplots()
        ax3.bar(list_countries, list_sex_ratio, color = ['indigo', 'red', 'green', 'blue', 'cyan', 'violet'])
        ax3.set_title("Sex ratio number of males in ratio of 100")
        ax3.set_xlabel("Countries")
        ax3.set_ylabel("Sex ratio")
        plt.savefig("ratio.pdf")
    except:
        raise ValueError("An error occured")
    else:
        return True


def main():
    values = get_country()
    print(values)
    plot_gdp(values[0], values[2])
    plot_pops(values[0], values[1])
    plot_sex_ratio(values[0],values[3])
    plot_internet(values[0],values[4])

if __name__ == "__main__":
    main()
