"""
Bug Class
"""

class Bug:

    """Primary defect object definition"""

    def __init__(self,priority,birthdate):
        self.priority = priority
        self.birthdate = birthdate

    def age(self, date):
        """returns age of defect"""

        if date < self.birthdate:
            raise ValueError("Date must be greater or equal to bug birthdate in age() method.")
        return date-self.birthdate

    def null(self):
        """Test method"""
        return 0
