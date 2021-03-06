import os
from FlaskApp import create_app, db
from FlaskApp.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG'))
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command("shell",Shell(make_context=make_shell_context)) 
manager.add_command('db',MigrateCommand) #migration command

@manager.command
def test():
    """Run he unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()#manager has no option like host & debug
    # app.run(host='0.0.0.0', debug=True)