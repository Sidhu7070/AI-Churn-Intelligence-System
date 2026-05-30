# ==================================
# CHURN REASON ANALYSIS
# ==================================

def churn_reason(customer):

    reasons = []

    if customer["MonthlyCharges"] > 80:

        reasons.append(
            "High Monthly Charges"
        )

    if customer["tenure"] < 12:

        reasons.append(
            "Low Customer Tenure"
        )

    if customer["TotalCharges"] < 500:

        reasons.append(
            "Low Service Usage"
        )

    if customer["Contract"] == 0:

        reasons.append(
            "Month-to-Month Contract"
        )

    if len(reasons) == 0:

        reasons.append(
            "No Significant Churn Indicators"
        )

    return reasons


# ==================================
# RETENTION STRATEGIES
# ==================================

def retention_strategy(customer):

    strategies = []

    if customer["MonthlyCharges"] > 80:

        strategies.append(
            "Offer Discount Plan"
        )

    if customer["tenure"] < 12:

        strategies.append(
            "Provide Loyalty Rewards"
        )

    if customer["Contract"] == 0:

        strategies.append(
            "Promote Annual Contract"
        )

    if customer["TotalCharges"] < 500:

        strategies.append(
            "Offer Premium Trial Service"
        )

    if len(strategies) == 0:

        strategies.append(
            "Customer Appears Stable"
        )

    return strategies