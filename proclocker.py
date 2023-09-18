import sys
import psutil

def check_arguments():
    if len(sys.argv) <= 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(1)

def get_targets():
    targets = sys.argv[1:]
    corrected_targets = []

    for target in targets:
        if not target.endswith('.exe'):
            corrected_targets.append(target + '.exe')
        else:
            corrected_targets.append(target)

    return corrected_targets

def lock(targets):
    for target in targets:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            try:
                if proc.info['name'].lower() == target.lower():
                    print(f'Terminando proceso: {proc.info["name"]}, PID: {proc.info["pid"]}')
                    psutil.Process(proc.info['pid']).terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

if __name__ == '__main__':
    check_arguments()
    targets = get_targets()
    
    lock(targets)
