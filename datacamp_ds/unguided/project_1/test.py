import unittest
from project__1.data import CustomerAnalytics
import pandas as pd
import numpy as np


class TestCustomerAnalytics(unittest.TestCase):
    def setUp(self):
        self.customeranalytics = CustomerAnalytics()

    def test_wrangle(self):
        # Checks if self.wrangle returns a dataframe
        self.assertIsInstance(self.customeranalytics.wrangle(
        ), pd.DataFrame, 'This is not a DataFrame')
        # checks if number of column matches specification
        self.assertEqual(self.customeranalytics.wrangle(
        ).shape[1], 14, 'No columns is not correct')
        # checks if student_id and training_hours are int32
        self.assertTrue((np.int32 in list(self.customeranalytics.wrangle()[
                        ['student_id', 'training_hours']].dtypes)), 'student_id and training_hours are not int32')
        # checks if job_change and city_development_index are float16
        self.assertTrue((np.float16 in list(self.customeranalytics.wrangle()
                                            [['job_change', 'city_development_index']].dtypes)), 'job_change and city_development_index are not float16')
        # checks if all other columns are categories
        self.assertTrue(all(self.customeranalytics.wrangle().drop(columns=[
                        'job_change', 'student_id', 'training_hours', 'city_development_index']) == 'category'), 'All other columns are not categories')

    def test_barplot(self):
        pass
