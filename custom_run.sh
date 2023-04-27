if [ "$1" -eq 1 ]; then 
./build_champsim.sh ppm_rewritten no no no next_line lru 1      
./run_champsim.sh ppm_ ppm_rewritten-no-no-no-next_line-lru-1core 1 10 cadical-low1186B.champsimtrace.xz  
./build_champsim.sh ppm_rewritten no no no next_line lru 1      
./run_champsim.sh ppm_ ppm_rewritten-no-no-no-next_line-lru-1core 1 10 cadical-low1186B.champsimtrace.xz             
gdb ./bin/ppm_classes-no-no-no-next_line-lru-1core
elif [ "$2" -eq 2 ]; then 
