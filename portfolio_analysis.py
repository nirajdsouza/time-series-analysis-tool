import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_portfolio_metrics(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    """
    Calculate portfolio return, volatility, and Sharpe ratio.
    """
    portfolio_return = np.sum(mean_returns * weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return portfolio_return, portfolio_volatility, sharpe_ratio

def efficient_frontier(returns, num_portfolios=10000, risk_free_rate=0.01):
    """
    Generate portfolios and calculate metrics for the efficient frontier.
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)
    results = np.zeros((3, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        portfolio_return, portfolio_volatility, sharpe_ratio = calculate_portfolio_metrics(
            weights, mean_returns, cov_matrix, risk_free_rate
        )
        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = sharpe_ratio
        weights_record.append(weights)

    return results, weights_record

def plot_efficient_frontier(results):
    """
    Plot the efficient frontier.
    """
    plt.figure(figsize=(12, 8))
    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='viridis', marker='o')
    plt.title('Efficient Frontier')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()
