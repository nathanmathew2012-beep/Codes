print("=== Smart School Day Planner ===")

print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()

weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()

homework = input("Is your homework done? (yes / no): ").strip().lower()

print()

print(f"=== Your Plan for {day} ===")

print("-" * 35)

if day in ('Saturday' , 'Sunday'):
    print('Day type : Last school day. Return library books today')
elif day=='Monday':
    print (2)
else: 
    print (5)
if weather =='sunny' and homework== 'yes':
    print('go out')
if weather =='cloudy' or weather== 'rainy':
    print ('dont go out')
if not (homework == 'yes'):
    print('dont go out')
    # Topic 5 -- Combining AND + OR + NOT together

if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework, then watch your favourite show.")

elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day - you are prepared!")

elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend weather - head outside and have fun!")

else:
    print("Best plan : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")

