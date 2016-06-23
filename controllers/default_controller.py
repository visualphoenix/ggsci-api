import os, subprocess, json, logging, re
GGSCI = os.getcwd() + '/test/ggsci'

log = logging.getLogger(__name__)

re_mgr_running = re.compile(r'^Manager is running.*$')

def ggsci(cmd) -> str:
    output = subprocess.run(
        ['echo "' + cmd + '" | ' + GGSCI + " | awk 'NR>10' | sed '$d' | sed '$d' | sed '$d'"],
        shell=True,
        stdout=subprocess.PIPE).stdout.decode("utf-8")
    return output

def manager_post(command) -> str:
    result = command.get('command')
    result = ggsci(result.upper() + ' MANAGER')
    result = [{'response':result}]
    return json.dumps(result)

def manager_childstatus_get() -> str:
    result = ggsci('SEND MANAGER CHILDSTATUS DEBUG')
    return result

def manager_get() -> str:
    raw_result = ggsci('INFO MANAGER').rstrip()
    result = bool(re_mgr_running.match(raw_result))
    result = [{'running':result, 'raw': raw_result}]
    return json.dumps(result)
