import subprocess
import cmd

def run_command(command, args):
    subprocess.run([command, *args])
    return 0

class MyShell(cmd.Cmd):
    intro = 'Type help to list all command\n'
    prompt = '(my_pseudo_shell) '

    def do_exit(self, line):
        return True
        
    def default(self, line):
        command, *args = line.split()
        try:
            return run_command(command, args)
        except:
            print("incorrect input")
            exit(84)

if __name__ == '__main__':
    MyShell().cmdloop()
