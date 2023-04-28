import os
import re
import click
import json
import logging

logger = logging.getLogger()


def find_cfile(file_name, cwd):
    if file_name in os.listdir('.'):
        return os.path.join(cwd, file_name)
    return None


@click.command()
@click.argument('_command')
def crun(_command):

    # find CFILE.json in dir
    cwd = os.getcwd()
    cfile = find_cfile('CFILE.json', cwd)
    if not cfile:
        logger.error("CFILE not found !")
        return 


    # Read the Cfile
    with open(cfile) as f:
        cfile_contents = f.read()

    c_dict = json.loads(cfile_contents)

    # find command
    try:
        command = c_dict[_command]
    except KeyError:
        logger.error("command not found!")
        return 

    # triger command
    if isinstance(command, list):
        for cmd in command:
            os.system(cmd)
        return
    os.system(command)
    
if __name__ == '__main__':
    crun()
