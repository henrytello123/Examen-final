import time

def mesureTime(function):
   def wrapper(*args, **kwargs):
       start = time.time()

       result = function(*args, **kwargs)

       total = time.time() - start
       print("La demora en la ejecución fue de: {}".format(total))

       return result

   return wrapper


@mesureTime
def div(a, b):
   time.sleep(1)
   division = a/b
   return division

"Ejem 1"
print("Division del primer ejemplo: ", div(1600, 800))

"Ejem 2"
print("Division del segundo ejemplo: ", div(500000000000, 25))