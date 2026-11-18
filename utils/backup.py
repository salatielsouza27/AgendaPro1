import shutil,datetime
def realizar_backup():
 shutil.copy('database.db',f"backup_{datetime.date.today()}.db")
