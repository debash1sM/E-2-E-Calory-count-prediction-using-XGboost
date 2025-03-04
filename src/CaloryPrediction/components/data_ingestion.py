
class DataIngestion():
    def __init__(self):
        pass

    
    def initiate_data_ingestion(self, data_path):
        """
        This function initiates the data ingestion process
        """
        self.data_path = data_path
        self.data = pd.read_csv(data_path)
        return self.data
    