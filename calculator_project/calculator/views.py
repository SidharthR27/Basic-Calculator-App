from django.shortcuts import render

# Create your views here.

def home(request):
    # print(request.POST)
    return render(request, 'calculator/home.html')

def calculate(request):
    print(request.POST)
    number1 = request.POST.get("number1")
    number2 = request.POST.get("number2")
    number3 = request.POST.get("number3", "")  # Default to empty string if empty
    number4 = request.POST.get("number4", "")  # Default to empty string if empty
    operation = request.POST.get("operation")
    try:
        received_data = [number1,number2,number3,number4]
        print(received_data)
        numbers =[]

        # add only numbers from the POST Data to another list
        for number in received_data:
            if not number is "":
                numbers.append(float(number))
    except ValueError:
        return render(request, "calculator/home.html", {"error": "Please enter only valid numbers."})
    

    # Perform the operation on the numbers
    try :
        if operation == "add":
            result = sum(numbers)

        elif operation == "subtract":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num

        elif operation == "multiply":
            result = numbers[0]
            for num in numbers[1:]:
                result *= num

        elif operation == "divide":
            if 0 in numbers:
                raise ZeroDivisionError
            else:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
         
    except :
        return render(request, 'calculator/home.html', {"error": 'Division by zero is not allowed. ' })
    
    # print(result)
    




    return render(request, 'calculator/home.html', {"result": round(result, 3) })
