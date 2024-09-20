class StatLogger():

    def __init__(self, path):
        self.path = path
        return self

    def log_data(self, data_point, count, avg, max_value, min_value, sum_value,
                 sum_square, variance):
        """
        Logs the data statistics in a single line format.

        Parameters:
            data_point (float): The current data point.
            count (int): The total count of data points.
            avg (float): The running average of the data points.
            max_value (float): The running maximum value.
            min_value (float): The running minimum value.
            sum_value (float): The running sum of the data points.
            sum_square (float): The running sum of the squares of data points.
            variance (float): The running variance of the data points.
        """

        log_message = (
            f"Data Point: {data_point:.2f} || "
            f"Count: {count} || "
            f"Average: {avg:.2f} || "
            f"Max: {max_value:.2f} || "
            f"Min: {min_value:.2f} || "
            f"Sum: {sum_value:.2f} || "
            f"Sum of Squares: {sum_square:.2f} || "
            f"Variance: {variance:.2f}"
        )

        print(log_message)

        if self.path:
            with open(self.path, 'a') as file:
                file.write(log_message + '\n')
