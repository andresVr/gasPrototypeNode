class SensorsRawData:
    def __init__(self, node, mq7, mq135, mq2, date, location):
        self.node = node
        self.mq7 = mq7
        self.mq135 = mq135
        self.mq2 = mq2
        self.date = date
        self.location = location

    def get_node(self):
        return self.node

    def get_mq7(self):
        return self.mq7

    def get_mq135(self):
        return self.mq135

    def get_mq2(self):
        return self.mq2

    def get_location(self):
        return self.location

    def get_date(self):
        return self.date

    def set_node(self, node):
        self.node = node

    def set_mq7(self,mq7):
        self.mq7 = mq7

    def set_mq135(self,mq135):
        self.mq135 = mq135

    def set_mq2(self,mq2):
        self.mq2 = mq2

    def set_date(self,date):
        self.date = date

    def set_location(self, location):
        self.location = location