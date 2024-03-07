import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import glob

dataframes = []

fbfl_df = pd.read_csv('results_fbfl_mnist.csv', sep=' ')
fbfl_df['Learning type'] = 'Field-based FL'
fbfl_df = fbfl_df[['time', 'Accuracy[mean]', 'Loss[mean]', 'TrainLoss[mean]', 'Learning type']]
fbfl_df = fbfl_df.rename(columns={'time':'Epoch', 'Accuracy[mean]': 'Average validation accuracy', 'Loss[mean]': 'Average validation loss', 'TrainLoss[mean]': 'Average train loss'})
dataframes.append(fbfl_df.iloc[:11])


fl_df = pd.read_csv('results_federated.csv')
fl_df['Learning type'] = 'Federated Learning'
fl_df['Epoch'] = [i for i in range(15)]
dataframes.append(fl_df.iloc[:11])

df_all = pd.concat(dataframes, axis=0)

ax = sns.lineplot(
    data=df_all, x="Epoch", y="Average train loss",
    hue="Learning type",
)

ax.set_xlabel('Epoch', fontsize=18)
ax.set_ylabel('Average train loss', fontsize=18)

plt.savefig('avg_train_loss_mnist2.png', dpi=500)
plt.close()

ax = sns.lineplot(
    data=df_all, x="Epoch", y="Average validation loss",
    hue="Learning type",
)
ax.set_xlabel('Epoch', fontsize=18)
ax.set_ylabel('Average validation loss', fontsize=18)
plt.savefig('avg_validation_loss_mnist2.png', dpi=500)
plt.close()

ax = sns.lineplot(
    data=df_all, x="Epoch", y="Average validation accuracy",
    hue="Learning type",
)
ax.set_xlabel('Epoch', fontsize=18)
ax.set_ylabel('Average validation accuracy', fontsize=18)
plt.savefig('avg_validation_accuracy_mnist2.png', dpi=500)
plt.close()
















