#!/bin/bash

TEST_EPISODES=$1
DQN_PY=/media/cosmin/400eca5a-8ba8-4ce9-a16b-9bd30a6e6ec0/Storage/Masters/1st_Year/1st_Semester/Artificial_Intelligence_of_Biological_Inspiration/DQN-2048/dqn2048.py
CSV_FILE="tests/2048_"$TEST_EPISODES"episodes.csv"

echo "episode,max_tile,episode_reward,episode_steps" > $CSV_FILE
python $DQN_PY $TEST_EPISODES 2>&1 > tmp_file

awk '/<TEST>:/ {print $2}' tmp_file >> $CSV_FILE