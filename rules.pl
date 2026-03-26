% Rules for loyalty strategy based on Churn Score (Input from ML) and Customer Type (Input from User)

% ----------------------------------------------------------------------
% Churn Score Classification (Using ML output for Prolog input)
% ----------------------------------------------------------------------
% churn_risk(Category) - facts asserted by Python
:- dynamic churn_risk/1.

% ----------------------------------------------------------------------
% Loyalty Strategy Rules (Module 3)
% ----------------------------------------------------------------------

% Strategy 1: High Churn Risk + New Customer => Aggressive Retention
loyalty_strategy(aggressive_retention, "Offer a massive discount (50% for 6 months) immediately. Assign a dedicated account manager.") :-
    churn_risk(high),
    customer_type(new).

% Strategy 2: High Churn Risk + Existing Customer => Service Recovery
loyalty_strategy(service_recovery, "Conduct a detailed service audit and provide a personalized resolution plan to address past issues.") :-
    churn_risk(high),
    customer_type(existing).

% Strategy 3: Medium Churn Risk + New Customer => Proactive Engagement
loyalty_strategy(proactive_engagement, "Send a thank-you gift and a personalized check-in call to ensure satisfaction during the trial period.") :-
    churn_risk(medium),
    customer_type(new).

% Strategy 4: Medium Churn Risk + Existing Customer => Value Reinforcement
loyalty_strategy(value_reinforcement, "Offer an upsell to a better-value plan or add-on feature at a nominal cost to increase commitment.") :-
    churn_risk(medium),
    customer_type(existing).

% Strategy 5: Low Churn Risk => Maintain Status Quo
loyalty_strategy(maintain_status_quo, "No immediate action required. Continue standard quarterly check-ins and newsletter subscription.") :-
    churn_risk(low).

% Strategy 6: Default/Unknown
loyalty_strategy(review_manually, "Data is inconclusive or a key customer type is missing. Requires manual review by a senior manager.") :-
    \+ churn_risk(_). % If no churn risk fact is present

% The main query predicate
get_strategy(Strategy, Recommendation) :-
    loyalty_strategy(Strategy, Recommendation).
