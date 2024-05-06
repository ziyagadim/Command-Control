import psutil

running_processes = psutil.process_iter()
for process in running_processes:
    print(process)

psutil.Process(17100).kill()