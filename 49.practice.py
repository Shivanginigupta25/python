def calculate_percentage(m1,m2,m3):
    marks= m1 + m2+m3
    per= (marks/300)*100
    r_per = round(per,2)
    return r_per
m1=int(input())
m2=int(input())
m3=int(input())
result= calculate_percentage(m1,m2,m3)
print(f"percentage {result}")