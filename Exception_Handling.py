class NoFile(Exception):
    def __init__(self):
        self.message = ('CSV File not found')
        super().__init__(self.message)

class NoRecord(Exception):
    def __init__(self):
        self.message = ('No record found')
        super().__init__(self.message)

class SaveFile(Exception):
    def __init__(self):
        self.message = ('File Not Saved')
        super().__init__(self.message)