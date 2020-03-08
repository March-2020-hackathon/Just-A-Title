class User:
    def __init__(self):
        self.preferences = []
        #self.log_in
        #self.password
    def set_preferences(self, preferences):
        if len(self.preferences):
            for i in preferences:
                self.preferences.append(i)
        else:
            self.preferences = preferences
                
            
        
    