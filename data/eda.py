# 2025 - 2026 gold rates 
import yfinance as yf
import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.preprocessing import StandardScaler
from statsmodels.graphics.tsaplots import plot_acf
import statsmodels.api as sm
import warnings

url = "https://raw.githubusercontent.com/JONG1510/FPNA-python/main/data/GC_latest.csv
df = pd.read_csv(url)
