#
# start_serve.sh
# Start vm & flask local server
# Author: Kenta Yamada
#

# Constants
EXEC_SCRIPT_PATH=$(cd $(dirname $0); pwd)
PROJECT_ROOT_PATH=$(pwd | xargs dirname)
FLASK_SERVER_PATH="${PROJECT_ROOT_PATH}/server.py"


function echo_help() {
    HELP_TEXT="
    no options: start vm host machine & local flask server
    -f: start only flask local server
    -h: show help document
    -v: start only vm host machine
    "
    echo "$HELP_TEXT"
}

function run_flask_server() {
    echo "Start local flask server"
    python3 -B $FLASK_SERVER_PATH
}

function run_vm() {
    echo 'Start vm host machine'
    VBoxManage startvm "Ubuntu14.04" -type headless
}

while getopts hfv: OPT
do
    case $OPT in
        "f" ) run_flask_server ;;
        "h" ) echo_help ;;
        "v" ) run_vm ;;
         *  ) run_vm; run_flask_server ;;
    esac
done

echo "completed"
exit 0
