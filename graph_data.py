import matplotlib.pyplot as plt


def plot(ranges, percentages, step):
    """Uses precompiled matplotlib modules to plot the data onto a graph"""
    plt.plot(ranges, percentages)
    plt.ylabel("Prime Probability")
    plt.xlabel("Number")
    plt.title(f"Prime Density Graph [Step {step}]")
    plt.show()
