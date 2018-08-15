# /bin/bash
export PYTHONPATH=
export PATH=~/anaconda3/bin:$PATH

## get this to point to venv for ParlAI
source /home/roboy/workspace/venv_ParlAI/bin/activate

python /home/roboy/workspace/Roboy/src/ParlAI/projects/roboy/ros_integration/gnlp_ros_srv.py
