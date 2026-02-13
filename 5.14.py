from datetime import datetime
import time
class Scheduler:
    obj = None 
    notifications = []
    def __new__(cls):
        if cls.obj:
            return cls.obj 
        cls.obj = super().__new__(cls)
        return cls.obj

    def schedule(self, id, user_id, message, send_at, priority):
        notification = {'id': id, 'user_id': user_id, 'message': message, 'send_at': send_at, 'priority': priotity}
        Scheduler.notifications.append(notification)

    def run_pending(self):
        for notificate in Scheduler.notifications:
            ts = datetime.strptime(notificate['send_at'], '%Y-%m-%dT%H:%M:%S').timestamp()
            if ts  <= time.time():
                print(f'INFO: Sending notification to user_id="{notificate["user_id"]}": "{notificate["message"]}"')

        
        

s = Scheduler()
s.schedule(1, 'a1b2-c3d4', '...', '2025-10-26T10:00:00', 'high')
s.run_pending()