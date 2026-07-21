class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]

            total_gas += difference
            current_gas += difference

            # Cannot reach the next station
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        # If total gas is negative, no solution exists
        if total_gas < 0:
            return -1

        return start
        