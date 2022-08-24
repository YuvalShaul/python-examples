import enckey


def enc_init():
    commands = {'info': enc_info, 'load':enc_load, 'newkey':enc_newkey, 'save':enc_save}
    return commands


def main_cli():
    commands = enc_init()
    cli_end = False
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] == 'done':
            cli_end = True
        if  cmd:
            commands[cmd[0]](cmd[1:])


def enc_save():
    print('_____save')

def enc_load():
    print('_____load')

def enc_newkey():
    the_new_key = enckey.new_enc_key()
    print('_____newkey')

def enc_info():
    print('____info')

main_cli()