import matplotlib.pyplot as plt
import numpy as np

from os import walk
import os  

# phase1 = "phase_1"
# phase2 = "phase_2"
# phase3 = "phase_3"
# fin = "results_30M"

# phase_1 = next(walk(phase1), (None, None, []))[2]
# phase_2 = next(walk(phase2), (None, None, []))[2]
# phase_3 = next(walk(phase3), (None, None, []))[2]
# final = next(walk(fin), (None, None, []))[2]

# a_1_pred = {}
# a_2_pred = {}
# a_3_pred = {}

# for i in phase_1:
#     if "high" not in i:
        # f_1 = open("phase_1/" + i, "r")
        # start = i.split("ltage")
        # end = start[1]
        # start = start[0]
        # # f_2 = open("phase_1/" + start + "ltage" + end, "r")
        # f_3 = open("results_30M/" + start + "ltage" + end, "r")
        # l_1 = f_1.readlines()
        # # l_2 = f_2.readlines()
        # l_3 = f_3.readlines()
        # a_1 = {}
        # # a_2 = {}
        # a_3 = {}
        # for k in l_1:
        #     try : 
        #         n = int(k.split("\n")[0])
        #         if n not in a_1:
        #             a_1[n] = 1
        #         else:
        #             a_1[n] += 1
        #     except Exception as e : 
        #         if "CPU 0 Branch Prediction Accuracy:" in k:
        #             a_1_pred[i] = k

        # for k in l_3:
        #     try : 
        #         n = int(k.split("\n")[0])
        #         if n not in a_3:
        #             a_3[n] = 1
        #         else:
        #             a_3[n] += 1
        #     except Exception as e : 
        #         if "CPU 0 Branch Prediction Accuracy:" in k:
        #             a_3_pred[i] = k

        # # for k in l_3:
        # #     try : 
        # #         n = int(k.split("\n")[0])
        # #         if n not in a_1:
        # #             a_1[n] = 1
        # #         else:
        # #             a_1[n] += 1
        # #     except Exception as e : 
        # #         if "CPU 0 Branch Prediction Accuracy:" in k:
        # #             a_1_pred[i] = k

        # print(i)
        # print(a_1)
        # # print(a_3)

# print(a_1_pred)
# print(a_2_pred)
# print(a_3_pred)

# cadical-med-30K-831B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 4544467, 4: 1650501, 2: 673948, 7: 72999, 5: 462665, 6: 232849, 12: 332562, 8: 34324, 9: 24841, 11: 47920, 10: 53285, 3: 754983, 1: 149960}
# cadical-med-30K-1246B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 4294094, 2: 1037882, 4: 1685744, 6: 224681, 5: 475675, 9: 14457, 8: 35135, 10: 88229, 7: 77760, 11: 48034, 12: 353021, 3: 732281, 1: 40307}
# kissat-mab-hywalk-low-30K-299B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 4464843, 6: 254205, 2: 575950, 7: 83233, 5: 386333, 8: 44282, 12: 673997, 4: 1830865, 9: 32649, 11: 103659, 10: 59873, 3: 477947, 1: 12945}
# cadical-med-30K-137B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 6065002, 8: 125198, 2: 407642, 6: 804432, 12: 624029, 7: 320162, 4: 3329929, 10: 150342, 5: 1458115, 11: 181959, 3: 460708, 9: 119414, 1: 18276}
# cadical-med-30K-109B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {4: 1398388, 0: 4748588, 6: 308681, 2: 568914, 5: 605106, 7: 68685, 8: 104208, 12: 233020, 9: 13994, 11: 39386, 10: 30224, 3: 679987, 1: 67039}
# cadical-low-60K-1186B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 3538284, 5: 480104, 2: 635334, 6: 584131, 4: 1970305, 7: 217439, 8: 103129, 12: 1502429, 11: 222151, 9: 54674, 10: 121558, 3: 400230, 1: 25400}
# cadical-med-30K-267B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 4695916, 8: 36846, 2: 665399, 6: 264264, 10: 27909, 4: 1571945, 5: 553216, 7: 69638, 12: 213247, 9: 11189, 11: 53319, 3: 701350, 1: 114217}
# cadical-med-30K-1463B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt
# {0: 4312050, 2: 752779, 4: 1916494, 7: 93058, 8: 32671, 12: 332934, 5: 471923, 6: 251325, 9: 11241, 10: 26256, 11: 50917, 3: 768281, 1: 41960}

# phase1 = {'cadical-med-30K-831B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.4315% MPKI: 14.486 Average ROB Occupancy at Mispredict: 48.6628\n', 'cadical-med-30K-1246B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.4265% MPKI: 14.5734 Average ROB Occupancy at Mispredict: 50.6328\n', 'kissat-mab-hywalk-low-30K-299B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 93.3418% MPKI: 9.95913 Average ROB Occupancy at Mispredict: 34.3812\n', 'cadical-med-30K-137B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 95.4399% MPKI: 10.6733 Average ROB Occupancy at Mispredict: 26.4395\n', 'cadical-med-30K-109B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 92.2837% MPKI: 11.3896 Average ROB Occupancy at Mispredict: 55.3767\n', 'cadical-low-60K-1186B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 95.2662% MPKI: 7.7872 Average ROB Occupancy at Mispredict: 70.6649\n', 'cadical-med-30K-267B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.6618% MPKI: 14.0254 Average ROB Occupancy at Mispredict: 48.4777\n', 'cadical-med-30K-1463B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.4375% MPKI: 14.4463 Average ROB Occupancy at Mispredict: 49.3912\n'}

# # phase2 = {'cadical-med-30K-831B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.8834% MPKI: 13.8019 Average ROB Occupancy at Mispredict: 50.4398\n', 'cadical-med-30K-1246B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.9161% MPKI: 13.8281 Average ROB Occupancy at Mispredict: 52.673\n', 'kissat-mab-hywalk-low-30K-299B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 93.7835% MPKI: 9.29833 Average ROB Occupancy at Mispredict: 36.3005\n', 'cadical-med-30K-137B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 96.8884% MPKI: 7.28297 Average ROB Occupancy at Mispredict: 29.7889\n', 'cadical-med-30K-109B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 92.6991% MPKI: 10.7764 Average ROB Occupancy at Mispredict: 58.2338\n', 'cadical-low-60K-1186B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 95.3182% MPKI: 7.70163 Average ROB Occupancy at Mispredict: 71.363\n', 'cadical-med-30K-267B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 91.0939% MPKI: 13.3764 Average ROB Occupancy at Mispredict: 50.4312\n', 'cadical-med-30K-1463B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.9388% MPKI: 13.689 Average ROB Occupancy at Mispredict: 51.5601\n'}
# # final = {'cadical-med-30K-831B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.9655% MPKI: 13.6776 Average ROB Occupancy at Mispredict: 51.2059\n', 'cadical-med-30K-1246B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 91.0018% MPKI: 13.6976 Average ROB Occupancy at Mispredict: 53.7031\n', 'kissat-mab-hywalk-low-30K-299B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 93.9051% MPKI: 9.11653 Average ROB Occupancy at Mispredict: 37.1686\n', 'cadical-med-30K-137B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 96.9897% MPKI: 7.0459 Average ROB Occupancy at Mispredict: 27.6205\n', 'cadical-med-30K-109B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 92.8554% MPKI: 10.5457 Average ROB Occupancy at Mispredict: 59.3472\n', 'cadical-low-60K-1186B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 95.3099% MPKI: 7.71517 Average ROB Occupancy at Mispredict: 73.1976\n', 'cadical-med-30K-267B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 91.2175% MPKI: 13.1908 Average ROB Occupancy at Mispredict: 51.174\n', 'cadical-med-30K-1463B.champsimtrace.xz-ltage-no-no-no-next_line-lru-1core.txt': 'CPU 0 Branch Prediction Accuracy: 90.9874% MPKI: 13.6155 Average ROB Occupancy at Mispredict: 52.3001\n'}

# phase1_final = {}
# # final_final = {}

# for i in phase1:
#     phase1_final[i.split(".champsim")[0]] = {"Acc":phase1[i].split("CPU 0 Branch Prediction Accuracy: ")[1].split("% MPKI")[0], "MPKI":phase1[i].split("MPKI: ")[1].split(" Average")[0]}
# #     final_final[i.split(".champsim")[0]] = {"Acc":final[i].split("CPU 0 Branch Prediction Accuracy: ")[1].split("% MPKI")[0], "MPKI":final[i].split("MPKI: ")[1].split(" Average")[0]}

# print(phase1_final)
# print(final_final)
phase1_final = {'cadical-med-30K-831B': {'Acc': '90.4315', 'MPKI': '14.486'}, 'cadical-med-30K-1246B': {'Acc': '90.4265', 'MPKI': '14.5734'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '93.3418', 'MPKI': '9.95913'}, 'cadical-med-30K-137B': {'Acc': '95.4399', 'MPKI': '10.6733'}, 'cadical-med-30K-109B': {'Acc': '92.2837', 'MPKI': '11.3896'}, 'cadical-low-60K-1186B': {'Acc': '95.2662', 'MPKI': '7.7872'}, 'cadical-med-30K-267B': {'Acc': '90.6618', 'MPKI': '14.0254'}, 'cadical-med-30K-1463B': {'Acc': '90.4375', 'MPKI': '14.4463'}}
phase2_final = {'cadical-med-30K-831B': {'Acc': '90.8834', 'MPKI': '13.8019'}, 'cadical-med-30K-1246B': {'Acc': '90.9161', 'MPKI': '13.8281'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '93.7835', 'MPKI': '9.29833'}, 'cadical-med-30K-137B': {'Acc': '96.8884', 'MPKI': '7.28297'}, 'cadical-med-30K-109B': {'Acc': '92.6991', 'MPKI': '10.7764'}, 'cadical-low-60K-1186B': {'Acc': '95.3182', 'MPKI': '7.70163'}, 'cadical-med-30K-267B': {'Acc': '91.0939', 'MPKI': '13.3764'}, 'cadical-med-30K-1463B': {'Acc': '90.9388', 'MPKI': '13.689'}}
final_final = {'cadical-med-30K-831B': {'Acc': '90.9655', 'MPKI': '13.6776'}, 'cadical-med-30K-1246B': {'Acc': '91.0018', 'MPKI': '13.6976'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '93.9051', 'MPKI': '9.11653'}, 'cadical-med-30K-137B': {'Acc': '96.9897', 'MPKI': '7.0459'}, 'cadical-med-30K-109B': {'Acc': '92.8554', 'MPKI': '10.5457'}, 'cadical-low-60K-1186B': {'Acc': '95.3099', 'MPKI': '7.71517'}, 'cadical-med-30K-267B': {'Acc': '91.2175', 'MPKI': '13.1908'}, 'cadical-med-30K-1463B': {'Acc': '90.9874', 'MPKI': '13.6155'}}

# ltage_phase2 = {'cadical-med-30K-831B': {'Acc': '90.8834', 'MPKI': '13.8019'}, 'cadical-med-30K-1246B': {'Acc': '90.9161', 'MPKI': '13.8281'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '93.7835', 'MPKI': '9.29833'}, 'cadical-med-30K-137B': {'Acc': '96.8884', 'MPKI': '7.28297'}, 'cadical-med-30K-109B': {'Acc': '92.6991', 'MPKI': '10.7764'}, 'cadical-low-60K-1186B': {'Acc': '95.3182', 'MPKI': '7.70163'}, 'cadical-med-30K-267B': {'Acc': '91.0939', 'MPKI': '13.3764'}, 'cadical-med-30K-1463B': {'Acc': '90.9388', 'MPKI': '13.689'}}
# hashed_final = {'cadical-med-30K-831B': {'Acc': '91.8443', 'MPKI': '12.3471'}, 'cadical-med-30K-1246B': {'Acc': '91.8786', 'MPKI': '12.3628'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '94.4396', 'MPKI': '8.31697'}, 'cadical-med-30K-137B': {'Acc': '97.2639', 'MPKI': '6.4041'}, 'cadical-med-30K-109B': {'Acc': '93.5762', 'MPKI': '9.4818'}, 'cadical-low-60K-1186B': {'Acc': '95.9367', 'MPKI': '6.6842'}, 'cadical-med-30K-267B': {'Acc': '92.069', 'MPKI': '11.9119'}, 'cadical-med-30K-1463B': {'Acc': '91.9025', 'MPKI': '12.2332'}}
# bimodal_final = {'cadical-med-30K-831B': {'Acc': '87.515', 'MPKI': '18.9014'}, 'cadical-med-30K-1246B': {'Acc': '87.8124', 'MPKI': '18.5528'}, 'kissat-mab-hywalk-low-30K-299B': {'Acc': '92.3564', 'MPKI': '11.433'}, 'cadical-med-30K-137B': {'Acc': '85.946', 'MPKI': '32.8949'}, 'cadical-med-30K-109B': {'Acc': '87.5437', 'MPKI': '18.3861'}, 'cadical-low-60K-1186B': {'Acc': '94.8292', 'MPKI': '8.50597'}, 'cadical-med-30K-267B': {'Acc': '87.0012', 'MPKI': '19.5235'}, 'cadical-med-30K-1463B': {'Acc': '87.5782', 'MPKI': '18.7659'}}

# ltage_phase1_x = []
# ltage_phase1_acc = []
# ltage_phase1_mpki = []
# hashed_x = []
# hashed_acc = []
# hashed_mpki = []
# bimodal_x = []
# bimodal_acc = []
# bimodal_mpki = []

phase1_x = []
phase1_acc = []
phase1_mpki = []
final_x = []
final_acc = []
final_mpki = []

for i in phase1_final:
    phase1_x.append(i)
    phase1_acc.append(float(phase1_final[i]['Acc']))
    phase1_mpki.append(float(phase1_final[i]['MPKI']))

for i in final_final:
    final_x.append(i)
    final_acc.append(float(final_final[i]['Acc']))
    final_mpki.append(float(final_final[i]['MPKI']))
  
# # plot lines
plt.plot(phase1_x, phase1_mpki, label = "ltage-Basic" )
plt.plot(final_x, final_mpki, label = "ltage-Optimised")
# plt.yticks(np.arange( 84, 100 , 2 ))
plt.yticks(np.arange( 5, 35 , 5 ))
plt.xticks(rotation=90)
plt.tight_layout()
plt.title("MPKI")
plt.legend(loc=2)
# plt.show()
plt.tight_layout()
plt.savefig("phase1-final-mkpi.png")
# plt.show()

