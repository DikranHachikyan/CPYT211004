def new_file():
    print('Create new file')

def open_file():
    print('Open file ...')

def save_file():
    print('Save file ...')

def quit_app():
    print('Quit Editor')
    quit()

if __name__ == '__main__':
    
    actions = {
        'n':new_file,
        'p':open_file,
        's':save_file,
        'q':quit_app
    }
    
    ch = input('Command (n-new, p-open, s-save, q-quit):')

    if ch in actions:
        actions[ch]()
    else:    
        print(f'Unknown command: {ch}')

print('---')