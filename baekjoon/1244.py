switch_count = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())

def toggle_switch(index):
    switch_status[index] = (switch_status[index] + 1) % 2

def m_student(num):
    for i in range(1, switch_count + 1):
        if i % num == 0:
            toggle_switch(i - 1)

def w_student(num):
    toggle_switch(num - 1)  # 중심 스위치 상태 변경
    offset = 1
    while num - 1 - offset >= 0 and num - 1 + offset < switch_count and switch_status[num - 1 - offset] == switch_status[num - 1 + offset]:
        toggle_switch(num - 1 - offset)
        toggle_switch(num - 1 + offset)
        offset += 1

for _ in range(student_num):
    student_gen, num = map(int, input().split())
    if student_gen == 1:
        m_student(num)
    else:
        w_student(num)

for i, status in enumerate(switch_status, start=1):
    print(status, end=' ')
    if i % 20 == 0:
        print()
if len(switch_status) % 20 != 0:
    print()
