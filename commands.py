import Admin_shell
from Admin_shell import commands,open_shell

black="$Host.UI.RawUI.BackgroundColor = [ConsoleColor]::Black;$Host.UI.RawUI.ForegroundColor = [ConsoleColor]::DarkGreen;"
homedir="set-location $home\desktop"


def sample_open_shell_call():
    open_shell_call = open_shell()
    open_shell_call.add_command(black)
    open_shell_call.add_command(homedir)
    open_shell_call.add_command("Get-command")
    output = open_shell_call.run_commands()
    if output:
        print(output)

def sample_commands_call():
    action = commands()
    action.add_command(black)
    action.add_command(homedir)
    output = action.run_commands()

    if output:
        print(output)

sample_commands_call()