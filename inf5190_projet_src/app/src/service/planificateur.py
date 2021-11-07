from apscheduler.schedulers.background import BackgroundScheduler


class Planificateur:

    def __init__(self):
        self.frequence = 123
        self.chose = BackgroundScheduler()
