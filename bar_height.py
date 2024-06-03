def bar_height(value):
    if value <= 50: return round(translate(value,0,50,0,19),0)
    elif value <= 100: return round(translate(value,51,100,20,38),0)
    elif value <= 200: return round(translate(value,101,200,39,57),0)
    elif value <= 300: return round(translate(value,201,300,58,76),0)
    else: return round(translate(value,301,500,77,96),0)
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)
 
print(bar_height(50))
print(bar_height(100))
print(bar_height(100))
print(bar_height(200))
print(bar_height(300))
print(bar_height(500))