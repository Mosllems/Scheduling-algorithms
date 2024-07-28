def show_app():
    print("Baraname haie Az System Amel:\tFCFS \tSJF \tSRT \tMCPU \tMLFQ \tAsansor \tBankdaran")

applications = show_app()
applications_list =  ["fcfs", "sjf", "srt", "mcpu", "mlfq", "asansor", "bankdaran"]
print("-"*100)

while True:
    entekhab_karbar = input("Lotfan az barname haie bala yeki ra be delkhah entekhab konid va baraie khoroj 'exit' ra vared konid: ")
    entekhab_karbar = entekhab_karbar.lower()
    if entekhab_karbar == "exit":
        break
    elif entekhab_karbar not in applications_list:
        print("Lotfan yeki az gozine haie gofte shode ra vared konid!")
    else:
        if entekhab_karbar == "fcfs":
            print("Shoma barname FCFS ra entekhab kardid!")
            print("-"*100)
            faraiand = []
            while True:
                try:
                    info = []
                    name_faraiand = input("name faraiand ra vared konid va baraie kharej shodan name faraiand ra 'exit' begzarid: ")
                    info.append(name_faraiand)
                    if name_faraiand == "exit":
                        break
                    else:
                        zaman_vorod = int(input("Zaman vorod ra vared konid: "))
                        info.append(zaman_vorod)
                        zaman_enfejar = int(input("Zaman enfejar ra vared konid: "))
                        info.append(zaman_enfejar)
                        info.append(None)
                        info.append(None)
                except ValueError:
                    print("Baiad adad vared konid!")
                faraiand.append(info)    

            len_faraiand = len(faraiand)
            for i in range(0,len_faraiand):
                for j in range(0,len_faraiand-1):
                    if faraiand[j][1] > faraiand[j+1][1]:
                        temp = faraiand[j]
                        faraiand[j] = faraiand[j+1]
                        faraiand[j+1] = temp

            waiting_time = []
            zaman = faraiand[0][1]
            for i in faraiand:
                k = zaman - i[1]
                if k < 0 :
                    zaman = 0
                waiting_time.append(k)
                zaman += i[2]

            completion_spot = []
            response_time = []
            s1 = faraiand[0][1]
            for i in faraiand:
                m = s1 + i [2]
                completion_spot.append(m)
                s1 = m

            onsor_dovom_har_list = []
            for i in faraiand:
                onsor_dovom_har_list.append(i[2])

            for i,j in zip(completion_spot,onsor_dovom_har_list):
                result = i - j 
                response_time.append(result)

            for i in range(0,len(waiting_time)):
                faraiand[i][3] = waiting_time[i]

            for i in range(0,len(response_time)):
                faraiand[i][4] = response_time[i]
            
            print("-" * 100)
            print("Name Faraiand\t Arrival Time\t Burst Time\t Waiting Time\t response_time")
            for i in range(0,len(faraiand)):
                print(f"{faraiand[i][0]}\t\t {faraiand[i][1]}\t\t {faraiand[i][2]}\t\t {faraiand[i][3]}\t\t {faraiand[i][4]}\t\t")

            print("-" * 20)

            AWT_list = []
            AAT_list = []
            for i in faraiand:
                AWT_list.append(i[3])
                AAT_list.append(i[4])

            AWT = round(sum(AWT_list) / len(faraiand),2)
            AAT = round(sum(AAT_list) / len(faraiand),2)

            print(f"AWT = {AWT}")
            print(f"AAt = {AAT}")
            print("-"*100)
            show_app()
        elif entekhab_karbar == "sjf":
            print("Shoma barname SJF ra entekhab kardid!")
            print("-"*100)
            def moratab_kardan():
                len_faraiand = len(faraiand)
                for i in range(0,len_faraiand):
                    for j in range(0,len_faraiand-1):
                        if faraiand[j][2] > faraiand[j+1][2]:
                            temp = faraiand[j]
                            faraiand[j] = faraiand[j+1]
                            faraiand[j+1] = temp
            faraiand = []
            while True:
                try:
                    info = []
                    name_faraiand = input("name faraiand ra vared konid va baraie kharej shodan name faraiand ra 'exit' begzarid: ")
                    info.append(name_faraiand)
                    if name_faraiand == "exit":
                        break
                    else:
                        zaman_vorod = int(input("Zaman vorod ra vared konid: "))
                        info.append(zaman_vorod)
                        zaman_enfejar = int(input("Zaman enfejar ra vared konid: "))
                        info.append(zaman_enfejar)
                        info.append(None)
                        info.append(None)
                except ValueError:
                    print("Baiad adad vared konid!")
                faraiand.append(info)
                moratab_kardan()    

            waiting_time = []
            zaman = faraiand[0][1]
            for i in faraiand:
                k = zaman - i[1]
                if k < 0 :
                    zaman = 0
                waiting_time.append(k)
                zaman += i[2]

            completion_spot = []
            response_time = []
            s1 = faraiand[0][1]
            for i in faraiand:
                m = s1 + i [2]
                completion_spot.append(m)
                s1 = m

            onsor_dovom_har_list = []
            for i in faraiand:
                onsor_dovom_har_list.append(i[2])

            for i,j in zip(completion_spot,onsor_dovom_har_list):
                result = i - j 
                response_time.append(result)

            for i in range(0,len(waiting_time)):
                faraiand[i][3] = waiting_time[i]

            for i in range(0,len(response_time)):
                faraiand[i][4] = response_time[i]
            
            print("-" * 100)
            print("Name Faraiand\t Arrival Time\t Burst Time\t Waiting Time\t response_time")
            for i in range(0,len(faraiand)):
                print(f"{faraiand[i][0]}\t\t {faraiand[i][1]}\t\t {faraiand[i][2]}\t\t {faraiand[i][3]}\t\t {faraiand[i][4]}\t\t")

            print("-" * 20)

            AWT_list = []
            AAT_list = []
            for i in faraiand:
                AWT_list.append(i[3])
                AAT_list.append(i[4])

            AWT = round(sum(AWT_list) / len(faraiand),2)
            AAT = round(sum(AAT_list) / len(faraiand),2)

            print(f"AWT = {AWT}")
            print(f"AAt = {AAT}")
            print("-"*100)
            show_app()
        elif entekhab_karbar == "srt":
            print("Shoma barname SRT ra entekhab kardid!")
            print("-"*100)
            import pandas as pd
            def SRT(data):
                import copy
                firstClone = copy.deepcopy(data)
                secondClone = copy.deepcopy(data)

                allEnterTimes = sorted(list(set(item['time'] for item in firstClone)))

                orderedData = []

                spendTime = allEnterTimes[0]
                secondEnterTime = allEnterTimes[1] if len(allEnterTimes) > 1 else None

                while firstClone:
                    available_tasks = [item for item in firstClone if item['time'] <= spendTime]
                    task = sorted(available_tasks, key=lambda x: x['service'])[0]

                    start = spendTime

                    if secondEnterTime:
                        if spendTime + task['service'] > secondEnterTime:
                            service = secondEnterTime - spendTime
                            secondEnterTime_index = allEnterTimes.index(secondEnterTime)
                            secondEnterTime = allEnterTimes[secondEnterTime_index + 1] if secondEnterTime_index + 1 < len(allEnterTimes) else None
                        else:
                            service = task['service']
                    else:
                        service = task['service']

                    end = start + service
                    spendTime = end

                    if service == task['service']:
                        firstClone = [item for item in firstClone if item['name'] != task['name']]
                    else:
                        for item in firstClone:
                            if item['name'] == task['name']:
                                item['service'] -= service

                    orderedData.append({**task, 'start': start, 'service': service, 'end': end})

                tableData = []
                for current in orderedData:
                    if tableData and tableData[-1]['name'] == current['name']:
                        lastItem = tableData[-1]
                        tableData[-1] = {**lastItem, 'service': lastItem['service'] + current['service'], 'end': current['end']}
                    else:
                        tableData.append(current)
                reversedTableData = list(reversed(tableData))

                lastOfEachItem = []
                for current in reversedTableData:
                    if not any(item['name'] == current['name'] for item in lastOfEachItem):
                        lastOfEachItem.append(current)

                result = []
                for current in secondClone:
                    currentItem = next(item for item in lastOfEachItem if item['name'] == current['name'])
                    waitingTime = currentItem['end'] - (current['service'] + current['time'])
                    answerTime = currentItem['end'] - current['service']
                    result.append({**current, 'waitingTime': waitingTime, 'answerTime': answerTime})
                    
                return {'tableData': tableData, 'result': result}

            def get_user_input():
                data = []
                num_tasks = int(input("Tedad vorodi hara moshakhas konid: "))
                for _ in range(num_tasks):
                    name = input("Name faraiand ra vared konid: ")
                    time = int(input(f"Zaman vorod {name} ra vared konid: "))
                    service = int(input(f"Zaman enfejar {name} ra vared konid: "))
                    data.append({'name': name, 'time': time, 'service': service})
                return data

            data = get_user_input()
            output = SRT(data)


            tableData_df = pd.DataFrame(output['tableData'])
            print("\nJadval data:")
            print(tableData_df.to_string(index=False))


            result_df = pd.DataFrame(output['result'])
            print("\nResult:")
            print(result_df.to_string(index=False))

            print("-"*50)
            majmoe_zamanvorod = []
            for i in output['result']:
                majmoe_zamanvorod.append(i['waitingTime'])
            majmoe_zamanservice = []

            for i in output['result']:
                majmoe_zamanservice.append(i['answerTime'])

            AWT = round(sum(majmoe_zamanvorod) / len(data),2)
            AAT = round(sum(majmoe_zamanservice)/ len(data),2)

            print(f"AWT = {AWT}")
            print(f"AAT ={AAT}")
            print("-"*100)
            show_app()
        elif entekhab_karbar == "mcpu":
            print("Shoma barname MCPU ra entekhab kardid!")
            print("-"*100)
            processes = []
            while True:
                try:
                    info = []
                    process_name = input("Name faraiand ra vared konid va baraie kharej shodan name faraiand ra 'exit' begzarid: ")
                    if process_name == "exit":
                        break
                    info.append(process_name)
                    
                    arrival_time = int(input("Zaman vorod ra vared konid: "))
                    info.append(arrival_time)
                    
                    burst_time = int(input("Zaman enfejar ra vared konid: "))
                    info.append(burst_time)
                    
                    info.append(None)
                    info.append(None)  
                    processes.append(info)
                except ValueError:
                    print("Baiad adad vared konid!")


            processes.sort(key=lambda x: x[1])

            cpu1_processes = []
            cpu2_processes = []

            cpu1_completion_time = 0
            cpu2_completion_time = 0

            for process in processes:
                if cpu1_completion_time <= cpu2_completion_time:
                    cpu1_processes.append(process)
                    cpu1_completion_time += process[2]
                else:
                    cpu2_processes.append(process)
                    cpu2_completion_time += process[2]

            def calculate_times(processes):
                current_time = 0
                waiting_times = []
                response_times = []
                completion_times = []

                for process in processes:
                    arrival_time = process[1]
                    burst_time = process[2]
                    
                    if current_time < arrival_time:
                        current_time = arrival_time 

                    waiting_time = current_time - arrival_time
                    completion_time = current_time + burst_time
                    response_time = completion_time - burst_time

                    waiting_times.append(waiting_time)
                    response_times.append(response_time)
                    completion_times.append(completion_time)

                    current_time = completion_time

                return waiting_times, response_times, completion_times

            cpu1_waiting_times, cpu1_response_times, cpu1_completion_times = calculate_times(cpu1_processes)
            cpu2_waiting_times, cpu2_response_times, cpu2_completion_times = calculate_times(cpu2_processes)

            for i in range(len(cpu1_processes)):
                cpu1_processes[i][3] = cpu1_waiting_times[i]
                cpu1_processes[i][4] = cpu1_response_times[i]

            for i in range(len(cpu2_processes)):
                cpu2_processes[i][3] = cpu2_waiting_times[i]
                cpu2_processes[i][4] = cpu2_response_times[i]

            print("-" * 100)
            print("CPU 1 Processes:")
            print("Name Faraiand\t Arrival Time\t Burst Time\t Waiting Time\t Response Time")
            for i in range(len(cpu1_processes)):
                print(f"{cpu1_processes[i][0]}\t\t {cpu1_processes[i][1]}\t\t {cpu1_processes[i][2]}\t\t {cpu1_processes[i][3]}\t\t {cpu1_processes[i][4]}")

            print("-" * 100)
            print("CPU 2 Processes:")
            print("Name Faraiand\t Arrival Time\t Burst Time\t Waiting Time\t Response Time")
            for i in range(len(cpu2_processes)):
                print(f"{cpu2_processes[i][0]}\t\t {cpu2_processes[i][1]}\t\t {cpu2_processes[i][2]}\t\t {cpu2_processes[i][3]}\t\t {cpu2_processes[i][4]}")


            cpu1_AWT = round(sum(cpu1_waiting_times) / len(cpu1_processes), 2)
            cpu1_ART = round(sum(cpu1_response_times) / len(cpu1_processes), 2)

            cpu2_AWT = round(sum(cpu2_waiting_times) / len(cpu2_processes), 2)
            cpu2_ART = round(sum(cpu2_response_times) / len(cpu2_processes), 2)

            print("-" * 20)
            print(f"CPU 1 AWT = {cpu1_AWT}")
            print(f"CPU 1 ART = {cpu1_ART}")
            print("-" * 20)
            print(f"CPU 2 AWT = {cpu2_AWT}")
            print(f"CPU 2 ART = {cpu2_ART}")
            print("-"*100)
            show_app()
        elif entekhab_karbar == "mlfq":
            print("Shoma barname MLFQ ra entekhab kardid!")
            print("-"*100)
            def MLFQ():
                data = []
                num_processes = int(input("Tedad faraiand ra vared konid: "))
                for i in range(num_processes):
                    name = input(f"Name faraiand {i + 1} ra vared konid: ")
                    time = int(input(f"Zaman vorod faraiand {i + 1} ra vared konid: "))
                    service = int(input(f"Zaman enfejar faraiand {i + 1} ra vared konid: "))
                    data.append({'name': name, 'time': time, 'service': service})

                first_cloned = data[:]
                second_clone = data[:]


                table_data = []
                sorted_data = sorted(first_cloned, key=lambda x: x['time'])
                spend_time = sorted_data[0]['time']
                current_quantum = 0
                group = []

                process_end_times = {item['name']: [] for item in data}

                while first_cloned:
                    all_coming_items = [item for item in first_cloned if item['time'] <= spend_time]
                    all_coming_items.sort(key=lambda x: x['time'])
                    current = next((item for item in all_coming_items if not any(group_item['name'] == item['name'] for group_item in group)), all_coming_items[0])
                    start = spend_time
                    service = min(current['service'], 2 ** current_quantum)
                    end = start + service
                    new_data = {'name': current['name'], 'start': start, 'service': service, 'end': end}
                    group.append(new_data)
                    process_end_times[current['name']].append(end)
                    spend_time = end
                    if service == current['service']:
                        first_cloned = [item for item in first_cloned if item['name'] != current['name']]
                    else:
                        first_cloned = [{**item, 'service': item['service'] - service} if item['name'] == current['name'] else item for item in first_cloned]
                    if len(group) == len(data) or not first_cloned:
                        current_quantum += 1
                        table_data.extend(group)
                        group = []

                result = []
                for item in second_clone:
                    current_item_end_times = process_end_times[item['name']]
                    total_end_time = sum(current_item_end_times)
                    answer_time = total_end_time - item['service']
                    result.append({'name': item['name'], 'waitingTime': current_item_end_times[-1] - (item['service'] + item['time']), 'answerTime': answer_time})
                return table_data, result
            table_data, result = MLFQ()

            import pandas as pd

            table_data_df = pd.DataFrame(table_data)
            result_df = pd.DataFrame(result)

            print("Jadval Data:")
            print(table_data_df)

            print("\nResult:")
            print(result_df)

            majmoe_zamanvorod = []
            for i in result:
                majmoe_zamanvorod.append(i["waitingTime"])

            majmoe_zamanservice = []
            for i in result:
                majmoe_zamanservice.append(i["answerTime"])

            print("-"*50)
            AWT = round(sum(majmoe_zamanvorod) / len(majmoe_zamanvorod),2)
            AAT = round(sum(majmoe_zamanservice) / len(majmoe_zamanservice),2)

            print(f"AWT = {AWT}")
            print(f"AAT = {AAT}")
            print("-"*100)
            show_app()
        elif entekhab_karbar == "asansor":
            print("Shoma barname Asansor ra entekhab kardid!")
            print("-"*100)
            Darkhast_shiar= int(input("Tedad darkhast ra vared konid: "))
            list_darkhastha = []
            for i in range(0,Darkhast_shiar):
                darkhastha = int(input(f"Shomare darkhast {i+1} ra vared konid: "))
                list_darkhastha.append(darkhastha)
            list_darkhastha.sort()

            haml = int(input("Shomare haml ra vared konid: "))

            print("-"*100)
            print("Result:")
            print(f"list_darkhastha = {list_darkhastha}")
            print(f"haml = {haml}")

            adad_bishtar_az_haml = []
            adad_kamtar_az_haml = []

            for i in list_darkhastha:
                if haml <= i:
                    adad_bishtar_az_haml.append(i)
                else:
                    adad_kamtar_az_haml.append(i)

            print(f"adad_bishtar_az_haml = {adad_bishtar_az_haml}")
            print(f"adad_kamtar_az_haml = {adad_kamtar_az_haml}")

            Asansor = []

            for i in adad_bishtar_az_haml:
                Asansor.append(i)
                print(Asansor)

            adad_kamtar_az_haml.reverse() # in barname Scan ast baraie tabdil shodan be Cscan in khat ra comment konid 
            for i in adad_kamtar_az_haml:
                Asansor.append(i)
                print(Asansor)
            print("-"*100)
            show_app()
        elif entekhab_karbar == "bankdaran":
            print("Shoma barname Bankdaran ra entekhab kardid!")
            print("-"*100)
            import numpy as np
            def max_zarfiat():
                rows = int(input("Tedad satr haie max ra vared konid: "))
                cols = int(input("Tedad soton haie max ra vared konid: "))
                hadaksar_zarfiat = np.empty((rows, cols), dtype=int)
                for i in range(rows):
                    for j in range(cols):
                        element = int(input(f"Adad noqte ({i+1},{j+1}) ra vared konid: "))
                        hadaksar_zarfiat[i, j] = element
                return hadaksar_zarfiat

            def allocation():
                rows = int(input("Tedad satr haie allocation ra vared konid: "))
                cols = int(input("Tedad soton haie allocation ra vared konid: "))
                allocation1 = np.empty((rows, cols), dtype=int)
                for i in range(rows):
                    for j in range(cols):
                        element = int(input(f"Adad noqte ({i+1},{j+1}) ra vared konid: "))
                        allocation1[i, j] = element
                return allocation1

            def manabe_baqi_mande():
                rows = int(input("Tedad satr haie manabe_baqi_mande ra vared konid: "))
                cols = int(input("Tedad soton haie manabe_baqi_mande ra vared konid: "))
                available = np.empty((rows, cols), dtype=int)
                for i in range(rows):
                    for j in range(cols):
                        element = int(input(f"Adad noqte ({i+1},{j+1}) ra vared konid: "))
                        available[i, j] = element
                return available

            max_matrix = max_zarfiat()
            allocation_matrix = allocation()
            available_matrix = manabe_baqi_mande()

            print(f"Max = \n{max_matrix}\n")
            print(f"Allocation = \n{allocation_matrix}\n")
            print(f"Manabe baqi mande = \n{available_matrix}\n")

            need = max_matrix - allocation_matrix
            print(f"Need = \n{need}\n")

            for i in range(need.shape[0]):
                if np.all(available_matrix >= need[i]):
                    available_matrix += allocation_matrix[i]
                    print(available_matrix)
                    print(f"System amn ast.")
                else:
                    print(f"System amn nist.")
            print("-"*100)
            show_app()