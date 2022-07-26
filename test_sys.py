import sys

std_input = sys.stdin # модуль потока входных данных
std_out = sys.stdout # модуль потока выходных данных

# цикл чтения входного потока данных
for line in std_input:
    # Завершение работы программы если получено сообщение 'exit'
    if "exit" == line.strip():
        std_out.write("Производим выход из программы.")
        exit(0)
    else:
        std_out.write(f"Собщение из std_input:\n {line}")