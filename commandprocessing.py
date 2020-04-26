from extendedfunc import *
from connectdb import getConnection
from trainmodule import command_train


def execute_command(trig, name):
    db = getConnection()
    cur = db.cursor()
    q = "SELECT command,name_val,type,executor FROM commands WHERE trigg='" + str(trig) + "'" + " && name_val='" + str(
        name) + "'"
    cur.execute(q)
    app = cur.fetchone()
    print(app)
    if app:
        name = str(app[1]) + str(app[2])
        com = app[0]
        executor = app[3]
        return dispatcher[executor](com, name)
    else:
        command_train(trig, name)


dispatcher = {'cmd': cmd}
