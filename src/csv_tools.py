# import pandas as pd
# baseline_df = pd.read_csv("data/construction_topic_baselines_numeric.csv")
# monthly_df = pd.read_csv("data/construction_monthly_metrics_numeric.csv")


# def get_baseline_data(topic):

#     result = baseline_df[
#         baseline_df["topic_name"].str.contains(topic, case=False, na=False)
#     ]

#     return result.to_dict(orient="records")


# # def get_monthly_data(topic, month):

# #     result = monthly_df[
# #         (monthly_df["topic_name"].str.contains(topic, case=False, na=False)) &
# #         (monthly_df["period_month"] == month)
# #     ]

# #     return result.to_dict(orient="records")


# def get_monthly_data(topic, month):

#     result = monthly_df[
#         (monthly_df["topic_name"].str.contains(topic, case=False, na=False)) &
#         (monthly_df["period_month"] == month)
#     ]

#     return result.to_dict(orient="records")

import pandas as pd

baseline_df = pd.read_csv("data/construction_topic_baselines_numeric.csv")
monthly_df = pd.read_csv("data/construction_monthly_metrics_numeric.csv")


def get_baseline_data(topic):

    if topic is None:
        return []

    result = baseline_df[
        baseline_df["topic_name"].astype(str).str.contains(topic, case=False, na=False)
    ]

    return result.to_dict(orient="records")


def get_monthly_data(topic, month):

    if topic is None or month is None:
        return []

    result = monthly_df[
        (monthly_df["topic_name"].astype(str).str.contains(topic, case=False, na=False)) &
        (monthly_df["period_month"].astype(str) == month)
    ]

    return result.to_dict(orient="records")
