import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def normal_distribution(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def app():
    st.title("Normal Distribution Visualizer")
    mu = st.slider("Mean (μ)", min_value=-10.0, max_value=10.0, value=0.0, step=0.01)
    sigma = st.slider("Standard Deviation (σ)", min_value=0.1, max_value=10.0, value=1.0, step=0.01)

    x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 1000)

    y = normal_distribution(x, mu, sigma)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"Normal Distribution (μ={mu:.1f}, σ={sigma:.1f})")
    plt.axhline(y = 0, color = 'r', linestyle = '-')
    plt.axvline(x = 0, color = 'r', linestyle = '-')
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.title("Normal Distribution")
    plt.legend()
    plt.grid(True)

    st.pyplot(plt)

if __name__ == "__main__":
    app()
