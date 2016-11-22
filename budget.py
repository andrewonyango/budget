# -*- coding: utf-8 -*-


class Budget:
    # constraint: 3 ≤ grants.length ≤ 100
    MIN_REQUESTS = 3
    MAX_REQUESTS = 100
    # constraint: 105 ≤ budget ≤ 200
    LOW_BUDGET = 105
    HIGH_BUDGET = 200
    # constraint: 1 ≤ grant ≤ 1000
    LOW_GRANT = 1
    HIGH_GRANT = 1000

    NO_LIMIT = -1

    def __input_is_valid(self, grants, budget):
        """
        returns True if the inputs are within the constraints
        raises ValueError for any constraint violation

        grants: the list of grant requests
        budget: the available budget
        """
        requests = len(grants)

        if requests < self.MIN_REQUESTS or requests > self.MAX_REQUESTS:
            raise ValueError("Number of grants should be between 3 and 100")

        if budget < self.LOW_BUDGET or budget > self.HIGH_BUDGET:
            raise ValueError("Budget should be between 105 and 200")

        for grant in grants:
            if grant < self.LOW_GRANT or grant > self.HIGH_GRANT:
                raise ValueError("Grants should be between 1 and 1000")

        return True

    def awardBudgetCutProblem(self, grants, budget):
        """
        returns -1 (no limit) if the available budget is enough for the grant
        requests.
        returns a cap, otherwise, which higher grant requests are limited to.

        grants: the list of grant requests
        budget: the available budget
        """
        if self.__input_is_valid(grants, budget):
            if sum(grants) <= budget:
                return self.NO_LIMIT

            # the average will be used to draw the line between high and
            # low grant requests
            average_grant = budget / len(grants)

            list_of_high_grants = [g for g in grants if g > average_grant]

            # calculate the sum of below-average grant requests to which we
            # can safely allocate funds without hitting the limit
            below_average_grants = sum(g for g in grants if g <= average_grant)

            # the balance after allocating funds to below-average requests
            balance_after_allocation = budget - below_average_grants

            # return the limit, which is the balance divided by the remaining
            # grant requests (the above-average, or high, requests)
            return balance_after_allocation // len(list_of_high_grants)
