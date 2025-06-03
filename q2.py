import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")
rc = {'font.sans-serif': 'SimHei', 'axes.unicode_minus': False}
sns.set(context="talk", style="ticks", rc=rc)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

order_df = pd.read_excel('附件1 近5年402家供应商的相关数据.xlsx', sheet_name='企业的订货量（m³）')
supply_df = pd.read_excel('附件1 近5年402家供应商的相关数据.xlsx', sheet_name='供应商的供货量（m³）')
predict_order = pd.read_excel("预测订货总量结果.xlsx")
predict_supply = pd.read_excel("供应商供货量预测结果用C代替.xlsx")


predict_order_capacity =