# app/core/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler

def remind_pending_approvals():
    print("Reminder job running")

scheduler = BackgroundScheduler()
scheduler.add_job(remind_pending_approvals, "cron", hour=20)
scheduler.start()
