from os import walk
import os 
mypath = "dp3_traces"

traces = next(walk(mypath), (None, None, []))[2]

print(traces)
num1 = 30
num2 = 30


for i in traces:
    if "high" not in i:
        # os.system("./run_champsim.sh bimodal-no-no-no-next_line-lru-1core " + str(num1) + " " + str(num2) + " " + i)
        # os.system("./run_champsim.sh hashed_perceptron-no-no-no-next_line-lru-1core " + str(num1) + " " + str(num2) + " " + i)

        os.system("./run_champsim.sh ltage-no-no-no-next_line-lru-1core " + str(num1) + " " + str(num2) + " " + i)
        print("done for trace" + i)