def calcAngle(h,m):
    
    hour_angle = (360/(12*60))*(h*60 + m ) # 360*( h/12 + m/60 )
    min_angle = 360/60*m
    angle = abs(hour_angle - min_angle)
    return min(angle, 360-angle)

print(calcAngle(3, 15))
# 7.50
print(calcAngle(3, 00))
# 90