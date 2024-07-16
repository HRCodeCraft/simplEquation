import matplotlib.pyplot as plt

def create_visualizations():
    data_input = input("Enter space-separated values for the data: ")
    data = [float(value) for value in data_input.split()]
    bins = int(input("Enter the number of bins: "))

    x_input = input("Enter space-separated values for X: ")
    x = [float(value) for value in x_input.split()]

    y_input = input("Enter space-separated values for Y: ")
    y = [float(value) for value in y_input.split()]

    labels_input = input("Enter space-separated labels: ")
    labels = labels_input.split()

    legend_input = input("Enter space-separated legends: ")
    legend = legend_input.split()

    # Histogram
    plt.hist(data, bins=bins, rwidth=1)
    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.legend(legend)
    plt.show()

    # Scatter Plot
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(legend)
    plt.show()

    # Bar Graph
    plt.bar(x, y)
    plt.title("Bar Graph")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.legend(legend)
    plt.show()

    # Line Plot
    plt.plot(x, y)
    plt.title("Line Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(legend)
    plt.show()

    # Pie Chart
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.legend(legend)
    plt.show()

    # Box Plot
    plt.boxplot(data)
    plt.title("Box Plot")
    plt.xlabel("Data")
    plt.ylabel("Values")
    plt.legend(legend)
    plt.show()

# Call the function to create visualizations
create_visualizations()
