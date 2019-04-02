from datetime import datetime
from social_network.helper import get_week_day_name,short_name


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text =text
        self.timestamp = timestamp
        

    def set_user(self, user):
        self.user = user
    

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(Post).__init__(text)
        self.timestamp = timestamp 
        self.user = None
            
    def __str__(self):
        
        timestamp = datetime.timestamp(self.timestamp) # convert timestamp to integer before passing below
        dt_object = datetime.fromtimestamp(timestamp)
        week_name=get_week_day_name(dt_object.weekday())
        m=dt_object.month
        s_m =short_name(m)
        d = dt_object.day
        y = dt_object.year
        # '@{} {}: "{}"{}{}, {} {}, {}'.format(self.user.first_name,self.user.last_name,self.text,"\n\t",week_name,s_m,d,y)
        return '@{} {}: "{}"{}{}, {} {}, {}'.format(self.user.first_name,self.user.last_name,self.text,"\n\t",week_name,s_m,d,y)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(Post).__init__(text)
        self.image_url = image_url
        self.timestamp = timestamp

    def __str__(self):
        
        timestamp = datetime.timestamp(self.timestamp) # convert timestamp to integer before passing below
        dt_object = datetime.fromtimestamp(timestamp)
        week_name=get_week_day_name(dt_object.weekday())
        m=dt_object.month
        s_m =short_name(m)
        d = dt_object.day
        y = dt_object.year
        
        return '@{} {}: "{}"{}{}{}{}, {} {}, {}'.format(self.user.first_name,self.user.last_name,self.text,"\n\t",self.image_url,"\n\t",week_name,s_m,d,y)

                                                        
class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(Post).__init__(text)
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def __str__(self):
        
        timestamp = datetime.timestamp(self.timestamp) # convert timestamp to integer before passing below
        dt_object = datetime.fromtimestamp(timestamp)
        week_name=get_week_day_name(dt_object.weekday())
        m=dt_object.month
        s_m =short_name(m)
        d = dt_object.day
        y = dt_object.year
        
        return '@{} Checked In: "{}"{}{}, {}{}{}, {} {}, {}'.format(self.user.first_name,self.text,"\n\t",self.latitude,self.longitude,"\n\t",week_name,s_m,d,y)
    
