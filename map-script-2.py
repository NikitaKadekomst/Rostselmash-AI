import numpy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt


# y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative",
#           "positive", "positive", "positive", "positive", "negative", "negative", "negative"]
#
# # prediction scores
# pred_scores = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3, 0.7, 0.5, 0.8, 0.2, 0.3, 0.35]
#
# # thresholds
# thresholds = numpy.arange(start=0.2, stop=0.7, step=0.05)
#
# threshold = 0.5
# y_pred = ["positive" if score >= threshold else "negative" for score in pred_scores]


def precision_recall_curve(y_true, pred_scores, thresholds):
    precisions = []
    recalls = []

    for threshold in thresholds:
        y_pred = ["positive" if score >= threshold else "negative" for score in pred_scores]

        precision = precision_score(y_true=y_true, y_pred=y_pred, pos_label="positive")
        recall = recall_score(y_true=y_true, y_pred=y_pred, pos_label="positive")

        precisions.append(precision)
        recalls.append(recall)

    return precisions, recalls


y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative",
          "positive", "positive", "positive", "positive", "negative", "negative", "negative"]
pred_scores = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3, 0.7, 0.5, 0.8, 0.2, 0.3, 0.35]
thresholds = numpy.arange(start=0.2, stop=0.7, step=0.05)
precisions, recalls = precision_recall_curve(y_true=y_true, pred_scores=pred_scores, thresholds=thresholds)


# Визуализация кривой precision-recall
def plot_pr_curve(recs, precs):
    plt.plot(recs, precs, linewidth=4, color="red")
    plt.xlabel("Recall", fontsize=12, fontweight='bold')
    plt.ylabel("Precision", fontsize=12, fontweight='bold')
    plt.title("Precision-Recall Curve", fontsize=15, fontweight="bold")
    plt.show()


plot_pr_curve(recalls, precisions)

precisions.append(1)
recalls.append(0)

precisions = numpy.array(precisions)
recalls = numpy.array(recalls)

AP = numpy.sum((recalls[:-1] - recalls[1:]) * precisions[:-1])
print(AP)