import matplotlib.pyplot as plt

# 假设数据是以字典形式存储的
# 结构为：数据集 -> 指标 -> 方法 -> 值
results = {
    'Dataset1': {
        'PSNR': {'Method1': 30, 'Method2': 35, 'Method3': 32},
        'SSIM': {'Method1': 0.9, 'Method2': 0.95, 'Method3': 0.92},
        'Dissipation': {'Method1': 0.1, 'Method2': 0.05, 'Method3': 0.08}
    },
    'Dataset2': {
        'PSNR': {'Method1': 28, 'Method2': 34, 'Method3': 31},
        'SSIM': {'Method1': 0.88, 'Method2': 0.94, 'Method3': 0.91},
        'Dissipation': {'Method1': 0.12, 'Method2': 0.06, 'Method3': 0.09}
    },
    'Dataset3': {
        'PSNR': {'Method1': 29, 'Method2': 33, 'Method3': 30},
        'SSIM': {'Method1': 0.89, 'Method2': 0.93, 'Method3': 0.90},
        'Dissipation': {'Method1': 0.11, 'Method2': 0.07, 'Method3': 0.10}
    }
}

def plot_results_for_dataset(dataset):
    plt.figure(figsize=(15, 5))
    for i, metric in enumerate(results[dataset], 1):
        plt.subplot(1, 3, i)
        methods = results[dataset][metric].keys()
        scores = results[dataset][metric].values()
        plt.bar(methods, scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        plt.title(f'{metric} for {dataset}')
        plt.xlabel('Method')
        plt.ylabel(metric)

    plt.tight_layout()
    plt.show()

# 分别为每个数据集生成图表
for dataset in results.keys():
    plot_results_for_dataset(dataset)
